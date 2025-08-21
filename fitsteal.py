import functions as fn
import FreeSimpleGUI as sg
label=sg.Text("Enter the TO-DO")
user_input=sg.Input(tooltip="enter todo",key="todo")
buttons=sg.Button("ADD")
list_box=sg.Listbox(values=fn.get_todos(),size=[45,10],enable_events=True,key='asur')
button2=sg.Button("Edit")


windows=sg.Window("TO_DO APP",layout=[[label],[user_input,buttons],[list_box,button2]],font=("Helvetica",16))
while True:

    event,values=windows.read()
    print(event)
    print(values)
    print(values['asur'][0])
    # print(event['asur'])
    match event:
        
        case 'ADD':
            if(values):
                myTodos=fn.get_todos()
                values['todo']=values['todo'] + '\n'
                myTodos.append(values["todo"])
                fn.write_todos(myTodos)
                windows['todo'].update('')
                windows['asur'].update(values=myTodos)
        case 'Edit':
            todos_to_edit=values['asur'][0]
            new_to_edit=values["todo"] + '\n'
            mylist=fn.get_todos()
            index=mylist.index(todos_to_edit) 
            mylist[index]=new_to_edit 
            fn.write_todos(mylist)
            windows['asur'].update(values=mylist)

        case 'asur':
            windows['todo'].update(value=values["asur"][0])    


        case sg.WIN_CLOSED:
            break        

    # print(event)
    # print(values)
    # windows['todo'].update('')
    # if event==sg.WIN_CLOSED:
    #     break
windows.close()

