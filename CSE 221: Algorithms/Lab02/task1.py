#Task 1a (Quadratic)
def findSum(N, S, arr):
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == S:
                return f"{i+1} {j+1}"
    return "IMPOSSIBLE"

#Task 1b (Linear)
def findSumLinearly(N, S, arr):
    hash = dict()
    for i in range(N):
        key = S - arr[i]
        if key in hash:
            return f"{hash[key]} {i+1}"
        hash[key] = i+1
    return "IMPOSSIBLE"


if __name__ == '__main__':
    #Tester code: Task 1a
    with open('input1a.txt', 'r') as filein:
        lines = filein.readlines()
        N, S = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))

    with open('output1a.txt', 'w') as fileout:
        fileout.write(findSum(N, S, arr))

    #Tester code: Task 1b
    with open('input1b.txt', 'r') as filein:
        lines = filein.readlines()
        N, S = map(int, lines[0].split())
        arr = list(map(int, lines[1].split()))

    with open('output1b.txt', 'w') as fileout:
        fileout.write(findSumLinearly(N, S, arr))