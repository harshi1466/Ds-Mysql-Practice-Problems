def findPair(arr,sum):
    arr.sort()

    low,high=0,len(arr)-1

    while low<high:
        if arr[low]+arr[high]==sum :
            print(arr[low],arr[high])
            return
        elif arr[low]+arr[high]<sum:
            low=low+1
        else:
            high =high-1

    print("Not found")


arr=[8,3,5,7,2]
sum=15
findPair(arr,sum)