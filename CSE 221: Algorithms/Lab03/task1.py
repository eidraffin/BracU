# Task 1
def MERGE_SORT(A, low, high):
    if low < high:
        mid = (low + high) // 2
        MERGE_SORT(A, low, mid)
        MERGE_SORT(A, mid+1, high)
        MERGE(A, low, mid, high)
    return A

def MERGE(A, low, mid, high):
    i = low
    j = mid + 1
    k = low
    temp = [None] * len(A)
    while i <= mid and j <= high:
        if A[i] < A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1

    while j <= high:
        temp[k] = A[j]
        j += 1
        k += 1

    for k in range(low, high + 1):
        A[k] = temp[k]


if __name__ == "__main__":
    with open('input1.txt', 'r') as file_in:
        lines = file_in.readlines()
        N = int(lines[0])
        A = list(map(int, lines[1].split()))

    with open("output1.txt", "w") as file_out:
        file_out.write(" ".join([str(i) for i in MERGE_SORT(A, 0, N - 1)]))