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


def pytest_addoption(parser):
    group = parser.getgroup('aibenchmark')
    group.addoption('--f', action='store_true', dest='mtr_none', help='Disable all traces')

def pytest_configure(config):
    config.addinivalue_line("markers", "aibenchmark_skip_test: mark test to be only executed.")

def pytest_runtest_setup(item):
    pass



