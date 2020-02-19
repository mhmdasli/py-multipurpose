import os.path
import time
import threading
import logging
import src.app as myApp
import json
from flask import Flask, escape, request, render_template, url_for, Response
import asyncio
from src.helpers import mylogger

# init root logger
logger = mylogger.create_logger('root')
logger.info("Primary App Starts")

#--------------------------------------------------------------------------------------
# define app
app = Flask(__name__)
# define routes
@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'GET':
        return render_template('admin-login.html')
    if request.method == 'POST':
        logger.info(request.form.to_dict())
        if(request.form["password"] == '123'):
            return render_template('admin.html')
        else:
            return render_template('admin-login.html',status='Wrong password')

@app.route('/api/faces', methods=['POST'])
def get_faces():
    return {"net_faces": shared_memory["net_faces"]}

if __name__ == "__main__":
    # start async app thread
    shared_memory = {}
    myapp = threading.Thread(target=myApp.start,args=(shared_memory,))
    myapp.start()
    # run app
    app.run(debug=False, threaded=False)
else:
    # start async app thread
    shared_memory = {}
    myapp = threading.Thread(target=myApp.start,args=(shared_memory,))
    myapp.start()
    