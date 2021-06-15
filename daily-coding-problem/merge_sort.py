def merge_sort(arr):
    print("Splitting ", arr)
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
         
        #recursion
        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j+=1
            k = k+ 1

        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            arr[k] =righthalf[j]
            j+=1
            k+=1
    print("Merging ", arr)
    return arr

arr = [54,26,93,17,77,31,44,55,20]
        

print(merge_sort(arr))
# time complexity O(n log(n))
#space complexity O(n) as it needs additional space to produce a sorted list