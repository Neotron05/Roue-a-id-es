# imports
import json, JSONS, GUI
from tkinter import *
from tkinter import ttk

url = 'things.json'
objects = JSONS.read(url)
GUI.window()
