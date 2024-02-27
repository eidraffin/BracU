#Task 2a (Logarithmic)
def mergeSort(A, B):
    C = list()
    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    C.extend(A[i:])
    C.extend(B[j:])
    return C

#Task 2b (Linear)
def mergeSortLinear(A, B):
    C = list()
    i, j  = 0, 0

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < len(A):
        C.append(A[i])
        i += 1

    while j < len(B):
        C.append(B[j])
        j += 1

    return C


if __name__ == '__main__':
    #Tester code: Task 2a
    with open('input2a.txt', 'r') as filein:
        lines = filein.readlines()
        N = int(lines[0])
        alice = list(map(int, lines[1].split()))
        M = int(lines[2])
        bob = list(map(int, lines[3].split()))

    with open('output2a.txt', 'w') as fileout:
        fileout.write(' '.join(map(str, mergeSort(alice, bob))))

    #Tester code: Task 2b
    with open('input2b.txt', 'r') as filein:
        lines = filein.readlines()
        N = int(lines[0])
        alice = list(map(int, lines[1].split()))
        M = int(lines[2])
        bob = list(map(int, lines[3].split()))

    with open('output2b.txt', 'w') as fileout:
        fileout.write(' '.join(map(str, mergeSortLinear(alice, bob))))