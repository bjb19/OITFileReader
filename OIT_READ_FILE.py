from tkinter import *

#This Function confirms that the file is in the system
#After confirming it puts the data into the text box
def searchFile(input, box, name) :
    #Clears Text Box
    box.config(state = NORMAL)
    box.delete("1.0", END)
    try :
        #Sets the saved name to the input in the file search bar
        #Reads and then inserts the data int the text box
        name.set(input.get().rstrip())
        file = open(name.get().rstrip())
        data = file.read()
        box.insert("1.0", data)
        file.close()
    except FileNotFoundError :
        #Clears file search bar and informs user the directory was invalid
        errorMsg = "Sumbit a valid Directory Input"
        input.delete(0, END)
        input.insert(0, errorMsg)
    return
    



def submitChanges(name, textInput, fileInput) :
    try :
        #Clears File
        open(name.get(), 'w').close()
        #Opens File Again and Writes all the copies the contents in the text box to it
        file = open(name.get(), 'w')
        file.write(boxInput(textInput))
        file.close()
        #Clears the File Search Bar
        fileInput.delete(0, END)
    except FileNotFoundError :
        #Clears the file search Bar and leaves an error message in it
        errorMsg = "Sumbit a valid Directory Input"
        input.delete(0, END)
        input.insert(0, errorMsg)
    #Clears the text box and resets the name of the file opened
    textInput.config(state = NORMAL)
    textInput.delete("1.0", END)
    name.set("")
    return

#Reads input from text boxes and returns it
def boxInput(box) :
    input = box.get("1.0",END)
    return input

#Opens GUI Window
root = Tk()
root.geometry("750x500")
root.title("File Display")


#Name of file currently opened saved outside of functions
fileName = StringVar()


#Generates a label, text search bar and a submit button
#These are used to type in the file name and write to it
fileBoxLabel = Label(root, text = "Type File Name here")
fileBoxLabel.pack()
fileNameBox = Entry(root, width = 100)
fileNameBox.pack()
fileSearchButton = Button(root, command = lambda : searchFile(fileNameBox, fileTextBox, fileName), text = "Search for File")
fileSearchButton.pack()


#Generates a label text box and sumbit changes button
#This is where the text will be displayed from the file and edited
#When changes are done the submit button will copy the text over to the file
fileLabel = Label(root, text = "File Contents")
fileLabel.pack()
fileTextBox = Text(root)
fileTextBox.pack()
submitButton = Button(root, command = lambda : submitChanges(fileName, fileTextBox, fileNameBox), text = "Submit Changes")
submitButton.pack()


root.mainloop()