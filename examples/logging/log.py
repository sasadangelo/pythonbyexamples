import logging

# Log on stdout
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.debug('This is a log message.')
#logging.disable(logging.CRITICAL)

# Log on file
#logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.debug('This is a log message.')
#logging.disable(logging.CRITICAL)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('logfile.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('This is a test log message.')
