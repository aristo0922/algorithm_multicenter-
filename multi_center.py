import numpy as np
import random

array = [[0]*10 for _ in range(10)]

# 1 => data가 들어간 상태
# loc_list : located list, 배열에 데이터가 들어간 위치 정보 저장
loc_list = list()


def input_list(list_in):
    input_num = random.randrange(0, 100)
    input_x = random.randrange(0, 10)
    input_y = random.randrange(0, 10)
    if is_null(list_in[input_x][input_y]):
        list_in[input_x][input_y] = input_num
        loc_list.append([input_x, input_y])
        return list_in
    else:
        return input_list(list_in)


def is_null(node):
    if node == 0:
        return True
    else:
        return False

# a = np.array((1, 2, 3))
# b = np.array((4, 5, 6))

# dist = np.linalg.norm(a-b)

# print(dist)


input_num = int(input("입력할 정점의 개수를 입력하세요 >> "))

for i in range(input_num):
    array = input_list(array)
array[5][5] = 5
loc_list.append([5, 5])


def find_index(list_in, loc_list, find_num):
    x = 0
    while True:
        index_x = loc_list[x][0]
        index_y = loc_list[x][1]
        if list_in[index_x][index_y] == (find_num):
            print("<<< ====  find! === >>>")
            break
        else:
            x += 1
            continue


# let_array = np.array(array)
# print(array)
for i in range(10):
    print(array[i])
    print('-------------')

print(find_index(array, loc_list, 5))
