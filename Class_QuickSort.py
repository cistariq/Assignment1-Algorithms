class QuickSort:
    def __init__(self):
        self.comparisons = 0
        self.moves = 0

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.moves += 3  # counting swaps as 3 moves
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.moves += 3
        return i + 1

    def sort(self, arr, low=0, high=None):
        if high is None:
            high = len(arr) - 1
        if low < high:
            pi = self.partition(arr, low, high)
            self.sort(arr, low, pi - 1)
            self.sort(arr, pi + 1, high)
