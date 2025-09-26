def load_his():
    # Load tasks from file and return as list of task (id, stat, text):
    tasks = []
    try :
        with open('data.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line :
                    stat = line[:3]
                    text = line[4:]
                    tasks.append((stat, text))
    except FileNotFoundError:
        pass
    return tasks

def list_todo():
    tasks = load_his()
    if not tasks :
        print("No tasks to show!")
        return
    for idx, (stat, text) in enumerate(tasks, 1):
        print(f"{idx}. {stat} {text}")

def add_todo() :
    print('Enter your data to append in todo')
    tasks = load_his()
    text = input('>')
    text = str(text)
    stat = '[ ]'
    tasks.append((stat, text))
    save_todo(tasks)


def save_todo(tasks):
    with open ('data.txt', 'w') as f:
        for stat, text in tasks:
            f.write(f'{stat} {text}\n')

def del_todo():
    tasks = load_his()
    list_todo()
    try:
        print('Enter list number that want to delete')
        del_num = int(input('>'))
        if 1 <= del_num <= len(tasks):
            tasks.pop(del_num-1)
            save_todo(tasks)
            print('Deleted Todo')
        else :
            print('Number not found')
    except ValueError:
        print('Please Enter Valid Number')


def mark_todo():
    tasks = load_his()
    list_todo()
    try:
        id = int(input('Enter Task id to mark done >'))
        for i, (stat, text) in enumerate(tasks, 1):
            if 1<= id <= len(tasks):
                stat, text = tasks[id-1]
                if stat == "[ ]":
                    tasks[id-1] = ("[x]", text)
                    save_todo(tasks)
                    print(f'Marked Task no {id} done')
                    return
                else :
                    print('Task already Done!')
                    return
            #print when not found task!
            print('Task number not found')
    except ValueError:
        print('Please enter a valid id')

def main():
    while True:
        print('CLI-TODO')
        print('1. View Todo')
        print('2. Add Todo')
        print('3. Mark Todo')
        print('4. Delete Todo')
        print('5. Exit')
        print('Select by enter only number')
        choice = input('>')
        choice = str(choice)

        if choice == "1" :
            list_todo()
        elif choice == "2" :
            add_todo()
        elif choice == "3" :
            mark_todo()
        elif choice == "4" :
            del_todo()
        elif choice == "5" :
            print('Bye! Exit.. Todo')
            break
        else :
            print('Invalid input enter on number')

if __name__ == "__main__":
    main()

    
    
