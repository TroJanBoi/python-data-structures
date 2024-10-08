from rich import print

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [2, 5, 1, 6, 7, 3, 0]
print(f"[yellow]unsorting: [/yellow]{arr}")
selection_sort(arr)
print(f"[green]sorting: [/green]{arr}")
