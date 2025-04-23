---

## 단일 연결리스트(Singly Linked List)란?

단일 연결리스트는 각 요소(노드)가 데이터와 다음 노드를 가리키는 포인터(참조)를 가지고 한 줄로 연결된 선형 자료구조다. 리스트의 시작점은 *헤드(Head)*라고 하며, 마지막 노드는 다음 노드가 없는 상태(`None`)로 표시된다.
즉, 각 노드는 `[Data | Next]` 형태로 연결되어 있다.

### 구조

- **Node(노드)**: 데이터를 저장하고, 다음 노드를 가리키는 포인터를 가진 객체
- **Head(헤드)**: 연결리스트의 시작 노드
- **Tail(테일)**: 마지막 노드(보통 구현에 따라 관리할 수도 있음)


### 특징

- **연속된 메모리 공간**에 저장하지 않고, 각 노드가 다음 노드의 위치를 참조한다.
- **삽입/삭제**가 리스트 중간에서도 효율적으로 가능하다(특정 위치를 찾는 데는 순차 접근 필요).
- **임의 접근(random access)**이 느리다(처음부터 차례로 접근해야 함).

---

## 파이썬으로 단일 연결리스트 구현

### 1. Node 클래스

```python
class Node:
    def __init__(self, data):
        self.data = data      # 데이터 저장
        self.next = None      # 다음 노드 참조
```

각 노드는 자신의 데이터와 다음 노드를 가리키는 `next` 포인터를 가진다.

### 2. LinkedList 클래스

```python
class LinkedList:
    def __init__(self):
        self.head = None      # 첫 번째 노드(헤드)
        self.size = 0         # 노드의 개수

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.size += 1

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -&gt; ")
            cur = cur.next
        print("None")
```

- `append`: 리스트 끝에 노드 추가
- `print_list`: 리스트 전체 출력[^3_7][^3_11]


### 3. 주요 연산 예시

- **맨 앞에 노드 추가(appendleft)**
새로운 노드를 만들어 `head` 앞에 붙이고, `head`를 새 노드로 변경한다.
- **중간/끝 노드 삭제**
이전 노드를 따라가면서 삭제할 노드를 찾아 연결을 끊는다.
- **검색, 길이 반환, 값 포함 여부 검사**
순차 탐색을 통해 구현한다.

---

## 단일 연결리스트의 장단점

| 장점 | 단점 |
| :-- | :-- |
| 중간 삽입/삭제가 빠름 | 임의 접근이 느림(순차 탐색 필요) |
| 메모리 효율적(필요할 때만 생성) | 노드마다 포인터 저장(메모리 약간 더 사용) |
| 크기 제한 없음 | 마지막 노드 삭제 등은 처음부터 순회 필요 |


---

## 예시 코드

```python
# Node와 LinkedList 클래스 정의는 위와 동일

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.print_list()  # 10 -&gt; 20 -&gt; 30 -&gt; None
```

이 코드를 실행하면, 노드가 순서대로 연결되어 출력된다.

---

## 요약

- 단일 연결리스트는 각 노드가 데이터와 다음 노드를 가리키는 포인터를 가진 선형 자료구조다.
- 파이썬에서는 클래스를 이용해 직접 구현할 수 있다.
- 삽입/삭제가 리스트 중간에서도 효율적이지만, 임의 접근은 느리다.
