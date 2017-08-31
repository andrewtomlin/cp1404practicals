
words_used = {}
text = input("Text: ")

all_words_used = text.split()
for word in all_words_used:
    frequency = words_used.get(word, 0)

    if frequency is None:
        words_used[word] = 1
    else:
        words_used[word] = frequency + 1


all_words_used = list(words_used.keys())

max_length = max((len(word) for word in all_words_used))
for word in all_words_used:
    print("{:{}} : {}".format(word, max_length, words_used[word]))