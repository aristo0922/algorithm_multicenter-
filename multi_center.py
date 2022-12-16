from collections import defaultdict
import numpy as np
import random

# https://velog.io/@guri_coding/알고리즘-스터디-최소신장트리MST-feat.-Python
# size_list * size_list 크기 배열 생성
size_list = 10

# 1 => data가 들어간 상태
# loc_list : located list, 배열에 데이터가 들어간 위치 정보 저장
loc_list = list()


def input_list(list_in):
    input_num = random.randrange(0, 100)
    input_x = random.randrange(0, size_list)
    input_y = random.randrange(0, size_list)
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

# located list를 이용해 길이 계산
# list[x1, y1] list[x2, y2]


def get_cost(x1, y1, x2, y2):
    x_cost = x2-x1
    y_cost = y2-y1
    cost = x_cost*x_cost + y_cost*y_cost
    cost /= cost
    return cost


# # find_num 이 위치한 index 찾기
# def find_index(list_in, loc_list, find_num):
#     x = 0
#     while True:
#         index_x = loc_list[x][0]
#         index_y = loc_list[x][1]
#         if list_in[index_x][index_y] == (find_num):
#             print("<<< ====  find! === >>>")
#             break
#         else:
#             x += 1
#             continue

# 입력값 초기화
array = [[0]*size_list for _ in range(size_list)]
input_num = int(input("입력할 정점의 개수를 입력하세요 >> "))
for i in range(input_num):
    array = input_list(array)
# test case
array[5][5] = 5
loc_list.append([5, 5])


class MST:
    def __init__(self, node):
        self.mst = defaultdict(list)
        self.mst[node]
        print("<<< === class init === >>>")
        print(self.mst)

    def insert_node(self, node, cost):
        self.mst[node].append(cost)


print("loc_ list shape >> ")

# mst = MST(array)
# mst 초ㄱl화
init_x = loc_list[0][0]
init_y = loc_list[0][1]
mst = MST(array[init_x][init_y])
print(array[init_x][init_y])


# array에 들어간 내용 확인
for i in range(size_list):
    print(array[i])

# cost 계산
index = 0
for index in range(len(loc_list)):
    try:
        a = np.array([loc_list[index][0], loc_list[index][1]])
        b = np.array([loc_list[index+1][0], loc_list[index+1][1]])
        cost = np.sqrt(np.sum(np.square((a-b))))
        index += 1
        print("<<< === cost === >>>")
        print(cost)
    except:
        break
