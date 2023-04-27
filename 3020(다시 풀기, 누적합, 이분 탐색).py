# 3020 개똥벌레

# 참고 : https://hongcoding.tistory.com/6

# 문제
# 개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다. 동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수) 첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.

# 아래 그림은 길이가 14미터이고 높이가 5미터인 동굴이다. (예제 그림)



# 이 개똥벌레는 장애물을 피하지 않는다. 자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.

# 위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. (4번째 구간은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)



# 하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.

# 동굴의 크기와 높이, 모든 장애물의 크기가 주어진다. 이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 H가 주어진다. N은 항상 짝수이다. (2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000)

# 다음 N개 줄에는 장애물의 크기가 순서대로 주어진다. 장애물의 크기는 H보다 작은 양수이다.

# 출력
# 첫째 줄에 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 공백으로 구분하여 출력한다.

# 이진 탐색

n, h = map(int, input().split())

down = []
up = []
for i in range(n):
    if i % 2 == 0:
        down.append(int(input()))
    else:
        up.append(int(input()))

down.sort()
up.sort()

min_count = n
range_count = 0


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start


for i in range(1, h + 1):
    down_count = len(down) - binary_search(down, i - 0.5, 0, len(down) - 1)
    top_count = len(up) - binary_search(up, h - i + 0.5, 0, len(up) - 1)

    if min_count == down_count + top_count:
        range_count += 1
    elif min_count > down_count + top_count: # 현재 범위가 새로운 최소 값이면
        range_count = 1
        min_count = down_count + top_count

print(min_count, range_count)

# 접근 방법

# 가장 먼저 떠오른 방법은 석순과 종유석의 배열을 따로 두고, 각각의 배열을 정렬 한 후에 처음 개똥벌레가 부딪히기 시작한 높이를 계산하는 방식이다. 왜냐하면 그 이후의 구간은 모두 부딪힌다는 이야기가 되기 때문에 첫 구간만을 구해 그 구간 전까지의 개수를 통해 답을 구할 수 있기 때문이다. 이러한 접근 방식을 누적 합(또는 구간합)이라고 하는데

# 현재 페이지에서는 다른 방식으로 풀어보려고 한다.

 

# 바로 이진탐색(Binary Search) 방식으로 풀려고 한다.

# 석순과 종유석의 배열이 각각 정렬되어 있기 때문에, 배열의 중간지점에서 개똥벌레가 부딪히는지 테스트를 진행한다.

# 보통의 이진탐색 과정과 마찬가지로 start값과 end값에 변화를 주며 mid값을 조정하여 개똥벌레가 최소한으로 부딪히는 구간을 찾으면 된다.

# binary_search함수의 target은 개똥벌레의 높이가 되며 down일 때는 i - 0.5, up일때는 h - i + 0.5를 넣는다.

# 위에서 자라는 종유석의 경우에는 아래와는 반대로 생각해야 하기 때문이다.


# 누적합

n, h = map(int, input().split())

down = [0] * (h + 1)  # 석순
up = [0] * (h + 1)  # 종유석

min_count = n  # 파괴해야 하는 장애물의 최소값
range_count = 0  # 최소값이 나타나는 구간의 수

for i in range(n):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(h - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

for i in range(1, h + 1):

    if min_count > (down[i] + up[h - i + 1]):
        min_count = (down[i] + up[h - i + 1])
        range_count = 1
    elif min_count == (down[i] + up[h - i + 1]):
        range_count += 1

print(min_count, range_count)

# 접근 방법
# 이 문제를 누적합 (전위합(Prefix Sum)) 으로 다시 풀었다.

# 높이 h부터 높이 1까지 누적 합을 계산하면 높이 i의 배열 값은 높이 i 이상의 모든 석순의 개수가 된다.

# 예를 들어, 높이가 6인 동굴에서 높이 5의 개똥벌레가 날아갈 때, 높이 5 이상의 석순에 모두 부딪히기 때문에

# 배열 5의 값이 높이 5의 개똥벌레가 부딪히는 석순의 개수가 된다.

 

# 마찬가지로 종유석은 위에서부터 내려오기 때문에 h - i + 1의 식을 이용하면 된다.

# 왜냐하면, 높이 6의 동굴에서 높이 2짜리 종유석은 높이 4 (실질적으로 3.5) 위로의 개똥벌레가 모두 부딪히기 때문이다.

# 즉, 석순처럼 높이2라고 해서 높이 2 밑의 개똥벌레가 부딪히는것이 아니라 위에서 부터기 때문에 반대가 된다.

# 누적합 2

import sys

n,h = map(int,sys.stdin.readline().split(" "))
side_even = [0] * h
side_odd = [0] * h
for i in range(0,n):
    k = int(sys.stdin.readline())
    if i % 2 == 0:
        side_even[k-1] += 1
    else:
        side_odd[k-1] += 1
for i in range(h-1,0,-1):
    side_odd[i-1] += side_odd[i]
    side_even[i-1] += side_even[i]

minn = 200001
ans = 0

for i in range(0,h):
    t = side_even[i] + side_odd[h - 1 - i]
    if t < minn:
        minn = t
        ans = 0
    if t == minn:
        ans += 1
print(minn , end=" ")
print(ans)

# 풀이

# 동굴에 종유석과 석순이 있고 개똥벌레가 날아갈 때 , 부수는 종유석과 석순 개수의 최솟값을 구하고 그러한 구간이 얼마나 있는지 구하는 문제이다.
# N,H의 범위가 2 ≤ N ≤ 200,000, 2 ≤ H ≤ 500,000 이므로 , 한줄 한줄 따라가며 계산하면 시간초과가 날 것이다.
# 종유석의 길이가 4 라면 , 4 3 2 1 구간은 모두 부숴야할 종유석이 +1 되고 , 석순도 거꾸로 보면 같다.
# 따라서 종유석과 석순 리스트를 구분하고 각각을 길이에 대해 누적합을 계산한다.
# 이후 만들어진 두 누적합 리스트를 같은 구간들끼리 더해주어 최종 정답을 구해낸다.
# 아래의 그림은 개똥벌레 문제의 1번 예시의 누적합을 알아보기 위한 예시 그림이다.