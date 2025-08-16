import matplotlib.pyplot as plt
from Random_array import array_sizes
from Class_MergeSort import MergeSort
from Class_QuickSort import QuickSort
from Class_HeapSort import HeapSort
import time

def run_sorting(sort_class, arr):
    sorter = sort_class()
    start = time.time()
    if isinstance(sorter, QuickSort):
        sorter.sort(arr)
    else:
        arr = sorter.sort(arr)
    end = time.time()
    return end - start, sorter.comparisons, sorter.moves

results = {}

for n in array_sizes:
    if n > 10**7:  # skip huge arrays if system is limited
        continue
    with open(f"arrays/array_{n}.txt") as f:
        arr = list(map(int, f.read().splitlines()))

    print(f"Sorting array of size {n}...")

    results[n] = {}
    for sort_name, sort_class in [("MergeSort", MergeSort), ("QuickSort", QuickSort), ("HeapSort", HeapSort)]:
        arr_copy = arr.copy()
        print(f"  Running {sort_name}...")
        t, comp, moves = run_sorting(sort_class, arr_copy)
        results[n][sort_name] = {"time": t, "comparisons": comp, "moves": moves}
        print(f"    Time: {t:.4f}s, Comparisons: {comp}, Moves: {moves}")

# Plot performance
for sort_name in ["MergeSort", "QuickSort", "HeapSort"]:
    times = [results[n][sort_name]["time"] for n in results]
    plt.plot(list(results.keys()), times, label=sort_name)
plt.xlabel("Array Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.show()
