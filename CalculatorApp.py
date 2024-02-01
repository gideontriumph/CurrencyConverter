"""
    Name: CalculatorApp.py
    Author: Triumhp Ogbonnia
    Created: 2/1/24
    Purpose: A calculator app in python using Tkinter GUI
"""
# Import all necessary libraries
from tkinter import *
import tkinter.font as font
from functools import partial
import ctypes
import json
import re
import math

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Colors
buttonColor = (255, 255, 255)
historyPanelBackgrond = (255, 255, 255)

# Tkinter Setup
root = Tk()
root.geometry("550x270")
root.title("Calculator")

# Set Icon
photo = PhotoImage(file = "icon.png")
root.iconphoto(False, photo)

# Loading font from font name
myFont = font.Font(family='Condolas', size=12)

formulas = [
    ['Pythagoras->c', '(({a}**2)+({b}**2))**0.5 ? a=5 & b=5'],
    ['Pythagoras->c**2', '({a}**2)+({b}**2) ? a=5 & b=5'],
    ['pq->(x1, x2)', '-({p}/2) + sqrt(({p}/2)**2 - ({q})), -({p}/2) - sqrt(({p}/2)**2 - ({q})) ? p=-1 & q=-12'],
    ['abc->(x1, x2)', 'quadratic_formula({a}, {b}, {c}) ? a=1 & b=5 & c=6'],
    ['Incline->y', '{m}*{x} + {q} ? m=4 & x=5 & q=6'],
]




root.mainloop()