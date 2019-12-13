import tkinter as tk
import subprocess

def exitApp():
    root.destroy()
    exit()

def manualadd():
    root.destroy()
    subprocess.call('pyw manualadd.pyw')

def search():
    root.destroy()
    subprocess.call('pyw search.pyw')


root = tk.Tk()
width, height = "210", "210"
root.geometry("{}x{}".format(width, height))
root.title("ExPlanner")
root.wm_iconbitmap('runnericon.ico')
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

manual_btn = tk.Button(root, text="Manually Add An Exercise",command=manualadd)
manual_btn.pack()
manual_btn.place(x=10, y=10, width=190, height=40)

random_btn = tk.Button(root, text="Generate [Under Construction]")
random_btn.pack()
random_btn.place(x=10, y=60, width=190, height=40)

search_btn = tk.Button(root, text="Search for An Exercise",command=search)
search_btn.pack()
search_btn.place(x=10, y=110, width=190, height=40)

exit_btn = tk.Button(root, text="Exit",command=exitApp)
exit_btn.pack()
exit_btn.place(x=60, y=160, width=80, height=40)

root.update()

root.mainloop()
