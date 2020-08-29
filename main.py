import string

format_string = "Hello {:^25}, how are you? Is your last name {}?"
print(format_string.format("Duleepa", "Thrimawithana"))
print("")

template = string.Template(
    "Hello $first, how are you? Is your last name $last?")
print(template.substitute(first="Duleepa", last="Thrimawithana"))

number = int(input("Enter Number: "))
print(number == 50)

for i in range(0, 10):
    print(i, ' ', end='')
    if i == 5:
        break
print()
