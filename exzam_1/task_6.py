#6.В строке “Иван Иванов” поменяйте местами слова. Может быть предоставлена любая строка с именем и фамилией.
# например
# “Петр Иванов” => “Иванов Петр”
string = "Иван Иванов"
splitted_string = string.split()
reversed_string = splitted_string[::-1]
result = " ".join(reversed_string)
print(result)