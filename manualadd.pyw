
import tkinter as tk
import threading, time, json, multiprocessing, datetime
# Actual Code



def back():
    import os, subprocess
    root.destroy()
    subprocess.call('pyw menu.pyw')
    exit()

def save_exercise():
    textIn.set("Saved!")
    f = open("exerciseHistory.json", "r")
    history = json.load(f)
    today = datetime.datetime.now().strftime("%d/%m/%Y")
    if exerciseVar.get() == "Jogging (miles)":
        exerciseVar.set("Jogging")
    foundDate = False
    for i in range(len(history)):
        if history[i]["date"] == today:
            current_exercise = {"name": exerciseVar.get(), "setsOf": int(setBox.get()), "setAmt": int(setDoneBox.get()), "total": int(setBox.get()) * int(setDoneBox.get())}
            history[i]["exercises"].append(current_exercise)
            foundDate = True
    if not foundDate:
        history.append({"date": today, "exercises": [{"name": exerciseVar.get(), "setsOf": int(setBox.get()), "setAmt": int(setDoneBox.get()), "total": int(setBox.get()) * int(setDoneBox.get())}]})
    f.close()
    f = open("exerciseHistory.json", "w")
    json.dump(history, f, indent=4, sort_keys=True)
    f.close()



def tick():
    if outBoxTicked.get() == 1:
        tick()

def resetSavedWithX(x):
    textIn.set("Unsaved!")
def resetSaved():
    textIn.set("Unsaved!")
##################################


root = tk.Tk()
width, height = "240", "200"
root.geometry("{}x{}".format(width, height))
root.wm_iconbitmap('runnericon.ico')
root.title("ExPlanner")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))


#########################

# All Widget Creations


'''start_button = tk.Button(root,text="Say Hi", command=example_function)
start_button.pack()'''
textIn = tk.StringVar(root)
text = tk.Label(root,textvariable=textIn ,text="Unsaved!")
textIn.set("Unsaved!")
text.pack()
text.place(x=10, y =137)

text1 = tk.Label(root,text="Exercise:")
text1.pack()
text1.place(x=10, y =14)

text2 = tk.Label(root,text="Sets Of:")
text2.pack()
text2.place(x=10, y =54)

text3 = tk.Label(root,text="Sets Done:")
text3.pack()
text3.place(x=10, y =94)

saveExercise_btn = tk.Button(root, text="Save New Exercise",command=save_exercise)
saveExercise_btn.pack()
saveExercise_btn.place(x=120, y=134, width=105, height=25)

exerciseVar = tk.StringVar(root)
exerciseVar.set("Select An Exercise")
options = ["Jogging (miles)", "Push-Ups", "Sit-Ups", "Squats", "Hill-Reps"]
exerciseOption = tk.OptionMenu(root, exerciseVar, *options, command=resetSavedWithX)
exerciseOption.pack()
exerciseOption.place(x=75, y=10, width=150, height=30)

setBox = tk.IntVar(root)
setBox = tk.Spinbox(root, from_=1, to=100, command=resetSaved)
setBox.pack()
setBox.place(x=75,y=50,width=150, height=30)

setDoneBox = tk.IntVar(root)
setDoneBox = tk.Spinbox(root, from_=1, to=100, command=resetSaved)
setDoneBox.pack()
setDoneBox.place(x=75,y=90,width=150, height=30)

exitBtn = tk.Button(root, text="Back", command=back)
exitBtn.pack()
exitBtn.place(x=188, y= 170)

root.update()
################
root.mainloop()

#######################
