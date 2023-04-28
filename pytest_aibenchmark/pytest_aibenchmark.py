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

import pytest
import datetime
from pytest_aibenchmark.session import PyTestAiBenchSession
from pytest_aibenchmark.db import PyTestAiBenchDBTblCases


def pytest_addoption(parser):
    group = parser.getgroup('aibenchmark')
    group.addoption('--db-path', action='store_true',
                    dest='mtr_none', help='set database path')


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "aibenchmark_skip_test: mark test to be only executed.")


def pytest_runtest_setup(item: pytest.Item):
    pass


def pytest_runtest_teardown(item, nextitem):
    pass


def pytest_runtest_call(item):
    pass


def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    if call.when == 'call':
        setattr(item, 'test_run_duration', call.stop - call.start)
    elif call.when == 'teardown':
        duration = getattr(item, 'test_run_duration', None)
        if duration is None:
            return
        p = PyTestAiBenchDBTblCases()
        p.name = item.name
        p.begin_time = datetime.datetime.fromtimestamp(call.start)
        p.end_time = datetime.datetime.fromtimestamp(call.stop)
        p.type = "inference"
        p.duration = duration
        p.qps = 1.0 / 1
        p.latency = 1
        p.accuracy = 0.0
        p.res = 0
        p.status = "success"
        p.save()


def pytest_sessionstart(session: pytest.Session):
    aibenchmark = PyTestAiBenchSession()
    aibenchmark.init()
    session.aibenchmark = aibenchmark


def pytest_sessionfinish(session: pytest.Session, exitstatus):
    session.aibenchmark = None
