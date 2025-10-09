intj = [2, 3, 5, 6, 8, 12, 53, 12, 20, 15, 25, 21]

print("First half")
for num in intj[:6]:
    print(num)

print("second half")
for num in intj[6:12]:
    print(num)

print("Even indices")
for num in intj[::2]:
    print(num)

print("Odd indicies")
for num in intj[1::2]:
    print(num)

print("Every third element")
for num in intj[3::3]:
    print(num)

print("reverse")
for num in intj[::-1]:
    print(num)