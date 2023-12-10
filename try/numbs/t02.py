import re

words = [
    "Abandonado, s. y adj.",
    "Abdicación, s.",
    "Abdomen, s.",
    "Aborígenes, s.",
]


def new_logic(words):
    start, end = 0, 1
    with open("try/abc/A1.txt", "r") as f:
        file = f.read()
        lenght = range(len(words))
        print(lenght)
        for _ in lenght:
            text = dict()
            pattern = rf"\n*{words[start]}(.+)\n*{words[end]}"
            match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
            if len(match) > 0:
                text[words[start]] = match[0]
                print(text)
            else:
                continue
            start += 1
            end += 1
        print(start, end)


new_logic(words)
