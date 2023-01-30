def selectionSort(arr):
    for step in range(len(arr)):
        minimum = step

        for i in range(step + 1, len(arr)):
            if arr[i] < arr[minimum]:
                minimum = i
        arr[step], arr[minimum] = arr[minimum], arr[step]


data = [20, 12, 10, 15, 2]

selectionSort(data)

print(data)
