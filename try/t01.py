import re


def letter_picker():
    letters = list()
    with open("src/edited_diabolous.txt", "r") as f:
        print("Find the Letter.")
        pattern = re.compile(r"^[A-Z]\n")
        for line in f:
            match = re.search(pattern, line)
            if match:
                letters.append(line.strip())
            elif match is None:
                continue
            else:
                print("Not found")
    return letters


def search_words(letters):
    with open("src/edited_diabolous.txt", "r") as f:
        start, end = 0, 1
        for letter in range(0, len(letters)):
            text = """"""
            with open(f"try/abc/{letters[start]}.txt", "w") as target:
                for line in f:
                    a = re.search(rf"^{start}\n", line)
                    if a is not None:
                        print(a)
                        text += line
                    b = re.search(rf"^{end}\n", line)
                    if b is None:
                        text += line
                    else:
                        print(b)
                        break
                    target.write(text)
            start += letter
            end += letter


search_words(letter_picker())
