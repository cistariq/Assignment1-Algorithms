class HeapSort:
    def __init__(self):
        self.comparisons = 0
        self.moves = 0

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n:
            self.comparisons += 1
            if arr[l] > arr[largest]:
                largest = l

        if r < n:
            self.comparisons += 1
            if arr[r] > arr[largest]:
                largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.moves += 3
            self.heapify(arr, n, largest)

    def sort(self, arr):
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.moves += 3
            self.heapify(arr, i, 0)
