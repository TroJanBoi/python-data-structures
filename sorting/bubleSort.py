from rich import print

def bubble_sort(arr):
    nbr = len(arr)
    for i in range(nbr):
        swap = False
        for j in range(0, nbr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break


arr = [2, 5, 1, 6, 7, 3, 0]
print(f"[yellow]unsorting: [/yellow]{arr}")
bubble_sort(arr)
print(f"[green]sorting: [/green]{arr}")
