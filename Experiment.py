import FreeSimpleGUI as sg
label=sg.Text("Enter a Nnumber")
input_box=sg.InputText(tooltip="Enter the Number",key="number")

windows=sg.Window("Emergency APP",layout=[[label],[input_box]],font=("Aerial",16))

windows.read()

print(windows["number"])
windows.close()

