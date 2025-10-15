students = []

while True:
    username = input("Username: ")
    if username.lower() == "done":
        break
    
    subjects = ["Math", "English", "Science"]
    scores = {}
    
    for subject in subjects:
        score = int(input(f"Enter {subject}: score "))   
        scores[subject] = score


    student_data = {"username": username, "score": scores}

    students.append(student_data)

for student in students:
    print(f"{student["username"]} has {scores} grade ")
print(students)


total = 0

for student in students:
    total += sum(student["score"].values())
    num_subjects = len(student["score"])  
    average = total / num_subjects 

print(total)
print(average)
print(student["score"])

#     sum += s["score"]
#     avg = sum / len(students)


# print(avg)
