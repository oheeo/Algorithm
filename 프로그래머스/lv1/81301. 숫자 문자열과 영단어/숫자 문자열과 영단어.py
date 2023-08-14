# tmp 라는 임시 문자열을 담아둘 변수 선언
# isnumeric() : 문자열이 숫자인지 체크
def solution(s):
    answer = ""
    tmp = ""
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in s:
        if(i.isnumeric()):
            answer += i
        else:
            tmp += i
            if tmp in arr:
                answer += str(arr.index(tmp))
                tmp = ""
    return int(answer)