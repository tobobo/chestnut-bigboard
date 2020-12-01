from pynput import keyboard

def split_word(word, pos):
  return (word[:pos], word[pos:])

class TextDisplay:
  def __init__(self, width, height, text):
    self.width = width
    self.height = height
    self.text = text
    
  def insert(self, char):
    cursor_row, _ = self.get_cursor_position()
    if cursor_row < self.height:
      self.text += char
        
  def backspace(self):
    self.text = self.text[:-1]

  def get_cursor_position(self):
    rows = self.get_rows()
    last_row_index = len(rows) - 1
    last_col_index = len(rows[-1]) - 1
    if last_col_index >= self.width - 1:
      return [last_row_index + 1, 0]
    else:
      return (len(rows) - 1, min(len(rows[-1]), self.width))
  
  def get_rows(self):
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
