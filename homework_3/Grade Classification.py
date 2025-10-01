grade = int(input("enter your score "))

if 90 <= grade and grade <= 100:
    print("A")
elif 80 <= grade and grade < 90:
    print("B")
elif 70 <= grade and grade < 80:
    print("C")
elif 60 <= grade and grade < 70:
    print("D")
elif grade < 60:
    print("F")
else:
    print("impossible")