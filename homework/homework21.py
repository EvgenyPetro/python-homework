# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "абвук щывщьщбдф ывфапы опаполабв фыввабввап абвпапьщл"

text = text.split(" ")
new_text = []
for s in text:
    if "абв" not in s:
        new_text.append(s)
print(" ".join(new_text))
