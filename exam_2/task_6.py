# Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце массива элементы заполнить нулями
def compress_array(arr, a, b):
    compressed_arr = [num for num in arr if num < a or num > b]
    compressed_arr += [0] * (len(arr) - len(compressed_arr))
    return compressed_arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 3
b = 7

compressed_arr = compress_array(arr, a, b)
print(compressed_arr)

