# The Monty Project
The project below explains how to build a simple chat bot called Monty, adding functionality in small incremental steps.

## Monty 1

Write a Python program to read in one user command and repeat it back to the user. An example output is given below.

```
>>> Hello, my name is Monty
>>> What can I do for you?
foo
>>> Your command is: foo
>>> Bye!
```
## Monty 2
Extend **Monty 1** code to work as follows:

```
>>> Hello, my name is Monty
>>> What can I do for you?

list
>>> Nothing to list
>>> What can I do for you?

foo
>>> OOPS! Unknown command
>>> What can I do for you?

exit
>>> Are you sure? y/n
n
>>> What can I do for you?

exit
>>> Are you sure? y/n
y
>>> Bye!
```

## Monty 3
Restructure the **Monty 2 code** to fit the following structure, while keeping the behavior same as **Monty 2**.

```python
import sys


# ADD MISSING METHODS


def main():
    print_greeting()
    while True:
        command = read_command()
        execute_command(command)


main()
```

## Monty 4
Enhance the **Monty 3 code** to improve the functionality as per the sample output given below.

```
>>> Hello, my name is Monty
>>> What can I do for you?

list
>>> Nothing to list
>>> What can I do for you?

add read book
>>> What can I do for you?

list
>>> List of items:
     1. read book
>>> What can I do for you?

add return book
>>> What can I do for you?

list
>>> List of items:
     1. read book
     2. return book
>>> What can I do for you?

exit
>>> Are you sure? y/n
y
>>> Bye!
```

## Monty 5

Enhance the Monty 4 code in the following ways:

* Add a done command so that the user can mark a task as done. e.g., done 2 marks the task at index 2 as 'done'.
* Show appropriate error messages if the user gives an invalid index for the done command

A sample output is given below.

```
>>> Hello, my name is Monty
>>> What can I do for you?

add borrow book
>>> What can I do for you?

add read book
>>> What can I do for you?

add return book
>>> What can I do for you?

list
>>> List of items:
     [✗] 1. borrow book
     [✗] 2. read book
     [✗] 3. return book
>>> What can I do for you?

done 1
>>> What can I do for you?

list
>>> List of items:
     [✓] 1. borrow book
     [✗] 2. read book
     [✗] 3. return book
>>> What can I do for you?

done abc
>>> SORRY, I could not perform that command. Problem: abc is not a number
>>> What can I do for you?

done 5
>>> SORRY, I could not perform that command. Problem: No item at index 5
>>> What can I do for you?

done 0
>>> SORRY, I could not perform that command. Problem: Index must be greater than 0
>>> What can I do for you?

garbage
>>> SORRY, I could not perform that command. Problem: Command not recognized
>>> What can I do for you?

exit
>>> Are you sure? y/n
y
>>> Bye!
```


💡 Each task has two data values: the description and the 'done' status. You can use a list to hold these two data items. 
That means your list of tasks will be a list containing lists. Example:
```python
tasks = []
tasks.append(['read book', False])
print('Description of the first task:', tasks[0][0])

if tasks[0][1]:
    print('✓')
else:
    print('✗')
```
💡 You can use exceptions to identify and handle errors in the command.

```python
def main():
    print_greeting()
    while True:
        try:
            command = read_command()
            execute_command(command)
        except Exception as e:
            print('>>> SORRY, I could not perform that command. Problem:', e)
```
## Monty 6
Enhance the **Monty 5 code** in the following ways:

* Add a help command so that the user can view how to use the app.
* Improve the formatting of the text displayed to the user to make the user experience nicer.

A sample output is given below.
```
*******************************************************************************************
*  __          __  _                            _          __  __             _           *
*  \ \        / / | |                          | |        |  \/  |           | |          *
*   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | \  / | ___  _ __ | |_ _   _   *
*    \ \/  \/ / _ \ |/ __/ _ \| '_ ' _ \ / _ \ | __/ _ \  | |\/| |/ _ \| '_ \| __| | | |  *
*     \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_) | | | | |_| |_| |  *
*      \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\___/|_| |_|\__|\__, |  *
*                                                                                  __/ |  *
*                                                                                 |___/   *
******************************************************************************************* 

>>> What can I do for you?

help
>>> I'm glad you asked. Here it is:
==================================================
Monty can understand the following commands:

  add DESCRIPTION 
    Adds a task to the list
    Example: add read book
  done INDEX
    Marks the task at INDEX as 'done'
    Example: done 1
  exit
    Exits the application
  help_info
    Shows the help_info information
  list
    Lists the tasks in the list
-------------------------------------------------- 

>>> What can I do for you?

add read book
>>> Task added to the list
>>> What can I do for you?

add return book
>>> Task added to the list
>>> What can I do for you?

done 1
>>> Congrats on completing a task! :-)
>>> What can I do for you?

list
>>> Here is the list of tasks:
==================================================
STATUS | INDEX | DESCRIPTION                
--------------------------------------------------
  ✓    |   1   | read book                  
  ✗    |   2   | return book                
--------------------------------------------------
>>> What can I do for you?
```

## Monty 7
Enhance the **Monty 6 code** in the following ways:

* Monty saves tasks into a csv file.
* Add a delete command that can delete a task at a specific index.

A sample output is given below. Note the following:

* Monty is able to show at the very start the three tasks loaded from the file.
* When item 2 is deleted, the item previously at index 3 moves to position 2.

```
*******************************************************************************************
*  __          __  _                            _          __  __             _           *
*  \ \        / / | |                          | |        |  \/  |           | |          *
*   \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | \  / | ___  _ __ | |_ _   _   *
*    \ \/  \/ / _ \ |/ __/ _ \| '_ ' _ \ / _ \ | __/ _ \  | |\/| |/ _ \| '_ \| __| | | |  *
*     \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | | (_) | | | | |_| |_| |  *
*      \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  |_|\___/|_| |_|\__|\__, |  *
*                                                                                  __/ |  *
*                                                                                 |___/   *
******************************************************************************************* 

>>> What can I do for you?

list
>>> Here is the list of tasks:
==================================================
STATUS | INDEX | DESCRIPTION                
--------------------------------------------------
  ✓    |   1   | borrow book                
  ✗    |   2   | read book                  
  ✗    |   3   | return book                
--------------------------------------------------
>>> What can I do for you?

delete 2
>>> Task deleted from the list
>>> What can I do for you?

list
>>> Here is the list of tasks:
==================================================
STATUS | INDEX | DESCRIPTION                
--------------------------------------------------
  ✓    |   1   | borrow book                
  ✗    |   2   | return book                  
--------------------------------------------------
```
💡 here are some tips:

* The filename can be specified in the code. e.g.,
`DATA_FILE = monty_7.csv`
* The format of the file is up to you. Here is an example:

```
borrow book,done
read book,pending
return book,pending
```

* The program can load the tasks from the file at the beginning. It can save the data after each command. For example, as follows:

```python
items = []
DATA_FILE = 'monty7.csv'


def main():
     load_data(DATA_FILE) # load task data from the file
     print_greeting()
     while True:
         try:
             command = read_command()
             execute_command(command)
             save_data(DATA_FILE, items) # save all tasks in the file
         except Exception as e:
             print('>>> SORRY, I could not perform that command. Problem:', e)

main()
```

Given below are some more features you can consider adding at this point (it is optional to add them to Monty 7):

* Remove the the need for the user to confirm before exiting Monty. As data are saved to a file, such a confirmation is no 
longer necessary because an accidental exit will not cause any permanent damage.

```
>>> What can I do for you?

exit
>>> Bye!
```

* Add a `pending` command that can mark a task as pending (i.e., the opposite of the `done` command).

```
 >>> What can I do for you?
 
 list
 >>> Here is the list of tasks:
 ==================================================
 STATUS | INDEX | DESCRIPTION                
 --------------------------------------------------
   ✓    |   1   | borrow book                
   ✗    |   2   | read book                  
   ✗    |   3   | return book                
 --------------------------------------------------
 >>> What can I do for you?
 
 pending 1
 >>> OK, I have marked that item as pending
 >>> What can I do for you?
 
 list
 >>> Here is the list of tasks:
 ==================================================
 STATUS | INDEX | DESCRIPTION                
 --------------------------------------------------
   ✗    |   1   | borrow book                
   ✗    |   2   | read book                  
   ✗    |   3   | return book                
 --------------------------------------------------
 >>> What can I do for you?
```

* Make commands case insensitive and immune to extra leading/trailing spaces. For example, 
all these commands should work the same way.

```
add read book
ADD read book
Add read book
add    read book
    add read book
```

## Monty 8
Enhance the **Monty 7 code** to add support for keeping track of deadlines as well as regular todo tasks

Previous behavior:

* add buy book: adds a task buy book

Proposed change - replace the above command with the following two:

* todo read book: adds a todo task read book
* deadline return book by: May 3rd adds a deadline return book which is to be done by May 3d.
Note: by: is a keyword. Anything that comes after it is considered a description of the deadline.

A sample output is given below.
```
>>> What can I do for you?

list
>>> Here is the list of tasks:
============================================================
STATUS | INDEX | DESCRIPTION                 | DEADLINE
------------------------------------------------------------
  ✓    |   1   | borrow book                 | -
  ✗    |   2   | read book                   | -
  ✗    |   3   | return book                 | Monday
------------------------------------------------------------
>>> What can I do for you?

todo watch movie
>>> What can I do for you?

deadline submit assignment by: end of May
>>> What can I do for you?

list
>>> Here is the list of tasks:
============================================================
STATUS | INDEX | DESCRIPTION                 | DEADLINE
------------------------------------------------------------
  ✓    |   1   | borrow book                 | -
  ✗    |   2   | read book                   | -
  ✗    |   3   | return book                 | Monday
  ✗    |   4   | watch movie                 | -
  ✗    |   5   | submit assignment           | end of May
------------------------------------------------------------
>>> What can I do for you?
```

## Monty 9
Enhance the **Monty 8 code** to use classes `ToDo` and `Deadline` (i.e., you need to define these two classes) to represent todo tasks and deadlines, respectively.

## Monty 10
Enhance the Monty 9 code to extract the following classes:

* `UserInterface`: an object of this class can be used to handle reading input from the user and showing output back to the user.
* `StorageManager`: an object of this class can be used to read data from the data file and write data back to the data file.
* `TaskManager`: an object of this class will hold the list of Task/Deadline objects and will execute commands.

**Optional feature to consider:** add a progress command that shows how many tasks/deadlines were marked as done during a session so far. Here is an example output:
```
>>> What can I do for you?

list
>>> Here is the list of tasks:
    ============================================================
    STATUS | INDEX | DESCRIPTION                 | DEADLINE
    ------------------------------------------------------------
      ✓    |   1   | borrow book                 | -
      ✗    |   2   | read book                   | -
      ✗    |   3   | return book                 | Monday
    ------------------------------------------------------------
>>> What can I do for you?

progress
>>> Progress for this session: todos 0 deadlines 0
>>> What can I do for you?

done 2
>>> Congrats on completing a task! :-)
>>> What can I do for you?

progress
>>> Progress for this session: todos 1 deadlines 0
>>> What can I do for you?

done 3
>>> Congrats on completing a task! :-)
>>> What can I do for you?

progress
>>> Progress for this session: todos 1 deadlines 1
>>> What can I do for you?

pending 2
>>> OK, I have marked that item as pending
>>> What can I do for you?

progress
>>> Progress for this session: todos 0 deadlines 1
>>> What can I do for you?

list
>>> Here is the list of tasks:
    ============================================================
    STATUS | INDEX | DESCRIPTION                 | DEADLINE
    ------------------------------------------------------------
      ✓    |   1   | borrow book                 | -
      ✗    |   2   | read book                   | -
      ✓    |   3   | return book                 | Monday
    ------------------------------------------------------------
>>> What can I do for you?
```
## Monty 11
Enhance the **Monty 10 code* to make the `Deadline` class inherit from the `ToDo` class:

## Monty 12
Enhance the **Monty 11 code** to divide the source code into multiple files (e.g., `todo.py`, `deadline.py`, etc.).

## Monty 13
Add some **unit tests** to **Monty 12 code.**

## Monty 14
Enhance the **Monty 13 code** to integrate it with the **skeletal GUI** given below.

Notes about the given version of the GUI:

* The GUI shows the list of tasks all the time.
* It initializes with some dummy data.
* It only supports an add command and a help command.

Here are some screenshots of the GUI:
```python
import datetime
from tkinter import *

import sys


class GUI:

    def __init__(self, task_manager):
        self.task_manager = task_manager
        self.window = Tk()
        self.window.geometry('800x700')  # set Window size
        self.window.title('Monty')  # set Window title

        self.input_box = Entry(self.window)  # create an input box
        self.input_box.pack(padx=5, pady=5, fill='x')  # make the input box fill the width of the Window
        self.input_box.bind('<Return>', self.command_entered)  # bind the command_entered function to the Enter key
        self.input_box.focus()  # set focus to the input box

        # add a text area to show the chat history
        self.history_area = Text(self.window, width="50")
        self.history_area.pack(padx=5, pady=5, side=LEFT, fill="y")
        self.output_font = ('Courier New', 12)
        self.history_area.tag_configure('error_format', foreground='red', font=self.output_font)
        self.history_area.tag_configure('success_format', foreground='green', font=self.output_font)
        self.history_area.tag_configure('normal_format', font=self.output_font)

        # add a text area to show the list of tasks
        self.list_area = Text(self.window)
        self.list_area.pack(padx=5, pady=5, side=RIGHT, fill="both")
        self.list_area.tag_configure('normal_format',  font=self.output_font)
        self.list_area.tag_configure('pending_format', foreground='red', font=self.output_font)
        self.list_area.tag_configure('done_format', foreground='green', font=self.output_font)

        # show the welcome message and the list of tasks
        self.update_chat_history('start', 'Welcome to Monty!', 'success_format')
        self.update_task_list(self.task_manager.items)

    def update_chat_history(self, command, response, status_format):
        """
        status_format: indicates which color to use for the status message
          can be 'error_format', 'success_format', or 'normal_format'
        """
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.history_area.insert(1.0, '-' * 40 + '\n', 'normal_format')
        self.history_area.insert(1.0, '>>> ' + response + '\n', status_format)
        self.history_area.insert(1.0, 'You said: ' + command + '\n', 'normal_format')
        self.history_area.insert(1.0, current_time + '\n', 'normal_format')

    def update_task_list(self, tasks):
        self.list_area.delete('1.0', END)  # clear the list area
        for i, task in enumerate(tasks):
            if task[1]:
                icon = '✓'
                output_format = 'done_format'
            else:
                icon = '✗'
                output_format = 'pending_format'
            self.list_area.insert(END, icon + ' ' + str(i+1) + ' ' + task[0] + '\n', output_format)

    def clear_input_box(self):
        self.input_box.delete(0, END)

    def command_entered(self, event):
        command = None
        try:
            command = self.input_box.get()
            if command.strip().lower() == 'exit':
                sys.exit()
            output = self.task_manager.execute_command(command)
            self.update_chat_history(command, output, 'success_format')
            self.update_task_list(self.task_manager.items)
            self.clear_input_box()
        except Exception as e:
            self.update_chat_history(command, str(e) + '\n' + self.task_manager.get_help(), 'error_format')

    def start(self):
        self.window.mainloop()


class TaskManager:
    def __init__(self):
        self.items = [
            ['task 1', True],
            ['task 2', False],
            ['task 3', True]
        ]

    def get_help(self):
        return 'help:\n...'

    def execute_command(self, command):
        if command == 'help':
            return self.get_help()
        elif command.startswith('add '):
            self.items.append([command[4:], False])
            return 'task added'
        else:
            raise Exception('Command not recognized')


GUI(TaskManager()).start()
```

