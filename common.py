#!/usr/bin/env python
#coding=utf8
import sys
import os
import time
import ConfigParser

class Common:

    @staticmethod
    def LoadConfig():
        cfg_fn = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\config.cfg")
        required_ops = [("Base", "AccessKeyId"), ("Base", "AccessKeySecret"), ("Base", "Endpoint")]
        optional_ops = [("Optional", "SecurityToken")]

        parser = ConfigParser.ConfigParser()
        parser.read(cfg_fn)
        for sec,op in required_ops:
            if not parser.has_option(sec, op):
                sys.stderr.write("ERROR: need (%s, %s) in %s.\n" % (sec,op,cfg_fn))
                sys.stderr.write("Read README to get help inforamtion.\n")
                sys.exit(1)

        accessKeyId = parser.get("Base", "AccessKeyId")
        accessKeySecret = parser.get("Base", "AccessKeySecret")
        endpoint = parser.get("Base", "Endpoint")
        securityToken = ""
        if parser.has_option("Optional", "SecurityToken") and parser.get("Optional", "SecurityToken") != "$SecurityToken":
            securityToken = parser.get("Optional", "SecurityToken")
            return accessKeyId,accessKeySecret,endpoint,securityToken

        return accessKeyId,accessKeySecret,endpoint,""
