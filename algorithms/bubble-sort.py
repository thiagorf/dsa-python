def bubbleSort(arr):
    steps = 0

    for i in range(len(arr)):
        # 0,1,2,3,4 = len(5)

        for j in range(0, len(arr) - i - 1):
            # i = 0
            # j in range(0, len(arr) - 0 - 1)
            # j in range(0, 5 - 0 - 1)
            # j in range(0, 4) = 0,1,2
            if arr[j] > arr[j + 1]:
                steps += 1
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                print("Step: %i" % steps)


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print(data)
