import pyautogui
import time
import tkinter as tk

def ScreenShot():
    # time.sleep(5)
    name = time.time()
    name = 'C:/Users/Techfaith/Desktop/LearningPython/{}.png'.format(name)
    shot = pyautogui.screenshot()
    shot.save(name)
    shot.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Take screenshot", command=ScreenShot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="Close", command=quit)
close.pack(side=tk.LEFT)

root.mainloop()