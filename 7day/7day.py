# 문제: 백준 15829 Hashing

# 입력
# 첫 줄에는 문자열의 길이 L이 들어온다. 둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.

# 입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.

# 출력
# 문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.

L = int(input())  # 문자열의 길이
string = input().strip()  # 문자열 입력

r = 31
M = 1234567891
hash_value = 0

for i in range(L):
    char_value = ord(string[i]) - ord('a') + 1  # 문자 'a'는 1, 'b'는 2, ..., 'z'는 26
    hash_value = (hash_value + char_value * pow(r, i, M)) % M

print(hash_value)

