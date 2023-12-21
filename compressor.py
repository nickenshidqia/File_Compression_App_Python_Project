import PySimpleGUI as sg
from zip_creator import make_archive

#theme
sg.theme("LightPurple")

# Create GUI elements
label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color = "green")
exit_button = sg.Button("Exit")

# Create the main window
window = sg.Window("File Compressor",
                   layout = [[label1, input1, choose_button1],
                             [label2, input2, choose_button2],
                             [compress_button, output_label, exit_button]])

# Main event loop
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Choose':
            #split to handling if user select more than 1 file
            filepaths = values['files'].split(";")
            folder = values['folder']

            #function from zip_creator
            make_archive(filepaths, folder)

            window["output"].update(value = "Compression completed!")

        case 'Exit':
            break

window.close()