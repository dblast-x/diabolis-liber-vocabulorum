import re
from os import mkdir


def letter_picker():
    letters = list()
    #  25 letters
    """
      'A', 'B', 'C', 'D', 'E', 'F',
      'G', 'H', 'I', 'J', 'K', 'L',
      'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'Y',
      'Z'.
    """
    with open("src/edit.txt", "r") as f:
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
    with open("src/edit.txt", "r") as f:
        start, end = 0, 1
        mkdir("try/abc")
        for letter in range(0, len(letters)):
            text = ""
            with open(f"try/abc/{letters[letter]}.txt", "w") as target:
                for line in f:
                    a = re.search(rf"^{letters[start]}\n", line)
                    if a is not None:
                        print(a)
                        text += line
                    try:
                        b = re.search(rf"^{letters[end]}\n", line)
                        if b is None:
                            text += line
                        else:
                            print(b)
                            break
                    except IndexError:
                        text += line
                    target.write(text)
                    text = ""
            start += 1
            end += 1


if __name__ == "__main__":
    search_words(letter_picker())
