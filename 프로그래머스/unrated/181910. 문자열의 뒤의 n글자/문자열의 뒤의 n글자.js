function solution(my_string, n) {
    const str = my_string;
    var answer = str.substr(str.length - n);
    return answer;
}