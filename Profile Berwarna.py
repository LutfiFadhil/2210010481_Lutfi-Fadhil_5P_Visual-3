import PySimpleGUI as sg
sg.theme("Blackwhite4")
sg.theme_text_color("#00ffCC")
Window = sg.Window('Profile Berwarna', 
    [[sg.Text('NPM :2210010481'),],
        [sg.Text('Nama :Luthfi Fadhil')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200)).read(close=True)
event, values=Window.read()
Window.close()