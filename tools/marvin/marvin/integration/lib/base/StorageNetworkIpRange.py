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
from marvin.integration.lib.base import CloudStackEntity
from marvin.cloudstackAPI import createStorageNetworkIpRange
from marvin.cloudstackAPI import listStorageNetworkIpRange
from marvin.cloudstackAPI import updateStorageNetworkIpRange
from marvin.cloudstackAPI import deleteStorageNetworkIpRange

class StorageNetworkIpRange(CloudStackEntity.CloudStackEntity):


    def __init__(self, items):
        self.__dict__.update(items)


    @classmethod
    def create(cls, apiclient, factory, **kwargs):
        cmd = createStorageNetworkIpRange.createStorageNetworkIpRangeCmd()
        [setattr(cmd, factoryKey, factoryValue) for factoryKey, factoryValue in factory.__dict__.iteritems()]
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        storagenetworkiprange = apiclient.createStorageNetworkIpRange(cmd)
        return StorageNetworkIpRange(storagenetworkiprange.__dict__)


    @classmethod
    def list(self, apiclient, **kwargs):
        cmd = listStorageNetworkIpRange.listStorageNetworkIpRangeCmd()
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        storagenetworkiprange = apiclient.listStorageNetworkIpRange(cmd)
        return map(lambda e: StorageNetworkIpRange(e.__dict__), storagenetworkiprange)


    def update(self, apiclient, **kwargs):
        cmd = updateStorageNetworkIpRange.updateStorageNetworkIpRangeCmd()
        cmd.id = self.id
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        storagenetworkiprange = apiclient.updateStorageNetworkIpRange(cmd)
        return storagenetworkiprange


    def delete(self, apiclient, **kwargs):
        cmd = deleteStorageNetworkIpRange.deleteStorageNetworkIpRangeCmd()
        cmd.id = self.id
        [setattr(cmd, key, value) for key,value in kwargs.iteritems()]
        storagenetworkiprange = apiclient.deleteStorageNetworkIpRange(cmd)
        return storagenetworkiprange