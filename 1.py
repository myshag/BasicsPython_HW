import tkinter as tk
import time


class TrafficLights(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Traffic Lights")
        self.grid()
        self.draw()

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
        self.light("yellow","off")
        self.canvas.update()
        time.sleep(1)
        self.light("yellow","on")
        self.canvas.update()
        self.after(4,self.animation)
          
        

        

    def start_traffic(self):
        self.animation()
        self.mainloop()

        
    def light(self, color:str, action:str):
        if color in ["red","yellow","green"]:
            if action=="on":
                self.canvas.itemconfig(self.lumps[color],fill=color)
            elif action=="off":
                self.canvas.itemconfig(self.lumps[color],fill='white')
    
            


traffic_lights = TrafficLights()
traffic_lights.start_traffic()
