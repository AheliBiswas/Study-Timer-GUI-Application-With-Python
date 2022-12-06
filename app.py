import tkinter as tk
import time
from tkinter import messagebox


def start_timer():
    temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    while temp > -1:
        mins = temp // 60
        secs = temp % 60
        hours = 0
        if mins > 60:
            hours = mins // 60
            mins = mins % 60

        hour.set("{0:02d}".format(hours))
        minute.set("{0:02d}".format(mins))
        second.set("{0:02d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            hour.set("00")
            minute.set("00")
            second.set("00")
            messagebox.showinfo("Timer", "Timer has ended")

        temp -= 1


def set_timer():
    hour.set("00")
    minute.set("25")
    second.set("00")


def break_time():
    hour.set("00")
    minute.set("10")
    second.set("00")


# ----------------------- Creating the window ----------------------------

root = tk.Tk()
root.resizable(False, False)
root.title('Timer')
root.geometry('384x150+450+150')

hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

hour.set("00")
minute.set("00")
second.set("00")

# ----------------------- Hour,Min,Sec Entries ----------------------------

hour_entry = tk.Entry(root, textvariable=hour, font=("Lato", 32, "bold"), bd=0)
hour_entry.place(height=39, width=50, x=98, y=36)

label1 = tk.Label(root, text=":", font=("Lato", 24, "bold"), fg='black')
label1.place(x=150, y=34)

minute_entry = tk.Entry(root, textvariable=minute, font=("Lato", 32, "bold"), bd=0)
minute_entry.place(height=39, width=50, x=168, y=36)

label2 = tk.Label(root, text=":", font=("Lato", 24, "bold"), fg='black')
label2.place(x=220, y=34)

second_entry = tk.Entry(root, textvariable=second, font=("Lato", 32, "bold"), bd=0)
second_entry.place(height=39, width=50, x=238, y=36)

# ----------------------- Play,Pause,Resume Buttons ----------------------------

play = tk.PhotoImage(file="white_icon/play-white.png")
play_btn = tk.Button(root, image=play, borderwidth=0, bg='#A6C7DF', cursor="hand2", command=start_timer)
play_btn.place(x=77, y=98, width=60, height=30)

preset = tk.PhotoImage(file="white_icon/tomato_white.png")
preset_btn = tk.Button(root, image=preset, borderwidth=0, bg='#A6C7DF', cursor="hand2", command=set_timer)
preset_btn.place(x=170, y=100, width=60, height=30)

brk = tk.PhotoImage(file="white_icon/break.png")
brk_btn = tk.Button(root, image=brk, borderwidth=0, bg='#A6C7DF', cursor="hand2", command=break_time)
brk_btn.place(x=265, y=100, width=60, height=30)

root.mainloop()
