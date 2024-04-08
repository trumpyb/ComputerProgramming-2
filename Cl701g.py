class Person:
  def __init__(self, first, last):
    self._first = first
    self._last = last

  def getName(self):
    return f"{self._last}, {self._first}"


class Student(Person):
  def __init__(self, first, last, gpa):
    super().__init__(first, last)
    self.gpa = gpa

class Teacher(Person):
  def __init__(self, first, last, numStudents):
    super().__init__(first, last)
    self.numStudents = numStudents

class Admin(Person):
  def __init__(self, first, last, word):
    super().__init__(first, last)
    self.word = word
    