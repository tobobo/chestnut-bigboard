from .text_display import TextDisplay
from .text_control import TextControl

class EditableText:
  def __init__(self, width, height, text):
    self.text_display = TextDisplay(width, height, text)
    self.text_control = TextControl(self.text_display)
    
  def mount(self):
    self.text_control.mount()
  
  def get_rows(self):
    return self.text_display.get_rows()
  
  def get_cursor_position(self):
    return self.text_display.get_cursor_position()
