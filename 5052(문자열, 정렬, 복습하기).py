# 5052 전화번호 목록

# 문제
# 전화번호 목록이 주어진다. 이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.

# 전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

# 예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자

# 긴급전화: 911
# 상근: 97 625 999
# 선영: 91 12 54 26
# 이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다. 전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다. 따라서, 이 목록은 일관성이 없는 목록이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 t가 주어진다. (1 ≤ t ≤ 50) 각 테스트 케이스의 첫째 줄에는 전화번호의 수 n이 주어진다. (1 ≤ n ≤ 10000) 다음 n개의 줄에는 목록에 포함되어 있는 전화번호가 하나씩 주어진다. 전화번호의 길이는 길어야 10자리이며, 목록에 있는 두 전화번호가 같은 경우는 없다.

# 출력
# 각 테스트 케이스에 대해서, 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    call = [str(sys.stdin.readline().strip()) for _ in range(n)] # 전화번호를 문자열로 받는다.
    call.sort() # 오름차순으로 정렬하여 사전순으로 정렬
    chek = "yes" # 일관성이 있는지 체크

    # 반복문을 통해 전화번호를 확인
    for i in range(len(call) - 1):

        # 현재 전화번호의 문자열과 다음 전화번호의 현재 전화번호 길이만큼의 문자열과 같은지 확인
        # 같으면 일관성이 없는 것
        if call[i] == call[i + 1][0:len(call[i])]:
            chek = "no"

    if chek == "no":
        print("NO")
    else:
        print("YES")

# 알고리즘
# - 테스트 케이스만큼 반복한다.

# - 전화번호를 문자열로 입력받아 오름차순으로 정렬한다.(사전순으로 정렬)

# - 반복문을 통해 전화번호를 확인한다.

# - 현재 전화번호의 문자열과 다음 전화번호의 현재 전화번호 길이만큼의 문자열을 비교한다.

# - 같으면 일관성이 없는 것이고 다르면 일관성이 있는 것이다.