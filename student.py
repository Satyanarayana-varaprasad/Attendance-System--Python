from tkinter import*

from tkinter import ttk, messagebox

#from PIL import Image,ImageTk

from PIL import Image,ImageTk
import cv2
import mysql.connector
class Student:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recogniton System")

        #variables...
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        # first image
        img = Image.open(r"images\rv1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # 2nd image
        img1 = Image.open(r"images\rv.jpg")
        img1 = img1.resize((225, 225), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # 3rd image
        img2 = Image.open(r"images\rv2.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image
        img3 = Image.open(r"images\1.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # text
        title_lbl = Label(bg_img, text="Student Details", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=20,y=50,width=1480,height=600)

        #left frame
        Left_frame =LabelFrame(main_frame, bd =2, bg="white", relief = RIDGE, text = "Student Details",font=("times new roman", 15, "bold"),
                           fg="blue")
        Left_frame.place(x = 10, y = 10, width = 730, height = 580)

        img_left= Image.open(r"images\1.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left= ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #current course
        # left frame
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course",
                                font=("times new roman", 15, "bold"),fg="blue")
        current_course_frame.place(x=5, y=135, width=720, height=150)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman", 12, "bold"),bg="yellow")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12, "bold"),state="read only")
        dep_combo["values"]=("Select Department","MCA","CSE","IT","ECE","EEE","MECH")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"), bg="yellow")
        course_label.grid(row=0, column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), state="read only")
        course_combo["values"] = ("Select Course", "ST", "MAD", "CS", "ADA", "C", "Python","Java","OS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10,sticky=W)

        #Year

        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"), bg="yellow")
        year_label.grid(row=1, column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="read only")
        year_combo["values"] = ("Select Year", "2021", "2020", "2019", "2018", "2017")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10,sticky=W)

        #SEmester

        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="yellow")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), state="read only")
        semester_combo["values"] = ("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4", "Sem-5","Sem-6")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information System",
                                          font=("times new roman", 15, "bold"), fg="blue")
        class_Student_frame.place(x=5, y=250, width=720, height=300)

        #studentid
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman", 13, "bold"))
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_ID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman", 13, "bold"))
        student_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # studentName
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"))
        studentName_label.grid(row=0, column=2, padx=10,pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5,sticky=W)

        # class divison
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 13, "bold"))
        class_div_label.grid(row=1, column=0, padx=10,pady=5, sticky=W)

        # class_div_entry = ttk.Entry(class_Student_frame,textvariable=self.var_div, width=20, font=("times new roman", 13, "bold"))
        # class_div_entry.grid(row=1, column=1, padx=10,pady=5, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div,
                                  font=("times new roman", 12, "bold"), state="read only")
        div_combo["values"] = ("Select Division", "A", "B", "C")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        #USN
        roll_no_label = Label(class_Student_frame, text="USN:", font=("times new roman", 13, "bold"))
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll, width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        #Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender,
                                  font=("times new roman", 12, "bold"), state="read only")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # gender_entry = ttk.Entry(class_Student_frame, textvariable=self.var_gender,width=20, font=("times new roman", 13, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #Dob:
        dob_label = Label(class_Student_frame, text="Date Of Birth:", font=("times new roman", 13, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #EmaIL
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 13, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        #Phone
        phone_label = Label(class_Student_frame, text="Phone Number:", font=("times new roman", 13, "bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame,textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        #Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        #Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"))
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)


    #Radio
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)


        radiobtn2 = ttk.Radiobutton(class_Student_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,font=("times new roman", 12, "bold"), bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=18, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        take_photo_btn = Button(btn_frame,command=self.generate_dataset, text="Take Photo Sample", width=18, font=("times new roman", 12, "bold"), bg="green", fg="white")
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=18, font=("times new roman", 12, "bold"), bg="green", fg="white")
        update_photo_btn.grid(row=1, column=3)















        # Right label frame
        Right_frame = LabelFrame(main_frame, bd = 2, bg = "white", relief = RIDGE,
                                 text = "Student Details",font=("times new roman", 15, "bold"), fg="blue")
        Right_frame.place(x=750,y=10,width=720,height=580)
        #image
        img_right = Image.open(r"images\1.jpg")
        img_right = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #Search System......................
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System",
                                         font=("times new roman", 15, "bold"), fg="blue")
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"),bg="red",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), state="read only")
        search_combo["values"] = ("Select", "USN", "Phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=16, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue",fg="white")
        search_btn.grid(row=0, column=3,padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue",fg="white")
        showAll_btn.grid(row=0, column=4,padx=4)


        #table frame...............

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","dob","gender","email","phone","address","teacher","photo"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="Date Of Birth")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone Number")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_dep.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="new_schema")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()

                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student Details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

        #fecting details from mysql...
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="new_schema")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #===========get cursor==================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


        #=================update function__________________
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_dep.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do You want to update this student details",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="new_schema")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get(),

                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==========================delete========================
    def delete_data(self):
        if self.var_std_id.get=="":
            messagebox.showerror("Error","student Id must required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do You Really Want to Delete",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="new_schema")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




    #================reset=============================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #==================Generate data set or Take Photo Sample===================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_dep.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="12345", database="new_schema")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dept=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",
                                                                                                                                                                                                            (
                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                            self.var_std_id.get()==id+1

                            ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()



                #============Load predefined data on face====================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #=======scaling factor=======1.3
                    #Minimum Neighbour============5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGRA2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets Completed!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)









if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()