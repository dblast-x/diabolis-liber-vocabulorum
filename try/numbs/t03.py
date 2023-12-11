# # dict list dict list
# lll = [{"hey": 1}, {"hey": 2}]
#
#
# # A none initial value is valid.
#
# letters = ["a", "b", "c", "d"]
#
# definition = dict()
# for letter in letters:
#     definition[letter] = None
#     for x in range(4):
#         definition[letter] = x

# Empty dict as element

# dictionary = dict()
# for letter in range(4):
#     dictionary[letter] = {}
#     print(dictionary)
#
# comprehension dict?
#
# letters = ["A", "B", "C"]
# dictionary = {l: {} for l in letters}
# print(dictionary)
#
# This test
letters = ["A", "B"]
definition = [
    {"Ard": "example 1"},
    {"Ard1": "example 2"},
    {"Ard3": "example 3"},
    {"Brd": "example 1"},
    {"Brd3": "example 3"},
]


def make_dict(letters, definitions):
    dictionary = {letter: {} for letter in letters}
    for definition in definitions:
        for key, value in definition.items():
            key_letter = key[0]
            if key_letter in dictionary:
                dictionary[key_letter].update({key: value})
            else:
                print(f"'{key_letter}' Not found")

    print(dictionary)


make_dict(letters, definition)
