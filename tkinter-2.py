import tkinter

window = tkinter.Tk()
window.title("Some Window")
window.geometry("320x500")
window.configure(background="#F1C09C", )

def show_message():
    message.config(text="Button Clicked!",bg="white")


# message = tkinter.Label(window, text="Welcome", bg="red", fg="white").pack(fill="x", expand=True)
message = tkinter.Label(window,text="",background="#F1C09C")
message.pack()
btn = tkinter.Button(window, text="Submit", command=show_message).pack(anchor="s")

window.mainloop()
