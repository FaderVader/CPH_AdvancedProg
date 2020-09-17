from myLogger import logger
import sys

log = logger('logfile.txt') #sys.stdout 'logfile.txt'
log('Hello World')
log('Hello Cruel World', level='ERROR')
log('Operation was a total succes, but the patient died', level='SUCCES')