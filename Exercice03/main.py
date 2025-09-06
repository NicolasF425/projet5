words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

liste = []
for word in words:
    nb_letters = 0
    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "y"]:
            nb_letters += 1
    liste.append((word, nb_letters))

print(liste)
