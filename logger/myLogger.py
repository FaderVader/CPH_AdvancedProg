from datetime import datetime as timeNow
import sys

def logger(file):
    tabStop = 14
    def inner(msg, level="INFO"):        
        with open('logfile.txt', 'a') as f: 
            time = timeNow.today().strftime('%H:%M')
            header = f'{time} - {level}'
            padding = ' '*(tabStop-len(header))
            f.write(f'{header}{padding} - {msg}\n')
    return inner

log = logger(sys.stdout)
log('Hello World')
log('Hello Cruel World', level='ERROR')