from datetime import datetime as timeNow
import sys

def logger(file):
    tabStop = 14
    def inner(msg, level="INFO"):        
        with open('logfile.txt', 'a') as file: # if we don't hide 'file', we get output to console instead
            time = timeNow.today().strftime('%H:%M')
            header = f'{time} - {level}'
            padding = ' '*(tabStop-len(header))
            file.write(f'{header}{padding} - {msg}\n')
    return inner

log = logger(sys.stdout)
log('Hello World')
log('Hello Cruel World', level='ERROR')