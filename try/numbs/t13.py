""" 
 <- Goal ->
 Make a simplier program to test
 the functionality of a new algo wich
 implements the search of type and def.
 in the same func.
 <- Goal -> 
     ++
 <- Elements ->
 [ x ] Text with different patterns to extract:
 '''
     Hello world, s. y adj. Esto es un concepto
     muy conceptual.
     Hello world, adv. Esto es un concepto
     muy conceptual.
 '''
 [  ] ..
 <- Elements ->
"""

import re


# 1. extract letters
def pick_letters(text):
    pattern = "\n+([A-Z])\n*"
    letters = re.findall(pattern, text)

    return letters


# 2. extract words
def pick_words(text):
    patterns = "|".join(
        [
            "\n+([A-Z][\w]+), s[.] y adj[.]",
            "\n+([A-Z][\w]+), s[.]",
            "\n+([A-Z][\w]+), v[.]t[.]",
        ]
    )
    words = re.findall(patterns, text)
    words = [word for sublist in words for word in sublist if word]

    return words


# 3. extract type
def pick_types(text):
    patterns = "|".join(
        [
            "\n*[A-Z][\w]+, (s[.] y adj[.])",
            "\n*[A-Z][\w]+, (s[.])",
            "\n*[A-Z][\w]+, (v[.]t[.])",
        ]
    )

    types = re.findall(patterns, text)
    types = [typ for sublist in types for typ in sublist if typ]

    return types


# 4. extract definition
def define(words, text: str):
    """
    Structures the definitions.
    """
    # end, start = 1, 0
    # with open("t_src/edit.txt", "r") as f:
    #     # ->> preps
    #     file = f.read()
    #     lenght = range(len(picked))
    #     definitions = list()
    #     # ->> preps
    #     x = 0
    #     for s in lenght:
    #         start = s
    #         definition = dict()
    #         try:
    #             pattern = f"\n*{picked[start]}(.+)[\n.]{picked[end]}"
    #             match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
    #         except IndexError:
    #             match = re.findall(
    #                 f"\n*{picked[start]}(.+)", file, re.MULTILINE | re.DOTALL
    #             )
    #
    #         if len(match) > 0:
    #             definition[picked[start]] = match[0]
    #             definitions.append(definition)
    #             print("." * x)
    #             x += 1
    #         else:
    #             continue
    #         start += 1
    #         end += 1
    #
    #     return definitions


# 5? create dictionary
# 6. pass it to db


def go():
    text = """
A
Abba, s. y adj. Funcionario útil que con frecuencia diri-
ble que el asaltante de caminos.
B
Bag, v.t. Cocodrilo de América, superior, en todo, al
y haber crecido con los otros ríos.
C
Cagada, s. Prototipo de la puntuación. Ob-
serva Garvinus que los sistemas de puntuación usa-
ron"""

    letters = pick_letters(text)
    print(letters)
    words = pick_words(text)
    print(words)
    types = pick_types(text)
    print(types)


if __name__ == "__main__":
    go()
