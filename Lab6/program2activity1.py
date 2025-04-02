def word_count(sentence):
    words = sentence.split()
    word_freq = {}  

    for word in words:
        word = word.lower()  
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return len(words), word_freq


sentence = input("Enter a sentence: ")


total_words, frequency = word_count(sentence)


print(f"\nThe number of words in the sentence is: {total_words}")
print("Word frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")

   
