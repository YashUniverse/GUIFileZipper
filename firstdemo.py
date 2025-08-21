import FreeSimpleGUI as sg
yash=sg.Text("Enter a todo")
label=sg.InputText(tooltip="Enter todo",key="todo")

buttons=sg.Button("ADD")
window=sg.Window("MY fist app",layout=[[yash],[label,buttons]],font=("Helvitica",20))
# window=sg.Window("MY fist app",layout=[yash])//only you pass iterables like list
while True:
    event,value=window.read()

    print(event)
    print(value)
window.close()

