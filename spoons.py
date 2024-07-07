import PySimpleGUI as sg
import random

# Define the layout with neon colors
layout = [
    [sg.Text("Task Name", text_color='cyan', background_color='#000080'), sg.InputText(key='task')],
    [sg.Text("Difficulty (1-5 Spoons)", text_color='cyan', background_color='#000080'), sg.Slider(range=(1, 5), orientation='h', key='difficulty', background_color='#000080', trough_color='magenta')],
    [sg.Button("Add Task", button_color=('black', 'lime')), sg.Button("Get Task", button_color=('black', 'yellow')), sg.Button("Complete Task", button_color=('black', 'red'))],
    [sg.Column([
        [sg.Text("Tasks List", text_color='cyan', background_color='#000080')],
        [sg.Listbox(values=[], size=(40, 10), key='tasks', text_color='lime', background_color='black')]
    ]),
    sg.VerticalSeparator(),
    sg.Column([
        [sg.Text("Recently Completed", text_color='cyan', background_color='#000080')],
        [sg.Listbox(values=[], size=(40, 10), key='completed_tasks', text_color='lime', background_color='black')]
    ])],
    [sg.Text("Available Spoons", text_color='cyan', background_color='#000080'), sg.Slider(range=(1, 10), orientation='h', key='spoons', background_color='#000080', trough_color='magenta')],
    [sg.Text("Suggested Task", text_color='cyan', background_color='#000080'), sg.Text("", size=(40, 1), key='suggested_task', text_color='lime', background_color='black')],
    [sg.Text("Ways to Gain More Spoons", text_color='cyan', background_color='#000080'), sg.Listbox(values=['Take a walk', 'Meditate', 'Healthy snack', 'Short nap'], size=(40, 5), key='extra_spoons', text_color='lime', background_color='black')],
]


# Set window color scheme to black for a neon look
sg.theme('DarkBlack')

# Create the window
window = sg.Window("Extra Spoons", layout, background_color='#000080')

tasks = []
completed_tasks = []


def update_tasks_list(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: (x[1], x[0].lower()))
    return [f"{t[0]} ({t[1]} Spoons)" for t in sorted_tasks]


def update_completed_tasks(completed_tasks):
    return [f"✔ {t[0]} ({t[1]} Spoons)" for t in completed_tasks]


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Add Task":
        task = values['task']
        difficulty = int(values['difficulty'])
        if task and difficulty:
            tasks.append((task, difficulty))
            window['tasks'].update(update_tasks_list(tasks))
    if event == "Get Task":
        available_spoons = int(values['spoons'])
        filtered_tasks = [task for task in tasks if task[1] <= available_spoons]

        if filtered_tasks:
            suggested_task = random.choice(filtered_tasks)
            window['suggested_task'].update(f"{suggested_task[0]} ({suggested_task[1]} Spoons)")
        else:
            window['suggested_task'].update("No suitable tasks available.")
    if event == "Complete Task":
        selected_task = values['tasks'][0] if values['tasks'] else None
        if selected_task:
            task_name, task_difficulty = selected_task.split(' (')
            task_difficulty = int(task_difficulty.split(' ')[0])
            tasks = [task for task in tasks if not (task[0] == task_name and task[1] == task_difficulty)]
            completed_tasks.append((task_name, task_difficulty))
            window['tasks'].update(update_tasks_list(tasks))
            window['completed_tasks'].update(update_completed_tasks(completed_tasks))

window.close()

#todo: 1) Change colors and fonts and the way it looks 2) Add txt file to save, edit, delete list, 3) make a delete item button,
# 4) figure out the sort issue, 5) make this prettier once the functionality is in there.
# 6) create a functions file? 7) Maybe have a place somewhere where you can track your daily spoons over time
# 8) the task list should be sort of like an info dump, so it has to be easy to use. Making lists is good for the brain
#  9) Keep playing with this to figure out what else it needs. 10) turn into an ios app? 11) make it so you can choose
#  your color scheme. Have retro, pastel, earthy I don't know? If this is an app, the first screen is like...hello how
#  are you today? Select mood and select spoon availability. once you do that you are taken to a menu that is like:
#  look at task list, create task list (and maybe you can create multiple lists 1)work, home, etc.
#  and then there will be the extra spoons task randomizer
