# marriage bereau registration form :

from tkinter import *

def details():
    print(f"Full Name : {name.get()}")
    print(f"Address : {address.get()}")
    print(f"City : {City.get()}")
    print(f"Gender : {Gender.get()}")
    print(f"Date of birth : {dob.get()}")
    print(f"Education : {education.get()}")
    print(f"Occupation : {occupation.get()}")
    print(f"Salary / month : {salary.get()}")      
    print(f"Adhar Number : {aadhar.get()}")
    

root = Tk()
root.geometry()

name = Label(root, text = "Name : ", font = " callibri 12 ").grid()  
address = Label(root, text = "Address : ", font = " callibri 12 ").grid()  
City = Label(root, text = "City : ", font = " callibri 12 ").grid()  
Gender = Label(root, text = "Gender : ", font = " callibri 12 ").grid()  
dob = Label(root, text = "Date of birth : ", font = " callibri 12 ").grid()  
education = Label(root, text = "Education : ", font = " callibri 12 ").grid()  
occupation = Label(root, text = "Occupation : ", font = " callibri 12 ").grid()  
salary = Label(root, text = "Salary : ", font = " callibri 12 ").grid()  
aadhar = Label(root, text = "Aadhar : ", font = " callibri 12 ").grid()

name = StringVar()
address = StringVar()
City = StringVar()
Gender = StringVar()
dob = StringVar()
education = StringVar()
occupation = StringVar()
salary = IntVar()
aadhar = IntVar()

name_entry = Entry(root , textvariable = name).grid(row = 0 , column = 1)
address_entry = Entry(root , textvariable = address).grid(row = 1 , column = 1)
City_entry = Entry(root , textvariable = City).grid(row = 2 , column = 1)
Gender_entry = Entry(root , textvariable = Gender).grid(row = 3 , column = 1)
dob_entry = Entry(root , textvariable = dob).grid(row = 4 , column = 1)
education_entry = Entry(root , textvariable = education).grid(row = 5 , column = 1)
occupation_entry = Entry(root , textvariable = occupation).grid(row = 6 , column = 1)
salary_entry = Entry(root , textvariable = salary).grid(row = 7 , column = 1)
aadhar_entry = Entry(root , textvariable = aadhar).grid(row = 8 , column = 1)

Button(text = "Submit",command  = details).grid()

root.mainloop()

            
            
            




            
          
          
          

          




