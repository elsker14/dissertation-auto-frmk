# transforms string from "word_example" to "wordExample"
def transformWord(word:str):
    result = ""

    splitted_words = word.split("_")
    i = 0
    # print(splitted_words)
    for splitted_word in splitted_words:
        if i > 0:
            result = result + splitted_word.capitalize()
        else:
            result = result + splitted_word
        i = i + 1

    return result
