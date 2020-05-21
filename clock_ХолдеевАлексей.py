from os import system
from time import sleep
from datetime import datetime


def translate(text):

  text = str(text)

  letters = []
  for letter in text:
    letters.append(NUMBERS[letter])
  for i in range(5):
    line = ''
    for letter in letters:
      line += letter.splitlines()[i] + ' '
    print(line)


NUMBERS = {
'1': u"""\
 ██   
███   
 ██   
 ██   
████  
""",
'3': u'''\
██████ 
    ██ 
██████ 
    ██ 
██████ ''',
'2': u'''\
██████ 
    ██ 
██████ 
██     
██████ ''',
'4': u'''\
██  ██ 
██  ██ 
██████ 
    ██ 
    ██ ''',
'5': u'''\
██████ 
██     
██████ 
    ██ 
██████ ''',
'6': u'''\
██████ 
██     
██████ 
██  ██ 
██████ ''',
'7': u'''\
██████ 
    ██ 
    ██ 
    ██ 
    ██ ''',
'8': u'''\
██████ 
██  ██ 
██████ 
██  ██ 
██████ ''',
'9': u'''\
██████ 
██  ██ 
██████ 
    ██ 
██████ ''',
'0': u'''\
██████ 
██  ██ 
██  ██ 
██  ██ 
██████ ''',
' ': u'''\
       
       
       
       
       ''',
':': u'''\
       
  ██   
       
  ██   
       ''',
}

def clock():
  while True:
    time = datetime.now()
    dt = datetime.strftime(time,'%H:%M:%S')
    translate(dt)
    sleep(1)
    system('clear')
      
clock()