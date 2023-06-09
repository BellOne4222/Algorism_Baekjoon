# 4948 베르트랑 공준

# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

import math

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n+1, 2*n+1):
        if isPrime(i):
            cnt += 1
    print(cnt)

# 풀이 과정
# 이 문제를 풀기 위해서는 소수를 판별하는 법을 알고 있어야 한다.

# 소수란, 1과 자기자신을 제외한 나머지 수로 나누어 떨어지지 않는 수이다.

# 그래서 소수를 판별하는 가장 간단한 방법은

# 2부터 자기자신 - 1 까지 for문을 돌면서 나누어 떨어지는지 확인하는 것이다.

 

# 하지만, 모두 확인할 필요 없이 제곱근까지만 확인을 하면 된다.

 

# 그 이유는 약수들의 곱이 서로 대칭을 이루기 때문인데

# 예를 들어, 16이라는 수가 있을 때

# 16의 약수는 1, 2, 4, 8, 16이며

# 약수들의 곱으로 나타내면 (1, 16) (2, 8) (4, 4) (8, 2) (16, 1) 다섯쌍의 곱으로 나타낼 수 있다.

 

# 이렇게 제곱근 4x4를 기준으로 양 옆으로 대칭을 이루기 때문에 제곱근 까지만 검사를 하면 된다.

 

# 이를 이용해 n+1 ~ 2n 중 소수를 판별하여 출력하면 된다.

# 두 번째 방법

num = 123456*2+1
num_list = [1]*num
for i in range(1, num):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            num_list[i] = 0
            break

while True:
    n = int(input())
    
    if n == 0:
        break
    
    prime = 0
    for i in range(n+1, 2*n+1):
            prime += num_list[i]
    print(prime)

# 코드 설명

# 에라토스테네스의 체를 이용하되, 함수 생성이 아닌 시간을 단축시킬 방법이 필요하다.
# 이는 코드가 실행됨가 동시에 미리 입력될 수들까지의 소수를 미리 구한 뒤, 소수의 개수를 더해주어 소수의 개수를 구하는 것이다.
# 해당 문제는 123456까지라는 제한된 수가 존재하므로, 123456*2 + 1개의 인자가 1 인 리스트를 생성한다.
# (이때 첫 번째 리스트는 사용되지 않기 때문에 + 1을 하는 것이다.)

# num = 123456*2+1
# num_list = [1]*num​

# 첫 번째 for문에서 1부터 123456*2 까지 순회하며 소수를 찾는다.
# 1은 소수가 될 수 없으므로 넘어가고, 2부터 에라토스테네스의 체를 이용하여 두 번째 for문을 순회한다.
# 2부터 첫 번째 for문에서 전달받은 i의 제곱근 까지 순회하며, i가 자신의 수 이하의 숫자에 의해 나누었졌을 때 나머지가 0인 경우, 해당 인덱스의 값을 0으로 변경하고, for문을 탈출한다. 
# 이 때 해당 숫자가 소수인 경우, 해당 인덱스의 리스트 값은 여전히 1이다.
# while문을 통해 각 n을 입력받고, n이 0이 될 경우, while문을 멈춘다.

# while True:
#     n = int(input())
    
#     if n == 0:
#         break​

# 소수의 개수를 구하기 위해 prime 변수를 선언하고, n 초과 2n 이하의 소수 개수를 for문을 통해 구한 뒤, for문이 끝날 경우 prime 변수를 출력하여 값을 구한다.