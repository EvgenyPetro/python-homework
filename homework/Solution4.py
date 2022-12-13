# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("enter number quarter "))

value = {
    1: "X=(0, ∞),Y=(0, ∞)",
    2: "X=(-∞, 0),Y=(0, ∞)",
    3: "X=(-∞, 0), Y=(-∞,0)",
    4: "X=(0, ∞), Y= (-∞, 0)"}

if quarter in value:
    print(value[quarter])
else:
    print("error")
