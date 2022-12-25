# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('homework20_1.txt') as f1:
    line1 = f1.read()

with open('homework20_2.txt') as f2:
    line2 = f2.read()


def replace_string_in_file(string_in_file):
    string = string_in_file.replace(" ", "").split("=")[0].split("+")
    return string


def get_multi_array(string_in_file):
    expression = {}
    for i in string_in_file:
        if i.isdigit():
            expression.setdefault(0, int(i))
        else:
            a, b = i.split("*x")
            degree = b.replace("^", "")
            if degree == "":
                degree = 1
            expression.setdefault(int(degree), int(a))
    return expression


def sum_expression(dist1, dist2):
    new_dist = {}
    for i in range(max(len(dist1), len(dist2))):
        if len(dist1) > len(dist2):
            new_dist[i] = dist1[i] + dist2.setdefault(i, 0)
        else:
            new_dist[i] = dist2[i] + dist1.setdefault(i, 0)
    return new_dist


def write_in_file(dist: dict):
    string = []

    with open('homework20_final.txt', 'w') as f:
        for k, v in dist.items():
            string.append(f'{v}*x^{k}')
        f.write((f'{" + ".join(string)} = 0'))
    return "Saved"


multi_string1 = replace_string_in_file(line1)
multi_string2 = replace_string_in_file(line2)

expression1 = get_multi_array(multi_string1)
expression2 = get_multi_array(multi_string2)

sum_expression = sum_expression(expression1, expression2)

print(write_in_file(sum_expression))
