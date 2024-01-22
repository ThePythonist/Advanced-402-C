import tkinter

window = tkinter.Tk()
window.title("Some Window")
window.geometry("320x500")
# window.resizable(width=False, height=True)
window.configure(background="#F1C09C", )

message = tkinter.Label(window, text="Welcome", bg="red", fg="white").pack(fill="x", expand=True)
btn = tkinter.Button(window, text="Submit", command=lambda: print("Button clicked")).pack(anchor="s")

window.mainloop()
