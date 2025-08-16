class MergeSort:
    def __init__(self):
        self.comparisons = 0
        self.moves = 0

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                self.moves += 1
                i += 1
            else:
                result.append(right[j])
                self.moves += 1
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        self.moves += len(left[i:]) + len(right[j:])
        return result

    def sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])
        return self.merge(left, right)
