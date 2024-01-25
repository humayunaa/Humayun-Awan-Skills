#!/usr/bin/env python3

class Triathlete():

   def __init__(self, name, id):
      self.name = name
      self.tid = id

   def __str__(self):
      return "Name: {}\nID: {}".format(self.name, self.tid)

def sort_on(t):
   return t.name

class Triathlon():

   def __init__(self):
      self.d = {}

   def add(self, other):
      self.d[other.tid] = other

   def remove(self, tid):
      if tid in self.d:
         del self.d[tid]

   def lookup(self, tid):
      if tid in self.d:
         return self.d[tid]

   def __str__(self):
      r = "\n".join([f'{t}' for t in sorted(self.d.values(), key=sort_on)])
      return r