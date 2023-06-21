import tkinter as tk

root = tk.Tk()
root.geometry("500x1000")

canvas = tk.Canvas(root, bg = "white")
canvas.pack(fill = tk.BOTH, expand = True)

canvas.create_line(150, 200, 150, 300, fill = "black",tag="person")
canvas.create_line(150, 250, 50, 210, fill = "black",tag="person")
canvas.create_line(150, 250, 250, 210, fill = "black",tag="person")
canvas.create_line(150, 300, 50, 400, fill = "black",tag="person")
canvas.create_line(150, 300, 250, 400, fill = "black",tag="person")
canvas.create_oval(100,100,200,200,fill='white',tag="person")

def move():  
    canvas.move("person", 5, 0)
    canvas.after(50, move)    
move()
root.mainloop()