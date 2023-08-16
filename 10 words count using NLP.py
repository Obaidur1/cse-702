from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")


def count_words(file_name):
    with open(file_name, "r") as file:
        text = file.read()

    words = word_tokenize(text)
    print(words)
    word_count = len(words)
    return word_count


file_name = "input.txt"
word_count = count_words(file_name)
print(f"Total words in the file:{word_count}")
