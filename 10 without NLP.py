def words_count(filename):
    with open(filename, "r") as file:
        texts = file.read()
        words = texts.split()
        total_words = len(words)
        return f"Total words in file :{total_words}"


num = words_count("input.txt")
print(num)
