def partition(arr, low, high):
    # ใช้ค่าสุดท้ายเป็น pivot
    pivot = arr[high]
    i = low - 1  # ดัชนีของค่าน้อยกว่า pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # สลับค่าที่น้อยกว่า pivot ไปด้านซ้าย

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # นำ pivot ไปไว้ที่ตำแหน่งที่ถูกต้อง
    return i + 1  # คืนค่าดัชนีของ pivot

def quick_sort(arr, low, high):
    if low < high:
        # หา pivot และแบ่งอาร์เรย์
        pi = partition(arr, low, high)

        # เรียก quick_sort สำหรับส่วนซ้ายของ pivot
        quick_sort(arr, low, pi - 1)

        # เรียก quick_sort สำหรับส่วนขวาของ pivot
        quick_sort(arr, pi + 1, high)

# ตัวอย่างการใช้งาน
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Before sorting:", arr)
quick_sort(arr, 0, n-1)
print("After sorting:", arr)
