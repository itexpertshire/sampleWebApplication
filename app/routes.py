from app import app
from flask import render_template, flash, redirect,request
from app.forms import LoginForm
from Log import Log
import oss2

endpoint = 'oss-cn-shenzhen.aliyuncs.com' # Suppose that your bucket is in the Hangzhou region.

auth = oss2.Auth('LTAIqo5BFYdWSvZD', 'kS2ezP0t81QHBwSTciUQybGxmwrHQP')
bucket = oss2.Bucket(auth, endpoint, 'mybatchjobscripts')

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/upload',methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      bucket.put_object(f.filename,'CustomUpload')
      flash('File uploaded successfully!')
   return render_template('upload.html')
	
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)