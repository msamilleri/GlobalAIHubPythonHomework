import time
import sys

start=time.time()
name=input("Name : ")
surname=input("Surname :")
finis=time.time()
last=finis-start
if( last>3 and name=="" and surname==""):
 print("try again")
else:
 print("Welcome")
 StudentList=[]
 midtermgrade=input("mit term note :")
 StudentList.insert(0,"midterm")
 StudentList.insert(1, midtermgrade)
 StudentList.insert(2, "final")
 finalGrade=input("final note :")
 StudentList.insert(3, finalGrade)
 StudentList.insert(4, "Project")
 projectgrade=input("project note :")
 StudentList.insert(5, projectgrade)
 grade=float((float(StudentList[1])*0.3)+(float(StudentList[3])*0.5)+(float(StudentList[5])*0.2))

 if grade>90:
       print("AA")
 elif 70<grade and grade<90:
      print("BB")
 elif 50 < grade and grade < 70:
      print("CC")
 elif 30<grade and grade<50:
      print("DD")
 else:
      print("FF\nFailure")
