#Tkinter to design interactive graphical user interface
from Tkinter import *
#to retirieve images
from PIL import Image, ImageTk, ImageFilter

# computation know;edge engine library
import wolframalpha

# library to convert text into speech
from gtts import gTTS

#library for wikipedia
import wikipedia

#import nltk
import nltk

#import webbrowser
import webbrowser

#import natural language processing library required functions
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#operating system libary
import os

#importing user defined module for data sets
import dataset as data


window = Tk()
window.title("macfi")
window.resizable(0,0)
icon = PhotoImage(file="icon.gif")
window.tk.call('wm','iconphoto',window._w,icon)

# get 
def data_processing(data):
    print data
    try:
        #if data.lower() in dataset.general_query:
        # answer = dataset.general_query[data.lower()]
        # else:
        #     pass
        # elif __stopwords__(input) in data.task_manager:
        #   check = raw_input("are you sure you want to",__stopwords__(input),"your computer: (y/n)")
        #   if check.lower() is 'y':
        #       os.system(data.task_manager[__stopwords__(input).lower])
        #       answer = "shuting down computer"
        #   else:
        #       break
        # else:
        # except Exception as e:
        #wolfram computatoional engine
        app_id = "6T3KKV-222Y9EW6A7"
        #get a client object
        client = wolframalpha.Client(app_id)
        #generating response
        res = client.query(data)
        # answer construction
        answer = next(res.results).text
    except Exception as e:
        #wiki query
        answer = wikipedia.summary(data, sentences=2)
    except:
        answer = 'Sorry sir i could not find anything '
    return answer

def get_result(input):
    answer = data_processing(input)

    try:
        if answer is not None:
            mytext = answer
        else:
            mytext = "I could not find answer"

        
    except Exception as e:
        mytext = "i am having trouble sir sorry for incovenience"

    try:
        speak(mytext)
    except Exception as e:
        mytext = "i could not find answer sorry for incovenience"
            
def speak(mytext):
        language = 'en'
        # Passing the text and language to the engine, 
        # here we have marked slow=False. Which tells 
        # the module that the converted audio should 
        # have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)

        # Saving the converted audio in a mp3 file named
        # welcome 
        myobj.save("welcome.mp3")

        # Playing the converted file
        os.system("mpg321 welcome.mp3")



bg_image = PhotoImage(file='background.gif')
bg_image_width = bg_image.width()
bg_image_height = bg_image.height() 
window.geometry('{}x{}'.format(bg_image_width,bg_image_height)) 
window = Label(window, image=bg_image,bd =-2)


#textbox = Entry(window, width=40, bg= "blue",bd=0)

large_font = ('Times New Roman',15)
#Entry might be Text with height=1,
textbox = Entry(window,  width=35, font=large_font)
textbox.place(x=205,y=200, anchor='s')

#getting question
#question = "Since You Didn't ask Hence im telling about myself"
try:
    def onclick():
        input = textbox.get()
        textbox.delete(0, END)
        if input != "":
            question = input
            input=""
            print question
            get_result(question)
        else:
            pass
    def OnEnter(event):
        input = event.widget.get()
        textbox.delete("0", END)
        if input != "":
            question = input
            input = ""
            get_result(question)
        else:
            pass
except Exception as e:
    pass

btn = Button(window, text="Go", command=onclick)
btn.place(x=405.5,y=200, anchor='s')
textbox.bind('<Return>',OnEnter)

# b.pack()
# textbox.grid(row=1,column=1,sticky=W)
# textbox.pack()
# button = Button(window, 100, 25, 'red')
# button.place(x=250,y=200,anchor='s')

window.configure(background="#23bdec")
window.pack(fill='both', expand =True)
#window.overrideredirect(1)
window.mainloop()


