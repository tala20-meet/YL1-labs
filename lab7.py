#problem1
''''import tkinter as tk
from tkinter import simpledialog

#Then when ever you want to ask the user for input use this code:
greeting = simpledialog.askstring("Input", "Hello, possible pirate! What's the password?", parent=tk.Tk().withdraw())
if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")'''


#problem2
'''import tkinter as tk
from tkinter import simpledialog

year = int(simpledialog.askstring("Input", "Greetings! What is your year of origin?", parent=tk.Tk().withdraw()))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")'''


#problem3
'''class Person:
  def __init__(self, first_name, last_name):
    self.first = first_name
    self.last = last_name
  def speak(self):
      print("My name is "+ self.first+" "+ self.last)

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")


me.speak()
you.speak()'''

#problem4




