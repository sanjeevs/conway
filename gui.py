from tkinter import *

class Gui:
  def __init__(self, nrows, ncols, width):
    self.tk = self.create_window()
    self.nrows = nrows
    self.ncols = ncols
    self.width = width
    self.canvas = self.create_canvas()
    self.arr = [[self.create_square(i, j) for j in range(ncols)] for i in range(nrows)]

  def create_window(self):
    tk = Tk()
    tk.title("GameOfLife")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    return tk

  def create_canvas(self):
    size = self.nrows * self.width
    canvas = Canvas(self.tk, width=size, height=size, bd=0, highlightthickness=0)
    canvas.pack()
    self.tk.update()
    return canvas

  def create_square(self, row, col):
    x1 = col * self.width 
    y1 = row * self.width 
    x2 = x1 + self.width
    y2 = y1 + self.width 
    return self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.off_color())

  def on_color(self):
    return "red"

  def off_color(self):
    return "blue"

  def set_on(self, row, col):
    self.canvas.itemconfig(self.arr[row][col], fill=self.on_color())

  def set_off(self, row, col):
    self.canvas.itemconfig(self.arr[row][col], fill=self.off_color())

  def update(self, board):
    for row in range(self.nrows):
      for col in range(self.ncols):
        if(board.is_alive(row, col)):
          self.set_on(row, col)
        else:
          self.set_off(row, col)
    self.tk.update_idletasks()
    self.tk.update()
