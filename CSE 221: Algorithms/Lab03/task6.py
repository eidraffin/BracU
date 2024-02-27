# Task 6
def PARTITION(A, low, high):
    x = A[high]
    i = low - 1
    for j in range(low, high):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

def kthSmallest(arr, low, high, k):
    if (k > 0) and k <= (high - low + 1):
        pos = PARTITION(arr, low, high)
        # Check if the position of the pivot is the kth smallest 
        if (pos - low) == (k - 1):
            return arr[pos]
        # If the kth smallest element is in the left subarray
        elif (pos - low) > (k - 1):
            return kthSmallest(arr, low, pos - 1, k)
        # Check the right subarray also
        else: 
            return kthSmallest(arr, pos + 1, high, k - pos + low - 1)
    return None


if __name__ == "__main__":
    with open("input6.txt", "r") as file_in:
        lines = file_in.readlines()
        high = int(lines[0][0]) - 1
        loop = int(lines[2][0])
        arr = lines[1].split()
        for i in range(len(arr)):
            arr[i] = int(arr[i].strip())

    with open("output6.txt", "w") as file_out:
        for i in range(loop):
            k = int(lines[i + 3].strip())
            file_out.write(str(kthSmallest(arr, 0, high, k)) + "\n")