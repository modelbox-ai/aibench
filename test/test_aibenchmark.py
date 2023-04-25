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
import sqlite3


def test_aibenchmark_cmd_test(testdir):
    """Make sure that aibenchmark does the job without impacting user tests."""
    # create a temporary pytest test module
    testdir.makepyfile(""" """)

    # run pytest with the following cmd args
    result = testdir.runpytest('-vv', '-s', '--help')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(['aibenchmark:'])

def test_aibenchmark_basic_test(testdir):
    """Make sure that aibenchmark does the job without impacting user tests."""
    # create a temporary pytest test module
    testdir.makepyfile("""
    import time
    def test_ok():
        time.sleep(0.5)
        x = ['a' * i for i in range(100)]
        assert len(x) == 100
""")

    # run pytest with the following cmd args
    result = testdir.runpytest('-vv', '-s')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(['*::test_ok PASSED*'])



def test_aibenchmark_pytest_skip_marker(testdir):
    """Make sure that pytest-aibenchmark does the job without impacting user tests."""

    # create a temporary pytest test module
    testdir.makepyfile("""
    import pytest
    import time
    @pytest.mark.skip("Some reason")
    def test_skipped():
        assert True
""")

    # run pytest with the following cmd args
    result = testdir.runpytest('-v')

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(['*::test_skipped SKIPPED*'])
