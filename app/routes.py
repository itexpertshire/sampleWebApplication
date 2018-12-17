
import os,sys,time
from app import app
from flask import render_template, flash, redirect,request
import oss2

from aliyun.log.logclient import LogClient

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")

from common import Common
from log import Log

#Load config values
accessKeyId,accessKeySecret,logEndPoint,logProject,logStore,ossEndPoint,ossBucketName,securityToken = Common.LoadConfig()

#Initialise OSS authentication
auth = oss2.Auth(accessKeyId, accessKeySecret)

# Initialise Log Service authentication client
client = LogClient(logProject+'.'+logEndPoint, accessKeyId, accessKeySecret)

#Instantiate OSS bucket
bucket = oss2.Bucket(auth, ossEndPoint, ossBucketName)

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/upload',methods = ['GET', 'POST'])
def upload_file():
   print (accessKeyId)
   print (accessKeySecret)
   if request.method == 'POST':
      f = request.files['file']
      try:
         bucket.put_object(f.filename,'CustomUpload')
         flash('File uploaded successfully!')

         # In case of file upload exceptions, log the exceptions into Log Serivce for automated alert notification
      except Exception, e:
         flash('File upload failure!')
         print("Unexpected error:", str(e))     
         contents = [('Msg', str(e) )]
         #Call write method from Log class to upload the log message into Log Service
         Log.write(client, logProject, logStore, '', '', contents)
    
   return render_template('upload.html')