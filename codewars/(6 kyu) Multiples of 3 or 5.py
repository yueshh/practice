def solution(n):
    res = []
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)
    return sum(res) 
