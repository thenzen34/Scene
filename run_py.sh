#!/usr/bin/env python3
# coding: utf-8



import class_test_use

#import simple_graphics_demo


quit();

class test(object):

  someval = 0;

  def __init__(self, start=1):
    self.someval = start

  def some(self):
    return self;

  def hello(self):
    return "test some hello text";

  def increment(self):
    self.someval += 1
    return self

  def decrement(self):
    self.someval -= 1
    return self

  def getVal(self):
    return self.someval

from class_test import test

t = test(1);
print(t.some().increment().increment().decrement().someval);

points = [];

for ix in range(10):
  points.append([ix, ix]);

print(points);

first = points.pop(0);

last = first;

for next in points:
  print(last, next);
  last = next;

print(last, first);
quit();

"""
choices = {'a': 1, 'b': 2}
result = choices.get(1, 'default')

print(result)

for number in range(10):
    print(0 if number % 2 == 0 else 1, end = "")
"""

from class_test import test

t = test(1);
print(t.some().increment().increment().decrement().someval);
quit();

def tt():
  print("hello")

A = [1, 2]
A.append(3)
B = list(range(5))
#A.push(4)
print(A)

print(A.pop())
print(A)
print(B)        

quit()

"""
for number in range(10):
    if number % 2 == 0:
        print(number)
"""


"""
import serial
 
found = False
 
for i in range(64) :
  try :
    port = "/dev/ttyS%d" % i
    ser = serial.Serial(port)
    ser.close()
    print("Найден последовательный порт: ", port)
    found = True
  except serial.serialutil.SerialException :
    pass
 
if not found :
  print("Последовательных портов не обнаружено")
"""

import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 400, 400)

window.getMouse()

window.close()