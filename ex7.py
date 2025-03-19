def studList():
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    for name in studentNames:
        print(f"{name} Evans")

def addToList(studentNames):
    new_name = input("Input names you will add：")
    studentNames.append(new_name)
    for name in studentNames:
        print(f"{name} Evans")

student_list = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
print("\nOriginal student list：")
studList()
print("\nThe list after added names：")
addToList(student_list)
