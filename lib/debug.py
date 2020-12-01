import curses, logging, time
from editable_text import EditableText

logging.basicConfig(filename='output.log', level=logging.DEBUG)

if __name__ == "__main__":
  logging.debug('started')
  width = 20
  height = 5
  text = "WELCOME TO THA BIG BOARD"
  text = EditableText(width=width, height=height, text=text)
  
  text.mount()

  def setup_screen(stdscr):
    stdscr.keypad(False)
    curses.curs_set(0)
    win = curses.newwin(height + 1, width, 0, 0)
    while 1:
      win.erase()
      for i, row in enumerate(text.get_rows()):
        # logging.debug('printng at ' + repr(i) + ' ' + repr(0) + ' ' + row)
        win.addstr(i, 0, row)
      cursor_row, cursor_column = text.get_cursor_position()
      if (cursor_row < height):
        win.addstr(cursor_row, cursor_column, "█")
      win.refresh()
      time.sleep(0.01)

  curses.wrapper(setup_screen)
