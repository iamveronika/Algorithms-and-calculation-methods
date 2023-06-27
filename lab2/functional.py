def heapify(array_a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array_a[i] < array_a[left]:
        largest = left
    if right < n and array_a[largest] < array_a[right]:
        largest = right

    if largest != i:
        array_a[i], array_a[largest] = array_a[largest], array_a[i]  # swap
        heapify(array_a, n, largest)


def heapsort(array_a):
    n = len(array_a)

    # max-heap
    for i in range(n, -1, -1):
        heapify(array_a, n, i)

    for i in range(n-1, 0, -1):
        array_a[i], array_a[0] = array_a[0], array_a[i]  # swap
        heapify(array_a, i, 0)
