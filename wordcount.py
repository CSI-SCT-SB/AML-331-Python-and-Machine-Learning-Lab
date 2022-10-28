def count(str):
    c={}
    words=str.split()
    for word in words:
        if word in c:
            c[word] += 1
        else:
            c[word] = 1

    return c
str=input("Enter the Sentence: ")
print(count(str))
