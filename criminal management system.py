from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class criminal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1270x680+0+0")
        self.root.title("CRIMINAL MANAGEMENT SYSTEM")
        
        #  main title=======

        main_title=Label(self.root,text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="gold")
        main_title.place(x=0,y=0,height=70,width=1400)



        # logo===
        '''
        img_logo=Image.open(file="jail1.webp")
        lbl=Label(self.root,image=img_pillu)
        lbl.place(x=5,y=5,relheight=1,relwidth=1)
        '''
        
       # main_title=Lable(root.self,text="CRIMINAL MANAGEMENT SYSTEM SOFTWARE",font=("times new roman",38,"bold"),bg="black",fg="gold")
        
        
        # main frame ======
        main_frame=Frame(self.root1,height=600,width=1300,bg="red",bd=2)
        main_frame.place(x=10,y=170)
        
        
        img1=Image.open("pillu.png")
        img1=img1.resize((),Image.ANTIALIAS)
        PhotoImg1=ImageTk.PhotoImage(img1)
        b1=Button(self,image=PhotoImg1,borderwidth=2)
        b1.place(x=5,y=5,width=300,height=400)
        
        
        
        
if __name__=="__main__" :
    root=Tk()
    obj=root
    root.mainloop()       
