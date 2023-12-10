import re

words = [
    "Abandonado, s. y adj.",
    "Abdicación, s.",
    "Abdomen, s.",
    "Aborígenes, s.",
]


def new_logic(words):
    end, start = 1, 0
    _ = input("!!Start!!")
    print(f"start, end \t\t ->> {start}|{end}")
    with open("try/abc/A1.txt", "r") as f:
        file = f.read()
        lenght = range(len(words))
        for s in lenght:
            start = s
            text = dict()
            try:
                pattern = rf"\n*{words[start]}(.+)\n*{words[end]}"
                match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
            except IndexError:
                match = re.findall(
                    rf"\n*{words[start]}(.+)", file, re.MULTILINE | re.DOTALL
                )

            if len(match) > 0:
                text[words[start]] = match[0]
                print(text)
            else:
                continue
            start += 1
            end += 1
        print(start, end)


new_logic(words)
