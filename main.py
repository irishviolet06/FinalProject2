from tkinter import *
from gui import *
import csv

def main():
    window = Tk()
    window.title('Final Project 2')
    window.geometry('565x391')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()