import tkinter as tk
root = tk.Tk()
root.geometry("1200x800")
def update_btn_text():
    if(close_button["text"]=="a"):
        close_button.configure(text="b")
    else:
        close_button.configure(text="a")


close_button = tk.Button(root, text="a", command=update_btn_text)
close_button.pack()

root.mainloop()