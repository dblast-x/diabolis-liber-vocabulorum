import re


def pick_words():
    """
    Creates a list with the extracted words.
    """
    with open("t_src/edit.txt", "r") as f:
        patterns = "|".join(
            [
                "(^[A-Z][\w]+), s[.] y adj[.]",
                "(^[A-Z][\w]+), adj[.] y s[.]",
                "(^[A-Z][\w]+), adj[.]",
                "(^[A-Z][\w]+), adv[.]",
                "(^[A-Z][\w]+), s[.]",
                "(^[A-Z][\w]+), v[.]t[.]",
                "(^[A-Z][\w]+), v[.]i[.]",
                "(^[A-Z][\w]+), v[.]r[.]",
            ]
        )
        pattern = re.compile(patterns)
        words = list()
        for line in f:
            line = line.rstrip()
            match = re.findall(pattern, line)
            if match:
                words.append(match)
            else:
                continue

        definitions_list = [
            alpha for sublist in words for word in sublist for alpha in word if alpha
        ]

        return definitions_list


def define(picked):
    """
    Structures the dictionary.
    """
    end, start = 1, 0
    with open("t_src/edit.txt", "r") as f:
        # ->> preps
        file = f.read()
        lenght = range(len(picked))
        definitions = list()
        # ->> preps
        x = 0
        for s in lenght:
            start = s
            definition = dict()
            try:
                pattern = f"\n*{picked[start]}(.+)[\n.]{picked[end]}"
                match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
            except IndexError:
                match = re.findall(
                    f"\n*{picked[start]}(.+)", file, re.MULTILINE | re.DOTALL
                )

            if len(match) > 0:
                definition[picked[start]] = match[0]
                definitions.append(definition)
                print("." * x)
                x += 1
            else:
                continue
            start += 1
            end += 1

        return definitions


# print(pick_types())
print(define(pick_words()))
