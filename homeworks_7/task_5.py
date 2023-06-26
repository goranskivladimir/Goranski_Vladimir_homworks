#5)Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице
my_list = [0] * 100
my_list.insert(0, 1)
my_list.append(1)
print(my_list)
print(f'Кол-во нулей в списке my_list: {my_list.count(0)}')
