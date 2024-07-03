import FreeSimpleGUI as sg
layout = [
  [sg.Text("Enter your name:")],
  [sg.InputText(key="name")],
  [sg.Button("Greet Me")]
]
window = sg.Window("Greeting App", layout)
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  elif event == "Greet Me":
    name = values["name"]
    print(f"Hello, {name}!")
window.close()