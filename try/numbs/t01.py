import re

words = [
    "Abandonado, s[.] y adj[.]",
    "Abdicación, s[.]",
    "Abdomen, s[.]",
    "Aborígenes, s[.]",
    "Abrupto, adj[.]",
    "Absoluto, adj[.]",
    "Abstemio, s[.]",
    "Absurdo, s[.]",
    "Aburrido, adj[.]",
    "Academia, s[.]",
    "Accidente, s[.]",
    "Acéfalo, adj[.]",
    "Acorde, s[.]",
    "Acordeón, s[.]",
    "Acreedor, s[.]",
]

t, start, end = 0, 0, 1
with open("try/abc/A.txt", "r") as f:
    for _ in range(len(words)):
        text = ""
        for line in f:
            line = line.rstrip()
            a = re.search(rf"^{words[start]}", line)
            if a is not None:
                print(a)
                if t == 0:
                    span = a.span()
                    text += line[span[1] :]
                    if t < 1:
                        t += 1
                text += line
            try:
                b = re.search(rf"^{words[end]}", line)
                if b is None:
                    print(b)
                    text += line
                else:
                    break
            except IndexError:
                print(1)
                text += line
            print(text)
            text = ""
        start += 1
        end += 1
