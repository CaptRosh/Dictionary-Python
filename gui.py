import tkinter as tk
from tkinter import messagebox
import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    closematch = get_close_matches(w,data.keys(),cutoff=0.8) 
    if w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif w in data:
        return data[w]
    elif len(closematch)>0:
        for i in range(0,len(closematch)):
            correction = tk.messagebox.askyesno(title="Spell Error",message="You entered {}.\nDid you mean {} instead?" .format(w,closematch[i])) 
            # input(( "Did you mean %s instead?" % closematch[i]))
            if correction:
                return data[closematch[i]]
                break
        else:
            return "Word not found in dictionary."
    else:
        return "Word not found in dictionary."

def output(meaning):
    num = 1
    op = ''
    if type(meaning) == str:
        op = meaning
    elif type(meaning) == list:
        for item in meaning:
            op += (str(num) + ") " + item + "\n")
            num = num + 1
    
    return op


window = tk.Tk()
window.title("Dictionary by Roshan Srivastava")
window.configure(bg='#008080')
window.geometry("700x400")

# photo = tk.PhotoImage(file = "assets/dictionary.gif")
# tk.Label(window,image=photo,bg="#008080").grid(row = 2,column = 1,rowspan =1,sticky="e")

def click():
    word = text.get()

    tk.Label(window,text="\nDefinition:",bg="#008080",font="Hack 15 bold").grid(row=4,column=0,sticky='w')

    outputText = tk.Text(window,width=80,height=15,wrap="word",background="#528B8B",font = "Hack 12 bold" )
    outputText.grid(row=5,column=0,columnspan=2)

    outputText.delete(0.0,"end")
    opText = output(translate(word))
    outputText.insert("end",opText)

tk.Label(window,text="Enter a word:",bg="#008080",font = "Hack 15 bold",padx=5).grid(row=1,column=0,sticky='w')

text = tk.Entry(window, width = 35, bg='#528B8B')
text.grid(row=2,column=0,sticky="w")

tk.Button(window,text="SUBMIT",width=6,command=click,pady=10,padx=10).grid(row=3,column=0,stick='w')


window.mainloop()