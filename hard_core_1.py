def change_word(begin_word, last_word, words_list):
    print("Begin: " + begin_word)
    print("Last: " + last_word)
    print(word_list)
    count = 0
    for word_aux in words_list:
        for i in range(len(word_aux)):
            if begin_word[i] != word_aux[i]:
                if word_aux[i] in last_word:
                    index = last_word.index(word_aux[i])
                    count += 1
                    begin_word = begin_word.replace(begin_word[i], last_word[index])
                    print(begin_word + '--> ', end="")
                else:
                    continue
            else:
                continue

            if begin_word == last_word:
                print("\nLenght", count)
            else:
                count += 1


word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
begin_word = "hit"
end_word = "cog"
change_word(begin_word, end_word, word_list)

