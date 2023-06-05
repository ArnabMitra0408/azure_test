import os
import logging

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
app = Flask(__name__)
logger_warning = logging.getLogger('warning')
logger_error = logging.getLogger('error')
logger_info = logging.getLogger('info')
logger_critical = logging.getLogger('critical')

@app.route('/')
def index():
   print('Request for index page received')
   logger_warning.warning("Its a Warning that index page is received",exc_info=True)

   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       logger_error.error("It is a error log saying that Request for hello page is received",exc_info=True)
    
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       logger_critical.critical("It is a critical log saying no name is received",exc_info=True)
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
