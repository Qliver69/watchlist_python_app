import app_main

app = app_main.App()

# configuration of the window and the widget
app.config_window()
app.config_widget()

# pack all the widget
app.pack_label()
app.pack_button()
app.pack_otherwidget()
app.pack_frame()

# binding widget to function/method
app.bind_widget()

# first initialisaton of the listbox and anime_list
app.set_anime_list()

app.window.mainloop()
