diabolous = {
    "A": {"Alba": "Aorem Ipsum"},
    "B": {"Biron": "Borem Ipsum"},
    "C": {"Colon": "Corem Ipsum"},
    "N": {"Norem": "Norem Ipsum"},
}

word = input("What are you looking for?\n.. ").capitalize()
letter = word[0]
result = diabolous[letter][word]

print(result)
