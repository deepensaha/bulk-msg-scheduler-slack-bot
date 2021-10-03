import logging

# Create and Configure Logger
logging.basicConfig(
    filename = 'app.log',
    format = '%(asctime)s %(message)s',
    filemode = 'a+'
)

# Create Logger Object
logger = logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)