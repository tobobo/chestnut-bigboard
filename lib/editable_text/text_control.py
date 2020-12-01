import os, time, curses, logging
from pynput import keyboard
from curses import wrapper

class TextControl:
  def __init__(self, text_display):
    self.text_display = text_display
    
  def mount(self):
    this_module = self
    def on_press(key):
      this_module.on_press(key)
    self.listener = keyboard.Listener(on_press=on_press)
    self.listener.start()
    
  def on_press(self, key):
    try:
      # self.text += key.char
      self.text_display.insert(key.char)
    except AttributeError: 
      if key == keyboard.Key.backspace:
        self.text_display.backspace()
      if key == keyboard.Key.space:
        self.text_display.insert(" ")
