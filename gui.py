from tkinter import *
import csv

class Gui:
    """
    method to set up Voting App GUI layout
    """
    def __init__(self, window):
        self.window = window

        self.frame_title = Frame(self.window)
        self.label_title = Label(self.window, text='Welcome to the Voting Booth!')
        self.label_title.pack()
        self.frame_title.pack()

        self.frame_state = Frame(self.window)
        self.label_state = Label(self.window, text='Please state your name and age')
        self.label_state.pack()
        self.frame_state.pack()

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.input_name = Entry(self.frame_name)
        self.label_name.pack(side='left')
        self.input_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', padx=10, pady=10)

        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.input_age = Entry(self.frame_age)
        self.label_age.pack(side='left')
        self.input_age.pack(padx=5, side='left')
        self.frame_age.pack(anchor='w', padx=22, pady=10)

        self.frame_text = Frame(self.window)
        self.label_text = Label(self.window, text='Hit enter when finished')
        self.label_text.pack()
        self.frame_text.pack()

        self.frame_enter = Frame(self.window)
        self.button_enter = Button(text='Enter', command=self.submit)
        self.button_enter.pack(pady=10)
        self.button_enter.pack()

    def submit(self):
        """
        method to check for correct values such as age input or name input and add candidate buttons
        """
        name = self.input_name.get()
        age = self.input_age.get()
        if name == '':
            self.label_text.config(text='Please state your name', bg='red')
            self.input_name.delete(0, END)
            self.input_age.delete(0,END)
        elif not age.isdigit():
            self.input_name.delete(0, END)
            self.input_age.delete(0, END)
            self.label_text.config(text='Error: Please enter an age', bg='red')
        elif int(age) < 18:
            self.input_name.delete(0, END)
            self.input_age.delete(0, END)
            self.label_text.config(text='Error: You must be at least 18 to vote', bg='red')
        else:
            self.frame_candidate_text = Frame(self.window)
            self.label_candidate_text = Label(self.window, text='Vote for your candidate')
            self.label_candidate_text.pack()
            self.frame_candidate_text.pack()

            self.frame_candidates = Frame(self.window)
            self.label_candidates = Label(self.frame_candidates, text='Candidates')
            self.frame_ans = IntVar()
            self.frame_ans.set(1)
            self.radio_john = Radiobutton(self.frame_candidates, text='John', value=1)
            self.radio_jane = Radiobutton(self.frame_candidates, text='Jane', value=2)
            self.radio_jill = Radiobutton(self.frame_candidates, text='Jill', value=3)
            self.label_candidates.pack(side='left')
            self.radio_john.pack(side='left', padx=10, pady=10)
            self.radio_jane.pack(side='left', padx=10, pady=10)
            self.radio_jill.pack(side='left', padx=10, pady=10)
            self.frame_candidates.pack()

            self.frame_submit = Frame(self.window)
            self.button_submit = Button(text='Submit', command=self.submit2)
            self.button_submit.pack(pady=10)
            self.button_submit.pack()
    def submit2(self):
        """
        method to send candidates information to file
        """
        name = self.input_name.get()
        age = self.input_age.get()
        candidates = self.frame_ans.get()
        if candidates == 1:
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Data submitted! Thank you and have a nice day!')
            self.label_saved.pack()
            self.frame_saved.pack()
            self.input_name.delete(0,END)
            self.input_age.delete(0,END)

            csv_file = 'voting.csv'
            with open(csv_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Name', 'Age', 'Candidates'])
                writer.writerow([name, age, 'John'])

        elif candidates == 2:
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Data submitted! Thank you and have a nice day!')
            self.label_saved.pack()
            self.frame_saved.pack()
            self.input_name.delete(0, END)
            self.input_age.delete(0, END)

            csv_file = 'voting.csv'
            with open(csv_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['name', 'age', 'candidates'])
                writer.writerow([name, age, 'Jane'])

        elif candidates == 3:
            self.frame_saved = Frame(self.window)
            self.label_saved = Label(self.window, text='Data submitted! Thank you and have a nice day!')
            self.label_saved.pack()
            self.frame_saved.pack()
            self.input_name.delete(0, END)
            self.input_age.delete(0, END)

            csv_file = 'voting.csv'
            with open(csv_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Name', 'Age', 'Candidates'])
                writer.writerow([name, age, 'Jill'])