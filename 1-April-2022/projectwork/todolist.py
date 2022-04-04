# Todo list with python

todos = []
is_quit = False
show = True

while is_quit == False:
    index = - 1
    if show == True:
        print(f'type - help - To see commands ')
        print(f'type - st - To show todos ')
        print(f'type - ct - To create todos ')
        print(f'type - rt - To remove todos ')
        print(f'type - q - To quit the todo ')
        print('')
        show = False
    res = input('What you want to do : ')

    if res == 'ct':
        todo = str(input('Enter a the name of the todo : '))
        print('Todo added')
        todos.append(todo)

    elif res == 'st':
        if len(todos) <= 0:
            print('No todos added')
        else:
            for t in todos:
                print(f'- {t}')
                print('-----------------------------------------------------')

    elif res == 'rt':
        if len(todos) <= 0:
            print('No todos added')
        else:
            for t in todos:
                print(f'- {t}')
                print('-----------------------------------------------------')
            rTodo = input('Enter the name of the todo to delete : ')
            try:
                tt = todos.remove(rTodo)
                print('Todo removed')
            except:
                print('No todo found with that name')

    elif res == 'q':
        is_quit = True
        break

    elif res == 'help':
        print(f'type - help - To see commands ')
        print(f'type - st - To show todos ')
        print(f'type - ct - To create todos ')
        print(f'type - rt - To remove todos ')
        print(f'type - q - To quit the todo ')

    else:
        print('Please enter a valid value')
