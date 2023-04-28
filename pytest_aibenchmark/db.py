# -*- coding: utf-8 -*-
#
# Copyright 2023 The Modelbox Project Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from peewee import *
from pytest_aibenchmark.db_table.tb_base import database_proxy
from pytest_aibenchmark.db_table.tb_cases import PyTestAiBenchDBTblCases
from pytest_aibenchmark.db_table.tb_resource_stat import PyTestAiBenchDBTblResourceStat

db = None

class AIBenchmarkDBBase(object):
    def __init__(self):
        self._db = None

    def create(self):
        return self.db


class AIBenchmarkDBSqlite(AIBenchmarkDBBase):
    def __init__(self, db_path: str):
        self._db_path = db_path
        self._pragmas = {}

    def cache_size(self, size: int):
        self._pragmas['cache_size'] = size

    def set_db_filepath(self, db_path: str):
        self._db_path = db_path

    def create(self):
        return SqliteDatabase(self._db_path, pragmas=self._pragmas)


class AIBenchmarkDBMysql(AIBenchmarkDBBase):
    def __init__(self, host: str, port: int, user: str, password: str, db_name: str):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._db_name = db_name

    def create(self):
        return MySQLDatabase(self._db_name, user=self._user, password=self._password, host=self._host, port=self._port)


class PyTestAiBenchDB(object):
    def __init__(self):
        self._db = None

    def init(self, db_creator: AIBenchmarkDBBase = None):
        global db
        if db is not None:
            self._db = db
            return
    
        self._db = db_creator.create()
        if self._db is None:
            raise Exception("DB path is invalid.")

        database_proxy.initialize(self._db)
        
        self._db.connect()
        self._db.create_tables(
            [PyTestAiBenchDBTblCases, PyTestAiBenchDBTblResourceStat])
        db = self._db
