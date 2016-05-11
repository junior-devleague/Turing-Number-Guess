# An internet client that guesses numbers on a sever
# by Ciril Rozic for Devleague and Punahou School, 2015
# based on the simple internet chat program from raspberrypi.org

#use: python number_client.py server_IP_address

import network
import sys
import time

if (len(sys.argv) < 2):
  sys.exit()

score = 0
guessed_number = 1

def heard(phrase):
  global score
  global guessed_number

  print("them:" + phrase)
  if phrase == "higher":
     guessed_number=guessed_number*2 #double it!
  elif phrase == "lower":
     guessed_number=guessed_number-1 #decrement it.
  elif phrase == "CORRECT!!!":
    score = 1
  if score == 0 and network.isConnected():
    print("me:" + str(guessed_number))
    network.say(str(guessed_number)) 
      
network.call(sys.argv[1], whenHearCall=heard)

while score == 0 and network.isConnected():
  time.sleep(5)
  
