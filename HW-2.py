FirstName=input("First Name :")
LastName=input("Last Name :")
Age=int(input("Age :"))
BirthDate=int(input("Birth Day Year :"))
MyList=[]
MyList.insert(0,FirstName)
MyList.insert(1,LastName)
MyList.insert(2,Age)
MyList.insert(3,BirthDate)

for i in range(len(MyList)):
    print(MyList[i])

if(MyList[2]<18):
    print("You can't go out beacuse it's too dangerous")
else:
    print("You can go out to the street")