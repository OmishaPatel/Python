def get_sentence_split(s, words):
    if not s or not words:
        return []

    word_set = set(words)
    print(word_set)
    print("s: "+s)
    words_sentence = []
    for i in range(len(s)):
        if s[0:i+1] in word_set:
            print(s[0:i+1])
            words_sentence.append(s[0:i+1])
            print(words_sentence)
            word_set.remove(s[0:i+1])
            words_sentence += get_sentence_split(s[i+1:], word_set)
        print ("i: "+str(i))
            
    return words_sentence

print(get_sentence_split("thequickbrownfox", ['quick', 'brown', 'the', 'fox']))
