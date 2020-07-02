arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]

for i in range(len(arr)):
    sum=0
    for j in range(i ,len(arr)):
        sum+=arr[j]

        if sum==0:
            print("Subarray from index {} to {}" .format(i,j))
