def printfMistake(mes):
    print(mes)
    return mes
time = 3
while time > 0:
    name = "Mustafa Şamil"
    surname = "İleri"
    name_input = input("Name : ")
    surname_input = input("Surname :")
    if (name != name_input or surname != surname_input):
        time -= 1
    if (name_input == name and surname_input == surname):
        break
mes = "Please Try Again Later"
if (time == 0):
    printfMistake(mes)
else:

    print("Welcome")
    Course = []
    for x in range(5):
        x = input("Course :")
        Course.append(x)
    y = Course.count('')
    if len(Course) - y < 3:
        print("You Failed in class")

    print(" Your Courses")
    print(Course)
    print("Choose one Courses")
    chosse = input("")
    print(chosse)
    chosse = {'midterm': 0, 'final': 0, 'project': 0}
    chosse["midterm"] = int(input("midterm :"))
    chosse["final"] = int(input("final :"))
    chosse["project"] = int(input("project :"))

    grade = float((chosse.get("midterm") * 0.3) + (chosse.get("final") * 0.5) + (chosse.get("project") * 0.2))
    print(grade)
    if grade >= 90:
        print("AA")
    elif 70 <= grade and grade < 90:
        print("BB")
    elif 50 < grade and grade < 70:
        print("CC")
    elif 30 < grade and grade <= 50:
        print("DD")
    else:
        print("FF\nFailure")

