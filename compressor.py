import FreeSimpleGUI as sg
import zipcreator as zp
label1=sg.Text("Select the files to compress")
input1=sg.Input()
choose_button1=sg.FilesBrowse("Choose",key='files')
label2=sg.Text("Select the destination folder")
input2=sg.Input()
choose_button2=sg.FolderBrowse("Choose",key='folder')
comperessor=sg.Button("Compress")

window=sg.Window("File Compressor",layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[comperessor]])
while True:
    event,value=window.read()
    if event==sg.WIN_CLOSED:
        break
    print(event)
    print(value)

    
    files_name=value['files'].split(';')
    folder_name=value['folder']
   
    zp.make_compress(files_name,folder_name)
    if event=='Compress':
        window['files'].update('')
        window['folder'].update('')
    


   


window.close()