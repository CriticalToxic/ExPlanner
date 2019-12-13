import tkinter as tk
import time, json, os, datetime, subprocess


def search(x=None):
    titleIn.set("Searching...")
    day = str(dayBox.get())
    month = str(monthBox.get())
    year = str(yearBox.get())
    if len(day) == 1:
        day = "0" + day
        print(day)
    if len(month) == 1:
        month = "0" + month
        print(month)
    date = "{}/{}/{}".format(day,month,year)
    titleIn.set("Results for " + date + ":")
    resultsIn.set("Searching")
    f = open("exerciseHistory.json")
    history = json.load(f)
    theResults = """"""
    for i in history:
        if i["date"] == date:
            for j in i["exercises"]:
                if j["name"] == "Jogging":
                    theResults = theResults + """[] You ran {} miles's. \n""".format(j["setAmt"])
                else:
                    theResults = theResults + """[] {} {}'s.\n""".format(j["setAmt"] * j["setsOf"], j["name"])
    if theResults == """""":
        resultsIn.set("No Results Found")
    else:
        resultsIn.set(theResults)

def back():
    root.destroy()
    subprocess.call('pyw menu.pyw')


#####################

root = tk.Tk()
width, height = "240", "200"
root.geometry("{}x{}".format(width, height))
root.wm_iconbitmap('runnericon.ico')
root.title("ExPlanner")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

#####################

formatLabel = tk.Label(root, text="DD     /     MM    /    YYYY")
formatLabel.pack()
formatLabel.place(x=10,y=10,width=150, height=20)

dayIn = tk.IntVar(root)
dayBox = tk.IntVar(root)
dayBox = tk.Spinbox(root, textvariable=dayIn, from_=1, to=31, command=search)
dayBox.pack()
dayBox.place(x=10,y=30,width=40, height=20)
dayIn.set(int(datetime.datetime.now().strftime("%d")))

monthIn = tk.IntVar(root)
monthBox = tk.IntVar(root)
monthBox = tk.Spinbox(root,textvariable=monthIn, from_=1, to=12, command=search)
monthBox.pack()
monthBox.place(x=60,y=30,width=40, height=20)
monthIn.set(int(datetime.datetime.now().strftime("%m")))

yearIn = tk.IntVar(root)
yearBox = tk.IntVar(root)
yearBox = tk.Spinbox(root, textvariable=yearIn,  from_=2019, to=9999, command=search)
yearBox.pack()
yearBox.place(x=110,y=30,width=60, height=20)
yearIn.set(int(datetime.datetime.now().strftime("%Y")))

titleIn = tk.StringVar(root)
titleIn.set("Insert a date to get some results.")
resultTitle = tk.Label(root, textvariable=titleIn,text="Insert a date for some results", font="BOLD")
resultTitle.pack()
resultTitle.place(x=10, y=60)

resultsIn = tk.StringVar(root)
results = tk.Label(root, textvariable=resultsIn)
results.pack()
results.place(x=10, y=82)

exitBtn = tk.Button(root, text="Back", command=back)
exitBtn.pack()
exitBtn.place(x=200, y= 175, height="15", width=30)

search()

#####################
root.update()
root.mainloop()

