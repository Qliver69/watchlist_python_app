import tkinter as tk


class AddingWdw:

    def __init__(self):
        self.colorBG = '#c5c5c5'
        self.colorBTN = '#7f7f7f'

        self.window2 = tk.Tk()

        self.title = tk.Label(self.window2, text='Add an anime :', bg=self.colorBG, font=('arial', 20), width=30)
        self.entry = tk.Entry(self.window2, text='Name', font=('arial', 18))

        self.frm_counter = tk.Frame(self.window2, bg=self.colorBG)
        self.frm_season = tk.Frame(self.frm_counter,  bg=self.colorBG)  # frame w/ season counter
        self.frm_episode = tk.Frame(self.frm_counter, bg=self.colorBG)  # frame w/ episode counter
        self.lbl_season = tk.Label(self.frm_season, text='Season :', bg=self.colorBG, font=('arial', 22), width=9)
        self.lbl_episode = tk.Label(self.frm_episode, text='Episode :', bg=self.colorBG, font=('arial', 22), width=9)

        # label printing the current season
        self.lbl_counter1 = tk.Label(self.frm_season, text='0', bg=self.colorBG, font=('arial', 22))
        # label printing the current episode
        self.lbl_counter2 = tk.Label(self.frm_episode, text='0', bg=self.colorBG, font=('arial', 22))

        self.btn_decrease1 = tk.Button(self.frm_season, text='-', bg=self.colorBG, font=('arial', 22),
                                       command=self.decrease1)
        self.btn_decrease2 = tk.Button(self.frm_episode, text='-', bg=self.colorBG, font=('arial', 22),
                                       command=self.decrease2)
        self.btn_increase1 = tk.Button(self.frm_season, text='+', bg=self.colorBG, font=('arial', 22),
                                       command=self.increase1)
        self.btn_increase2 = tk.Button(self.frm_episode, text='+', bg=self.colorBG, font=('arial', 22),
                                       command=self.increase2)

        self.ckbtn_finish = tk.Checkbutton(self.frm_btnBD, text='Finished', bg=self.colorBG,
                                           command=self.checkbox_click,
                                           font=('arial', 22), activebackground=self.colorBG)

    def config_window(self):
        self.window2.geometry('480x510')
        # self.window2.minsize(480, 510)
        # self.window2.maxsize(480, 510)
        self.window2.config(bg=self.colorBG)
        self.window2.title('WatchList TC')
        self.window2.iconbitmap('data\\file.ico')

    def pack_elements(self):
        self.title.grid(row=0, column=0, sticky='ew', pady=15)
        self.entry.grid(row=1, column=0, sticky='ew', padx=30, pady=15)

        self.frm_counter.grid(row=2, column=0, sticky='nwe')
        self.frm_season.grid(row=0, column=0, sticky='nw ', padx=35)
        self.frm_episode.grid(row=0, column=1, sticky='ne', padx=35)

        self.lbl_season.grid(row=0, column=0, sticky='nw')
        self.lbl_episode.grid(row=0, column=0, sticky='nw')

        self.btn_decrease1.grid(row=1, sticky='w')
        self.lbl_counter1.grid(row=1, sticky='we')
        self.btn_increase1.grid(row=1, sticky='e')

        self.btn_decrease2.grid(row=1, sticky='w')
        self.lbl_counter2.grid(row=1, sticky='we')
        self.btn_increase2.grid(row=1, sticky='e')

# add 1 to season counter
    def increase1(self):
        value = int(self.lbl_counter1['text'])
        self.lbl_counter1['text'] = f"{value + 1}"

# add 1 to episode counter
    def increase2(self):
        value = int(self.lbl_counter2['text'])
        self.lbl_counter2['text'] = f"{value + 1}"

# remove 1 to season counter
    def decrease1(self):
        value = int(self.lbl_counter1['text'])
        self.lbl_counter1['text'] = f"{value - 1}"

# remove 1 to episode counter
    def decrease2(self):
        value = int(self.lbl_counter2['text'])
        self.lbl_counter2['text'] = f"{value - 1}"


wdw = AddingWdw()
wdw.pack_elements()
wdw.config_window()
wdw.window2.mainloop()
