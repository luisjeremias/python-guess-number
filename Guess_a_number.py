import random
import re
from time import sleep

class Guess:
  def __init__(self):
    self.minimum = 0
    self.maximum = 100
    self.guess = random.randint(self.minimum,self.maximum)

  def start(self):
    self.guess_number()

  def guess_number(self):
    try:
     the_guess = int(input('Chute um numero de 0 á 100: '))
     if the_guess == self.guess:
       print('Voce acertou')
     elif the_guess > self.guess:
       print('Chute um valor menor!')
       sleep(1)
       self.guess_number()
     elif the_guess < self.guess:
       print('Chute um valor maior!')
       sleep(1)
       self.guess_number()

    except ValueError:
      print('Por favor digite apenas numeros!')
      self.guess_number()


new_guess = Guess()
new_guess.start()