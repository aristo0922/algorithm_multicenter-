
import random

array = [[0]*10 for _ in range(10)]

# 1 => data가 들어간 상태


def input_list(list):
    input_x = random.randrange(0, 10)
    input_y = random.randrange(0, 10)
    if is_null(list[input_x][input_y]):
        list[input_x][input_y] = 1
        return list
    else:
        return input_list(list)


def is_null(node):
    if node == 0:
        return True
    else:
        return False


input_num = int(input("입력할 정점의 개수를 입력하세요 >> "))

for i in range(input_num):
    array = input_list(array)

for i in range(10):
    print(array[i])
    print('-------------')
