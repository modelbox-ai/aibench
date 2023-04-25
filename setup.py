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

import pathlib
import re
from setuptools import setup, find_packages


def read_version():
    p = pathlib.Path(__file__)
    p = p.parent / 'pytest_aibenchmark' / '__init__.py'
    with p.open('r') as f:
        for line in f:
            if line.startswith('__version__'):
                line = line.split('=')[1].strip()
                match = re.match(r"^['\"](\d+\.\d+\.\d+\w*)['\"]", line)
                if match:
                    return match.group(1)
    raise ValueError('Unable to compute version')


def read(fname):
    file_path = pathlib.Path(__file__).parent / fname
    with file_path.open('r', encoding='utf-8') as f:
        return f.read()


setup(
    name='pytest-aibenchmark',
    version=read_version(),
    author='Modelbox Team',
    maintainer='Modelbox Team',
    license='Apache License 2.0',
    project_urls=dict(Source='https://github.com/modelbox-ai/pytest-aibenchmark',
                      Tracker='https://github.com/modelbox-ai/pytest-aibenchmark/issues'),
    description='Pytest plugin for analyzing resource usage.',
    # long_description=read('README.rst'),
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=['pytest', 'requests', 'psutil>=5.1.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache License 2.0',
    ],
    entry_points={
        'pytest11': [
            'aibenchmark = pytest_aibenchmark.pytest_aibenchmark',
        ],
    },
)
