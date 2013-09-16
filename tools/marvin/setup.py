#!/usr/bin/env python
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from distribute_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
    except ImportError:
        raise RuntimeError("python setuptools is required to build Marvin")


VERSION = '0.2.0'

import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

setup(name="Marvin",
    version=VERSION,
    description="Marvin - Python client for Apache CloudStack",
    author="Edison Su",
    author_email="Edison.Su@citrix.com",
    maintainer="Prasanna Santhanam",
    maintainer_email="tsp@apache.org",
    long_description="Marvin is the Apache CloudStack python client written around the unittest framework",
    platforms=("Any",),
    packages=["marvin", "marvin.cloudstackAPI",
              "marvin.deployer", "marvin.entity", "marvin.factory", "marvin.factory.data",
              "marvin.generate", "marvin.legacy",
              "marvin.sandbox", "marvin.sandbox.advanced", "marvin.sandbox.advancedsg", "marvin.sandbox.basic",
              "marvin.test"],
    license="LICENSE.txt",
    install_requires=[
        "mysql-connector-python",
        "requests",
        "paramiko",
        "nose",
        "simplejson",
        "factory_boy",
        "should-dsl",
        "inflect",
    ],
    py_modules=['marvin.marvinPlugin'],
    zip_safe=False,
    entry_points={
        'nose.plugins': ['marvinPlugin = marvin.marvinPlugin:MarvinPlugin']
    },
)
