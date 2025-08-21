import FreeSimpleGUI as sg

yash = sg.Text("Enter a todo")
label = sg.InputText(tooltip="Enter todo", key="todo")
buttons = sg.Button("ADD")

window = sg.Window("MY first app", layout=[[yash], [label, buttons]], font=("Helvetica", 20))

while True:
    event, value = window.read()

    # Break condition
    if event == sg.WIN_CLOSED:   # If user closes window
        break
    if event == "ADD":           # If ADD button pressed
        print("Todo:", value["todo"])
        window['todo'].update("")
        


# Close window OUTSIDE loop
window.close()
