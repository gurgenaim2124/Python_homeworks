for i in range(1, 51):

    if i % 3 == 0:
        continue
    print(i)
    if i % 7 == 0 and i > 30:
        print(f"i found it {i}")
        break