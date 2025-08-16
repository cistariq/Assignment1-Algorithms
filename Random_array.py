import random
import time
import os

array_sizes = [10**3, 10**5, 10**7]  # adjust last size if needed
output_folder = "arrays"
os.makedirs(output_folder, exist_ok=True)

for n in array_sizes:
    print(f"Generating array of size {n}...")
    arr = [random.randint(1, n) for _ in range(n)]
    with open(f"arrays/array_{n}.txt", "w") as f:
        f.write("\n".join(map(str, arr)))
    print(f"Array {n} saved.")
