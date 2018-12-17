#!/usr/bin/env python
#coding=utf-8
import sys
import os
import time
import ConfigParser

class Common:

    @staticmethod
    def LoadConfig():
        cfg_fn = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "\\config.cfg")
        required_ops = [("Base", "AccessKeyId"), ("Base", "AccessKeySecret"), ("Base", "LogEndpoint"), ("Base", "LogProject"), ("Base", "Logstore"), ("Base", "OSSEndpoint"), ("Base", "OSSBucketName")]
        #optional_ops = [("Optional", "SecurityToken")]
        
        # Read config.cfg and parse the configuration parameters
        parser = ConfigParser.ConfigParser()
        parser.read(cfg_fn)

        # Check if any of the manadatory parameters are missing
        for sec,op in required_ops:
            if not parser.has_option(sec, op):
                sys.stderr.write("ERROR: need (%s, %s) in %s.\n" % (sec,op,cfg_fn))
                sys.stderr.write("Read README to get help inforamtion.\n")
                sys.exit(1)

        # Assign each of the configuration parameters values to separate varaiables
        accessKeyId = parser.get("Base", "AccessKeyId")
        accessKeySecret = parser.get("Base", "AccessKeySecret")
        logEndPoint = parser.get("Base", "LogEndpoint")
        logProject = parser.get("Base", "LogProject")
        logStore = parser.get("Base", "Logstore")
        ossEndPoint = parser.get("Base", "OSSEndpoint")
        ossBucketName = parser.get("Base", "OSSBucketName")

        securityToken = ""

        if parser.has_option("Optional", "SecurityToken") and parser.get("Optional", "SecurityToken") != "$SecurityToken":
            securityToken = parser.get("Optional", "SecurityToken")

        return accessKeyId,accessKeySecret,logEndPoint,logProject,logStore,ossEndPoint,ossBucketName,securityToken
