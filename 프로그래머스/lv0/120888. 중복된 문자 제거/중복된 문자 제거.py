# 방법 2
# dict.fromkeys(word)
# dict으로 변환 후 join 함수 사용 (파이썬 3.6부터 dict 순서 보장)
def solution(my_string):
    answer = ''.join(dict.fromkeys(my_string))
    return answer

# 방법 1
# for문으로 문자 하나하나 돌면서 if문에서 중복된 문자는 넣지 않는다.
# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer += i
#     return answer

# 방법 3
# 파이썬 3.6 이전엔 dict 순서 보장이 안됐기에 OrderedDict으로 변환 후 join 함수 사용
# def solution(my_string):
#     from collections import OrderedDict
#     answer = ''.join(dict.fromkeys(my_string))
#     return answer