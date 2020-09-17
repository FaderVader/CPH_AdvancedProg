from datetime import datetime as timeNow

def logger(fileName):
    tabStop = 14
    def inner(msg, level="INFO"):        
        with open(fileName, 'a') as file:  #
            time = timeNow.today().strftime('%H:%M')
            header = f'{time} - {level}'
            padding = ' '*(tabStop-len(header))
            file.write(f'{header}{padding} - {msg}\n')
    return inner

# inner functions:
# https://www.geeksforgeeks.org/python-inner-functions/

# open file and append, tips:
# https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python