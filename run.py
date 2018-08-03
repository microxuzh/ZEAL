from app import app
import os
import logging
import logging.config


# logging.basicConfig(
#     filename='example.log',
#     level=logging.INFO,
#     format=
#     '%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%b/%y %I:%M:%S %p')


logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('example')
#"application" code
# logger.debug("debug message")
# logger.info("info message")
# logger.warn("warn message")
# logger.error("error message")
# logger.critical("critical message")

# logHello = logging.getLogger("hello")
# logHello.info("Hello world!")


# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')

if __name__ == '__main__':
    # app.jinja_env.auto_reload = True
    app.run(host="0.0.0.0", port=8000, debug=app.config['DEBUG'])