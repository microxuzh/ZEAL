from app import app
import os
import logging
import logging.config


# logging.basicConfig(
#     filename='example.log',
#     level=logging.WARNING,
#     format=
#     '%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%b/%y %I:%M:%S %p')
logging.config.fileConfig('logger.conf')
logger = logging.getLogger('infoLogger')
logger.info('This is info message')
logger.error('This is error message')

# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8000, debug=app.config['DEBUG'])