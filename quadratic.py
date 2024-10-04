import PySimpleGUI as sg
import random
#!/usr/bin/python3

layout = [[sg.Text("Practice factorization 😊")],
          [sg.Multiline(size = (60, 2), key = "output")],
          [sg.Button("generate"), sg.Button("answer"), sg.Button("close"), sg.OptionMenu(["Difficulty 1", "Difficulty 2", "Difficulty 3(work in progress)"], default_value = "Difficulty 3(work in progress", key = "difficulty")]]

window = sg.Window("quadratic demo", layout)

def testerFunction(difficultyLevel):
        global a
        global b
        if difficultyLevel == 1:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            window["output"].update("x\u00b2 + "+str(a+b)+"x + "+str(a*b))
        elif difficultyLevel == 2:
            if random.randint(0,1) == 0:
                a = -random.randint(1, 9)
                b = random.randint(1, 9)
                if (a+b) > 0:
                    window["output"].update("x\u00b2 + "+str(a+b)+"x "+str(a*b))
                elif a+b == 0:
                    window["output"].update("x\u00b2 + "+str(a*b))
                elif a+b < 0:
                    window["output"].update("x\u00b2 "+str(a+b)+"x "+str(a*b))
            else:
                a = -random.randint(1, 9)
                b = -random.randint(1, 9)
                window["output"].update("x\u00b2 "+str(a+b)+"x + "+str(a*b))
     
def answerFunction():
    if a > 0 and b < 0:
        window["output"].update(values["output"] + "\n(x + " +str(a)+")(x "+str(b)+")")
    elif a < 0 and b > 0:
        window["output"].update(values["output"] + "\n(x " +str(a)+")(x + "+str(b)+")")
    elif a < 0 and b < 0:
        window["output"].update(values["output"] + "\n(x " +str(a)+")(x "+str(b)+")")
    elif a > 0 and b > 0:
        window["output"].update(values["output"] + "\n(x + " +str(a)+")(x + "+str(b)+")")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "close":
        break
    if event == "generate" :
        if values["difficulty"] == "Difficulty 1":
             testerFunction(1)
        elif values["difficulty"] == "Difficulty 2":
             testerFunction(2)
        elif values["difficulty"] == "Difficulty 3":
             testerFunction(3)
    if event == "answer":
        if values["difficulty"] != "Difficulty 3":
            answerFunction()
        
window.close()