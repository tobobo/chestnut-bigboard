import os, time, curses, logging
from pynput import keyboard
from curses import wrapper

logging.basicConfig(filename='output.log', level=logging.DEBUG)

def split_word(word, pos):
  return (word[:pos], word[pos:])
  

class EditableText:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.text = "WELCOME TO THE CHESTNUT BIG BOARD"
    
  def mount(self):
    this_module = self
    def on_press(key):
      this_module.on_press(key)
    self.listener = keyboard.Listener(on_press=on_press)
    self.listener.start()
    
  def on_press(self, key):
    try:
      # self.text += key.char
      self.append_text_if_possible(key.char)
    except AttributeError: 
      if key == keyboard.Key.backspace:
        self.text = self.text[:-1]
      if key == keyboard.Key.space:
        # self.text += " "
        self.append_text_if_possible(" ")
        
  def append_text_if_possible(self, char):
    cursor_row, _ = self.get_cursor_position()
    if cursor_row < self.height:
      self.text += char

  def get_cursor_position(self):
    rows = self.rows()
    last_row_index = len(rows) - 1
    last_col_index = len(rows[-1]) - 1
    if last_col_index >= self.width - 1:
      return [last_row_index + 1, 0]
    else:
      return (len(self.rows()) - 1, min(len(self.rows()[-1]), self.width))
  
  def rows(self):
    words = self.text.split(" ")
    rows = []
    word_index = 0
    row_index = 0

    while word_index < len(words) and row_index < self.height:
      word = words[word_index]
      
      if row_index == len(rows):
        prefix, suffix = split_word(word, self.width)
        rows.append(prefix)
        if len(suffix):
          words.insert(word_index + 1, suffix)
        word_index += 1
      elif len(rows[row_index]) + len(word) + 1 < self.width:
        rows[row_index] += " " + word
        word_index += 1
      elif row_index == self.height - 1:
        prefix, suffix = split_word(word, self.width - len(rows[row_index]) - 1)
        rows[row_index] += " " + prefix
        row_index += 1
      else:
        row_index += 1

    return rows


if __name__ == "__main__":
  logging.debug('started')
  width = 20
  height = 5
  text = EditableText(width=width, height=height)
  
  text.mount()

  def setup_screen(stdscr):
    stdscr.keypad(False)
    curses.curs_set(0)
    win = curses.newwin(height + 1, width, 0, 0)
    while 1:
      win.erase()
      for i, row in enumerate(text.rows()):
        # logging.debug('printng at ' + repr(i) + ' ' + repr(0) + ' ' + row)
        win.addstr(i, 0, row)
      cursor_row, cursor_column = text.get_cursor_position()
      if (cursor_row < height):
        win.addstr(cursor_row, cursor_column, "█")
      win.refresh()
      time.sleep(0.01)

  wrapper(setup_screen)
