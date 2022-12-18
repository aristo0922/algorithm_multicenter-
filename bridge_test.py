# https://velog.io/@crosstar1228/pythondefaultdict-그래프-자료구조-변환할-때
# https://velog.io/@youngmin3841/백준-소풍시간초과
# https://dongdongfather.tistory.com/68
# https://lbdiaryl.tistory.com/219
# https://sarah950716.tistory.com/12
# https://kingpodo.tistory.com/46
# https://sarah950716.tistory.com/12
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    # 노드 삽입
    def insert_node(self, node, connected_node):
        self.graph[node].append(connected_node)
        self.graph[connected_node].append(node)

    # 브릿지 여부 판별
    def determine_bridge(self):
        while True:
            print("간선의 양 끝점을 입력하고 엔터를 누르세요--->")
            input1, input2 = map(int, input().split())
            if input2 in self.graph[input1]:
                print(str(input1)+"과 " + str(input2)+"는 브리지로 연결되었습니다.")
            else:
                print("두 노드는 연결되지 않았습니다.")
                break

    def get_items(self):
        return self.graph.items()


def call_insert_node(graph):
    while True:
        print('간선의 양 끝점을 입력하고 엔터를 누르세요:>')
        input1, input2 = map(int, input().split())
        if input1 == -1 & input2 == -1:
            break
        else:
            graph.insert_node(input1, input2)


graph = Graph()

call_insert_node(graph)

# lists = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 5], [5, 6], [5, 7], [7, 3], [-1, -1]]

print("그래프 노드 출력 >> ")
print(graph.get_items())

# 입력받은 두 양 끝점이 브리지인지 아닌지 판별하는 알고리즘
graph.determine_bridge()
