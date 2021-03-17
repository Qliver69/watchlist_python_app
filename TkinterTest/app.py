import tkinter as tk
import os
from selenium_script import main


class App:

    def __init__(self):
        self.anime_list = []
        self.colorBG = '#c5c5c5'
        self.colorBTN = '#7f7f7f'

        self.window = tk.Tk()

        self.frm_watchList = tk.Frame(bg=self.colorBG)  # right frame w/ list and right button
        self.frm_body = tk.Frame(bg=self.colorBG)  # left frame w/ name and info about anime
        self.frm_btnWL = tk.Frame(self.frm_watchList, bg=self.colorBG)  # frame right down corner w/ button
        self.frm_label_name = tk.Frame(self.frm_body, bg=self.colorBG)  # frame on top left w/ anime's name
        self.frm_addAnime = tk.Frame(self.frm_body, bg=self.colorBG)  # frame left down corner for adding button
        self.frm_btnBD = tk.Frame(self.frm_body, height=300, width=3 * 160, bg=self.colorBG)  # frame middle left
        self.frm_season = tk.Frame(self.frm_btnBD,  bg=self.colorBG)  # frame w/ season counter
        self.frm_episode = tk.Frame(self.frm_btnBD, bg=self.colorBG)  # frame w/ episode counter
        self.frm_finishCheck = tk.Frame(self.frm_btnBD, height=150, width=1.5 * 160, bg=self.colorBG,
                                        relief=tk.GROOVE, bd=5)  # frame w/ finished checkbox

        self.lbl_titleWL = tk.Label(self.frm_watchList, text='WatchList :', bg=self.colorBG, font=22)
        self.lbl_animeName = tk.Label(self.frm_label_name, text="Anime's Name",
                                      bg=self.colorBG, font=('arial', 25), width=15, anchor=tk.CENTER)
        self.lbl_season = tk.Label(self.frm_season, text='Season :', bg=self.colorBG, font=('arial', 22), width=9)
        self.lbl_episode = tk.Label(self.frm_episode, text='Episode :', bg=self.colorBG, font=('arial', 22), width=9)
        # label printing the current season
        self.lbl_counter1 = tk.Label(self.frm_season, text='0', bg=self.colorBG, font=('arial', 22))
        # label printing the current episode
        self.lbl_counter2 = tk.Label(self.frm_episode, text='0', bg=self.colorBG, font=('arial', 22))

        self.listboxWL = tk.Listbox(self.frm_watchList, height=25, width=50)  # listbox to select an anime
        self.scrollbarWL = tk.Scrollbar(self.frm_watchList)
        # checkbox to mark finished an anime
        self.ckbtn_finish = tk.Checkbutton(self.frm_btnBD, text='Finished', bg=self.colorBG,
                                           command=self.checkbox_click,
                                           font=('arial', 22), activebackground=self.colorBG)

        self.btn_finished = tk.Button(self.frm_btnWL, text='Finished', activebackground=self.colorBG,
                                      bg=self.colorBTN, font=22, width=12, command=self.set_finished_anime)
        self.btn_inprogress = tk.Button(self.frm_btnWL, font=22, width=12, activebackground=self.colorBG,
                                        text='In progress', bg=self.colorBTN, command=self.set_inprogress_anime)
        self.btn_homeWL = tk.Button(self.frm_btnWL, text='Home', bg=self.colorBTN,
                                    command=lambda: [f() for f in [self.save, self.set_anime_list]],
                                    font=22, activebackground=self.colorBG)
        self.btn_addAnime = tk.Button(self.frm_addAnime, text='Add an anime to the list', bg=self.colorBTN,
                                      font=22, activebackground=self.colorBG, height=2, width=50)
        self.btn_downloadAnime = tk.Button(self.frm_addAnime, text='Lunch download script with voiranime.com links',
                                           bg=self.colorBTN, font=22, activebackground=self.colorBG, height=2, width=50,
                                           command=main)
        self.btn_decrease1 = tk.Button(self.frm_season, text='-', bg=self.colorBG, font=('arial', 22),
                                       command=self.decrease1)
        self.btn_decrease2 = tk.Button(self.frm_episode, text='-', bg=self.colorBG, font=('arial', 22),
                                       command=self.decrease2)
        self.btn_increase1 = tk.Button(self.frm_season, text='+', bg=self.colorBG, font=('arial', 22),
                                       command=self.increase1)
        self.btn_increase2 = tk.Button(self.frm_episode, text='+', bg=self.colorBG, font=('arial', 22),
                                       command=self.increase2)
        self.btn_delete = tk.Button(self.frm_btnBD, text='Delete', width=9, bg=self.colorBG,
                                    activebackground=self.colorBG)
        self.btn_save = tk.Button(self.frm_btnBD, text='Save before quit', width=9, bg=self.colorBG,
                                  activebackground=self.colorBG, command=self.save)

    def config_window(self):
        self.window.geometry('815x510')
        self.window.minsize(815, 510)
        self.window.maxsize(815, 510)  # (1222, 765)
        self.window.config(bg=self.colorBG)

    def config_widget(self):
        self.listboxWL.config(yscrollcommand=self.scrollbarWL.set)
        self.scrollbarWL.config(command=self.listboxWL.yview)

    def pack_frame(self):
        self.frm_episode.grid(row=1, column=0, sticky='nw', padx=20)
        self.frm_season.grid(row=0, column=0, sticky='nw', padx=20)
        self.frm_addAnime.grid(row=2, column=0, sticky='nw', pady=90)
        self.frm_btnBD.grid(row=1, column=0, sticky='nw')
        self.frm_label_name.grid(row=0, column=0, sticky='nw')
        self.frm_btnWL.grid(row=2, column=0, sticky='nw', pady=10)
        self.frm_body.grid(row=0, column=0, sticky='nw')
        self.frm_watchList.grid(row=0, column=1, sticky='nw')

    def pack_label(self):
        self.lbl_counter2.grid(row=1)
        self.lbl_counter1.grid(row=1)
        self.lbl_titleWL.grid(row=0, column=0, sticky='nw', pady=5)
        self.lbl_animeName.pack(fill=tk.BOTH, pady=10, padx=10)
        self.lbl_season.grid(row=0, column=0, sticky='nw', pady=10)
        self.lbl_episode.grid(row=0, column=0, sticky='nw', pady=10)

    def pack_otherwidget(self):
        self.listboxWL.grid(row=1, column=0, sticky='w', pady=5)
        self.scrollbarWL.grid(row=1, column=1, sticky='nwse', pady=5)
        self.ckbtn_finish.grid(row=0, column=1, sticky='nsew', padx=10)

    def pack_button(self):
        self.btn_save.grid(row=1, column=1, sticky='sew')
        self.btn_delete.grid(row=1, column=1, sticky='ew')
        self.btn_increase2.grid(row=1, sticky='e')
        self.btn_increase1.grid(row=1, sticky='e')
        self.btn_decrease2.grid(row=1, sticky='w')
        self.btn_decrease1.grid(row=1, sticky='w')
        self.btn_addAnime.grid(row=0, column=0, pady=5, padx=5)
        self.btn_downloadAnime.grid(row=1, column=0)
        self.btn_finished.grid(row=0, column=0, pady=10)
        self.btn_inprogress.grid(row=0, column=1)
        self.btn_homeWL.grid(row=0, column=2)

    def bind_widget(self):
        self.listboxWL.bind('<<ListboxSelect>>', self.set_body)

# initiate anime_list and print all the anime's name from fill to list
    def set_anime_list(self):
        self.listboxWL.delete(0, tk.END)
        # line: <anime's name>, <season>, <episode>, <finished(1/0)>
        file = open('anime112.txt', 'r')
        self.anime_list = file.readlines()
        # separate informations on one line
        for i in range(len(self.anime_list)):
            self.anime_list[i] = self.anime_list[i].split(', ')
            self.anime_list[i][3] = self.anime_list[i][3].replace('\n', '')
            # insert anime not finished
            if self.anime_list[i][3] == '0' and self.anime_list[i][2] == '0':
                self.ckbtn_finish.deselect()
                self.listboxWL.insert(tk.END, self.anime_list[i][0])
        file.close()

    def set_finished_anime(self):
        self.save()
        self.listboxWL.delete(0, tk.END)
        for i in range(len(self.anime_list)):
            # insert anime finished
            if self.anime_list[i][3] == '1':
                self.ckbtn_finish.select()
                self.listboxWL.insert(tk.END, self.anime_list[i][0])

    def set_inprogress_anime(self):
        self.save()
        self.listboxWL.delete(0, tk.END)
        for i in range(len(self.anime_list)):
            # insert anime in progress
            if self.anime_list[i][3] == '0' and self.anime_list[i][2] != '0':
                self.ckbtn_finish.deselect()
                self.listboxWL.insert(tk.END, self.anime_list[i][0])

# add 1 to season counter
    def increase1(self):
        value = int(self.lbl_counter1['text'])
        self.lbl_counter1['text'] = f"{value + 1}"
        self.anime_list[self.find_index()][1] = self.lbl_counter1['text']

# add 1 to episode counter
    def increase2(self):
        value = int(self.lbl_counter2['text'])
        self.lbl_counter2['text'] = f"{value + 1}"
        self.anime_list[self.find_index()][2] = self.lbl_counter2['text']

# remove 1 to season counter
    def decrease1(self):
        value = int(self.lbl_counter1['text'])
        self.lbl_counter1['text'] = f"{value - 1}"
        self.anime_list[self.find_index()][1] = self.lbl_counter1['text']

# remove 1 to episode counter
    def decrease2(self):
        value = int(self.lbl_counter2['text'])
        self.lbl_counter2['text'] = f"{value - 1}"
        self.anime_list[self.find_index()][2] = self.lbl_counter2['text']

# set all left side of the app
    def set_body(self, evt):
        # get the name selected
        name = self.listboxWL.get(self.listboxWL.curselection())
        # change the name on the left
        self.lbl_animeName['text'] = f'{name}'
        # change the value of season and episode on the left
        self.lbl_counter1['text'] = self.anime_list[self.find_index()][1]
        self.lbl_counter2['text'] = self.anime_list[self.find_index()][2]

    def find_index(self):
        x = 0
        while self.listboxWL.get(self.listboxWL.curselection()) != self.anime_list[x][0]:
            x += 1
        return x

    def save(self):
        os.remove('anime112.txt')
        file = open('anime112.txt', 'w+')
        for i in range(len(self.anime_list)):
            for j in range(3):
                self.anime_list[i][0] = self.anime_list[i][0]+', '+self.anime_list[i][j+1]
            self.anime_list[i] = self.anime_list[i][0] + '\n'
            file.write(self.anime_list[i])
        file.close()
        self.set_anime_list()

    def checkbox_click(self):
        if self.anime_list == '0':
            self.anime_list[self.find_index()][3] = '1'
        else:
            self.anime_list[self.find_index()][3] = '0'
        print(self.anime_list[self.find_index()][3])

# problem of the night : the checkbox isn't responding well to transform an anime in finished anime
