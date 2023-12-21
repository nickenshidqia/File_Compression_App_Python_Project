import PySimpleGUI as sg
from zip_extractor import extract_archive

#theme
sg.theme("DarkAmber")

#Create GUI elements
label1 = sg.Text("Select archive :  ")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select directory :")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="orange")
exit_button = sg.Button("Exit")

#aligned column
#col1 = sg.Column([[label1], [label2]])
#col2 = sg.Column([[input1], [input2]])
#col3 = sg.Column([[choose_button1], [choose_button2]])

# Create the main window
window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label, exit_button]])

# Main event loop
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Choose' :
            archivepath = values["archive"]
            dest_dir = values["folder"]
            extract_archive(archivepath, dest_dir)
            window["output"].update(value="Extraction completed !")

        case 'Exit':
            break

window.close()

