student = {
    "Name": "giorgi",
    "Age" : "19",
    "Course": "Web-Dev",
    "GPA": "3.5"
    ""
}

print(student)


student["Age"] = "20"
student["GPA"] = "3.0"

student["Lastname"] = "Gurgenidze"
student["Height"] = "6.1 feet"


print(student)

student.pop("Height")


for key, value in student.items():
    print(f"{key}, {value}")


