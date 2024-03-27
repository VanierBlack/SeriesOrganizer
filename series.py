import module


#files tuple to store the files
files = ()
#list for storing each file's creation time in seconds
files_created_time = []
#dictionary to bind each file with its creation time
files_time_dict = dict()
#the available extensions for each file, where the extensions are the keys and files are the  values
extensions = dict()


def change_names(**entry_boxes):
    """
    this function is called when the Submit changes buttons was pressed
    this function take all of the information given by the user and store them in a kwargs
    then extracts each file path and its extension 
    then rename each file with new name
    finally empty the containers
    """

    global files
    global files_time_dict
    global extensions

    epi = entry_boxes["epi"].get()
    sea = entry_boxes["sea"].get()
    entr = entry_boxes["entr"].get()
    
    for each_epis in range(int(epi), len(files)+1):
        for ext in extensions.keys():
            if ext in files[each_epis-1]:
                name_file = (files[each_epis-1].split('/')[-1])
                path_file = (files[each_epis-1][:-len(name_file)])
                module.os.rename(path_file + name_file,path_file + entr + " S0"+ sea + (" E0{}".format(str(each_epis))+".{}".format(ext)) )
    files = module.empty_containers(files=files, extensions = extensions, dict_time = files_time_dict)
    
def extension_extract():
    """
    this function is used 
    to extract the extension from each file then chain the files of the common extension
    with key_value pairs using dictionaries
    """

    global files
    each_existed_extension = []
    for file in files:

        #splite the file out of the dot
        file_extension = (file.split('.'))

        #get the extension, which is usually the last item
        each_existed_extension.append(file_extension[len(file_extension) - 1])
    #delete the repeated extensions by convert the list each_existed_extension to a set
    each_existed_extension = set(each_existed_extension)
    #return the dictionary after chaining the key value pairs
    return  module.list_dic(each_existed_extension, files, 'ld')

def choose(text_box):
    """
    this function is called when choose_files button was pressed
    to open window to choose the required files(videos) to be rename 
    """
    global files
    global files_created_time
    global files_time_dict
    global extensions
    #multiple files, print them into the Text box
    files = module.filedialog.askopenfilenames()
    for file in files:
        text_box.insert(1.0,file+"\n\n")

    #store each file's creation time in seconds in files_created_time
    files_created_time = module.get_file_time_epoch(files)
    #change the order of the files in files tuple according to the time indices
    files = module.keys_values_tied_sorted(files, files_created_time)
    #call the extension function to splite the extensions from the files 
    #this function return a dictionary containing the keys as extensions, values as files
    extensions = extension_extract()


#here is the window initializing, and its attributes
window = module.Tk()
window.geometry("650x430")
window.config(bg="black")
window.title("SeriesNames")

#separate frame for the text box
frame_text = module.Frame(window, bg="black", width=200, height=100)
frame_text.pack(padx=10, pady= 10)

#frame for the other widgets
frame_widget = module.Frame(window, bg="black", width=200, height=100)
frame_widget.pack(padx=10, pady=10)

#text box initialization
text_files = module.Text(frame_text, font=("Ink Free", 13), fg="aqua", bg="black", width=60, height=10)
text_files.grid(row=0, column= 0, padx=10, pady=10)

#label to display a text about the desirable name
convert_name = module.Label(frame_widget, bg="black", fg="aqua", font=("Ink Free", 13),
                 text="Converted Name")
convert_name.grid(row = 0, column= 0, padx=10, pady=10)

#initialization of the entry of the desirable name
convert_name_entry = module.Entry(frame_widget,relief='raised', border=2,font=("Ink Free", 12), fg="aqua", bg="black")
convert_name_entry.grid(row = 1, column = 0, padx=10, pady=10)

#initialization of the label of the wanted first epsiode to begin with
episode_number = module.Label(frame_widget, bg="black", fg="aqua", font=("Ink Free", 13),
                 text="Episode Number")
episode_number.grid(row = 0, column= 1, padx=10, pady=10)

#initialization of the entry of the first episode to begin with
episode_box  = module.Entry(frame_widget, relief='raised', border=2,font=("Ink Free", 12), fg="aqua", bg="black")
episode_box.grid(row=1, column= 1, padx=10, pady=10)

#initialization of the label of the season of the whole files for one season
season_number = module.Label(frame_widget, bg="black", fg="aqua", font=("Ink Free", 13),
                 text="Season Number")
season_number.grid(row = 0, column= 2, padx=10, pady=10)

#initialization of the entry of the season of the whole files for one season
season_box  = module.Entry(frame_widget, relief='raised', border=2,font=("Ink Free", 12), fg="aqua", bg="black")
season_box.grid(row=1, column= 2, padx=10, pady=10)

#initialization of the choose_files button with its attributes
choose_files = module.Button(frame_widget, text="Choose Files", bg="black", fg="aqua",
                font=("Ink Free", 16), activebackground="black", activeforeground="aqua",
                command=module.partial(choose, text_files))
choose_files.grid(row = 4, column= 1,padx=10, pady=10)

#initialization of the submit_changes button to save the files with desirable new name
submit_changes =module. Button(frame_widget, text="Submit Changes",  bg="black", fg="aqua",
                font=("Ink Free", 16), activebackground="black", activeforeground="aqua",
                command=module.partial(change_names, epi = episode_box, sea = season_box, entr = convert_name_entry))
submit_changes.grid(row=4, column=0, padx=10, pady=10)

window.mainloop()