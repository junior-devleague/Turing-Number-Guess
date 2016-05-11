# An internet server that responds to a guessing client
# by Ciril Rozic for Devleague and Punahou School, 2015
# based on the simple internet chat program from raspberrypi.org

#use: python number_server.py 1234

import network
import sys
import time

if (len(sys.argv) < 2):
  sys.exit()

score=0
imagined_number=int(sys.argv[1])

def heard(phrase):
  global score

  print("them:" + phrase)
  guessed_number = int(phrase)
  #time.sleep(1) #pause here to make the Pi seem human
  if network.isConnected():
    if imagined_number > guessed_number:
       network.say("higher")
    elif imagined_number == guessed_number:
       network.say("CORRECT!!!")
       score = 1
    else:
       network.say("lower")  

network.wait(whenHearCall=heard) #wait for quiz taker to connect

if network.isConnected():
  network.say("Guess a number!")

while score == 0 and network.isConnected():
  time.sleep(3)

