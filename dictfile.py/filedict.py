def read_file():
    file = open('word.txt', 'r')
    dict1 = dict()
    for line in file:
        key = line.split(',')[0]
        #using strip to get rid of new line for value
        value = line.split(',')[1].strip()
        dict1[key] = value
    return dict1

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = key
        else:
            inverse[val].append(key)
    return inverse

def read_to_file(text_data):
    file2 = open('word1.txt','w')
    for key,value in text_data.items():
        file2.write(key+","+value+"\n")
    file2.close()

#Assigning the ouput of read_file function which is a dictionary from the text file to text_data 
text_data = read_file()
print('Original Dictionary' ,text_data)
text_data = invert_dict(text_data)
print('Inverted Dictionary' ,text_data)
print(read_to_file(text_data))

# for original dictionary i decided to split the word file at ',' to separate key and value pairs. For inverted dictionary i used .items() method of dictionary to loop over all items and write them to file
