from tkinter import*

from tkinter import ttk, messagebox

from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        #=================title===============
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"),bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #================bg image===============
        img3 = Image.open(r"images\background.jpg")
        img3 = img3.resize((1530, 790), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=45, width=1530, height=710)
        #======================button===============
        b1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                    font=("times new roman", 25, "bold"), bg="white", fg="red")
        b1.place(x=500, y=380, width=530, height=60)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for  image in path:
            img=Image.open(image).convert('L') #Gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            #C:\Users\Lenovo\Desktop\face_recoginitionsystem\data\user.1.1.jpg

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13           #1 means enter 13 means close

        ids=np.array(ids)



        #===================== Train Classifier and save =======================

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")





if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()