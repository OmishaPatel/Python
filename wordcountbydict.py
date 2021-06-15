text = input("enter a file name: ").split()
d = dict()
for word in text:
    print(word)
    d[word] = d.get(word,0) +1
print(d)
count = -1
word = None
for k,v in d.items():
    if v > count:
        count = v
        word = k
print("Word", word, "Repeats", count)
    
