#!/usr/bin/env python
#coding=utf-8

import sys
import os,json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

import time
import time
from aliyun.log.logitem import LogItem
from aliyun.log.putlogsrequest import PutLogsRequest

class Log:
    @staticmethod
    def write(client, project, logstore, topic, source, contents):
        # contents = [('Data', 'Data1')]
        logitemList = [] # LogItem list
        logItem = LogItem()
        logItem.set_time(int(time.time()))
        logItem.set_contents(contents)
        logitemList.append(logItem)
        req = PutLogsRequest(project, logstore, topic, source, logitemList)
        res = client.put_logs(req)
        res.log_print()