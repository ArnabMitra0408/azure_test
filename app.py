import os
import logging
from applicationinsights.flask.ext import AppInsights


from opencensus.ext.azure.log_exporter import AzureLogHandler

#logger = logging.getLogger(__name__)
#logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=e01274f4-cb23-4bf0-b457-6b630481eef3;IngestionEndpoint=https://centralindia-0.in.applicationinsights.azure.com/;LiveEndpoint=https://centralindia.livediagnostics.monitor.azure.com/'))

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
app = Flask(__name__)

app.config['APPINSIGHTS_INSTRUMENTATIONKEY'] = 'e01274f4-cb23-4bf0-b457-6b630481eef3'
appinsights = AppInsights(app)

@app.route('/')
def index():
   print('Request for index page received')
   #logger.warning('Going to index Page')

   app.logger.warn('This is a warning log message')

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
       app.logger.debug('This is a debug log message')
       app.logger.info('This is an information log message')
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       #logger.error('Add Name Please')
       app.logger.info('This is an information log message')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
