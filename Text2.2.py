import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
Window = sg.Window(title="Text2",
                   layout= [[sg.Text("TEKNOLOGI INFORMASI", size=(25,1), justification="center")],
                            [sg.Text("TEKNOLOGI INFORMASI", size=(25,1), justification="left")],
                            [sg.Text("TEKNOLOGI INFORMASI", size=(25,1), justification="right")],
                            [sg.Text(("TEKNOLOGI INFORMASI "+" ")* 2,size=(25,2),justification="cnter")],
                            [sg.Text("UNISKA MAB BANJARMASIN",text_color="#FFCC00")]],
                            size=(400,250),
                            font=("times", 18))
Window()
Window.colose()