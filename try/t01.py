import re


def letter_picker():
    letters = list()
    """
     [
      'A', 'B', 'C', 'D', 'E', 'F',
      'G', 'H', 'I', 'J', 'K', 'L',
      'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'Y', 'Z' ->> 25 letters
     ]
    """
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


# BUG: Debug this file, there's and eternal loop.
# BUG: Debug this file, there is a repetition in the write part
#  #  DONE!! the text var is got to go blank again
# FIX: The last letter z is out of boundries


def search_words(letters):
    with open("src/edited_diabolous.txt", "r") as f:
        start, end = 0, 1
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
                        eof = re.search(r"nomber sagrados\.$", line, re.MULTILINE)
                        if eof is None:
                            text += line
                        else:
                            print(eof)
                            break
                    target.write(text)
                    text = ""
            start += 1
            end += 1


# print(letter_picker())

search_words(letter_picker())
