#!/usr/bin/env python
#coding=utf8

import sys
import os,json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import time
from common import Common



import time
from aliyun.log.logitem import LogItem
from aliyun.log.logclient import LogClient
from aliyun.log.getlogsrequest import GetLogsRequest
from aliyun.log.putlogsrequest import PutLogsRequest
from aliyun.log.listlogstoresrequest import ListLogstoresRequest
from aliyun.log.gethistogramsrequest import GetHistogramsRequest

class Log:
    @staticmethod
    def write(client,topic,source,contents):
        # contents = [('Data', 'Data1')]
        logitemList = [] # LogItem list
        logItem = LogItem()
        logItem.set_time(int(time.time()))
        logItem.set_contents(contents)
        logitemList.append(logItem)
        req = PutLogsRequest(project, logstore, topic, source, logitemList)
        res = client.put_logs(req)
        res.log_print()
