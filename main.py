from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog,messagebox
import PIL.ImageGrab as ImageGrab

class Paint():
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.iconbitmap("C:/Users/admin/Desktop/Codeeee/Python projects/Paint app/paint.ico")
        self.root.geometry("800x520")
        self.root.configure(background = 'white')
        self.root.resizable(0,0)

        self.pen_color = 'black'

        self.color_frame = LabelFrame(self.root, text = 'Color', font = ('arial', 15), bd = 5, relief = RIDGE, bg = 'white')
        self.color_frame.place(x = 0, y = 0, width = 70, height = 185)

        colors = ['#ff0000','#ff4dd2', '#ffff33', '#000000', '#0066ff', '#660033', '#4dff4d', '#b300b3', '#00ffff', '#808080', '#99ffcc']
        i = j = 0

        for color in colors:
            Button(self.color_frame, bg = color, bd = 2, relief = RIDGE, width = 3, command  = lambda col = color:self.select_color(col)).grid(row = i, column = j)
            i+=1
            if i==6:
                i = 0
                j = 1

        self.eraser_button = Button(self.root, text = "Eraser", bd = 4, bg = 'white', command = self.eraser, width = 8)
        self.eraser_button.place(x = 0, y = 187)
        self.clear_button = Button(self.root, text = "Clear", bd = 4, bg = 'white', command = lambda: self.canvas.delete('all'), width = 8)
        self.clear_button.place(x = 0, y = 217)
        self.save_button = Button(self.root, text = "Save", bd = 4, bg = 'white', command = self.save_paint, width = 8)
        self.save_button.place(x = 0, y = 247)
        self.canvas_color_button = Button(self.root, text = "Color", bd = 4,  bg = 'white', command = self.color_choose, width = 8)
        self.canvas_color_button.place(x = 0, y = 277)

        # Creating a scale bar for pen nd eraser size
        self.pen_size_scale_frame = LabelFrame(self.root, text = 'Size', bd = 5, bg = 'white', font = ('arial', 15, 'bold'), relief = RIDGE)
        self.pen_size_scale_frame.place(x = 0, y = 310, height = 200, width = 70)


        self.pen_size = Scale(self.pen_size_scale_frame, orient = VERTICAL, from_ = 50, to = 0, length = 170)
        self.pen_size.set(1)
        self.pen_size.grid(row = 0, column = 0, padx = 15)

        # Creating Canvas
        self.canvas = Canvas(self.root, bg = 'white', bd = 5, relief = GROOVE, height = 500, width = 700)
        self.canvas.place(x = 80, y = 0)

        #Bind the canvas with mouse
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1,y1 = (event.x-2),(event.y-2)
        x2,y2 = (event.x+2),(event.y+2)

        self.canvas.create_oval(x1,y1,x2,y2, fill=self.pen_color, outline = self.pen_color, width=self.pen_size.get())

    def select_color(self, col):
        self.pen_color = col    

    def eraser(self):
        self.pen_color = 'white'    

    def color_choose(self):
        c = colorchooser.askcolor()     
        self.pen_color = c[1]

    def save_paint(self):
        try:
            filename = "C:/Users/admin/Desktop/1.jpg"    
            # print(filename)
            x = self.root.wininfo_rootx() + self.canvas.wininfo_x()
            y = self.root.wininfo_rooty() + self.canvas.wininfo_y()
            x1 = x + self.canvas.wininfo_width()
            y1 = y + self.canvas.wininfo_height()
            ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            # messagebox.shoinfo("Image is saved as "+str(filename))

        except:
            messagebox.showerror("Error!","Error occured while saving the file.")    


if __name__ == '__main__':
    root = Tk()
    P = Paint(root)
    root.mainloop()        