from rich import print

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [2, 5, 1, 6, 7, 3, 0]
print(f"[yellow]unsorting: [/yellow]{arr}")
insertion_sort(arr)
print(f"[green]sorting: [/green]{arr}")
