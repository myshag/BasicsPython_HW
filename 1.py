import tkinter as tk
import time


class TrafficLights(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.runt = time.time()
        self.pack()
        self.master.title("Traffic Lights")
        self.grid()
        self.draw()
        self.animation()
        

    def draw(self):
        self.canvas = tk.Canvas(self, width = 300, height = 400, bg = "black")
        self.canvas.grid(row = 0, column = 0)
        self.canvas.create_rectangle(100, 50, 200, 350)
        self.light_red=self.canvas.create_oval(100, 50, 200, 150, fill='white')
        self.light_yellow=self.canvas.create_oval(100, 150, 200, 250, fill='white')
        self.light_green=self.canvas.create_oval(100, 250, 200, 350, fill='white')
        
        self.lumps = {"red":self.light_red,
                        "yellow":self.light_yellow,
                        "green":self.light_green}

    def animation(self):
        self.light("red","on")
        self.after(7000, self.light("red","off"))
        self.after(7020, self.light("yellow","on"))
        self.after(9030, self.light("yellow","off"))
        self.after(9040, self.light("green","on"))
        self.after(12000, self.light("green","off"))
        self.after(12500,self.animation)


    def light(self, color:str, action:str):
        
        if color in ["red","yellow","green"]:
            print(str(time.time()-self.runt),color,action)
            if action=="on":
                self.canvas.itemconfig(self.lumps[color],fill=color)
            elif action=="off":
                self.canvas.itemconfig(self.lumps[color],fill='white')
        self.canvas.update()
    
            

root = tk.Tk()
app = TrafficLights(master=root)
root.mainloop()
