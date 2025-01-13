def solution(s):

    s = s.lower()

    return True if s.count('p') == s.count('y') else False

input(solution('pPoooyY'))
input(solution('Pyy'))
