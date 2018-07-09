#!/usr/bin/env python

from classzs import Employee
from Boss import *
emp1 = Employee("Zara", 2200)
emp2 = Employee("Xile", 3350)
emp1.displayEmployee()
boss = Boss("Arma", "cccia")
boss.displayBoss()
emp1.displayCount()
del emp2
# emp2.displayEmployee()
emp1.displayCount()