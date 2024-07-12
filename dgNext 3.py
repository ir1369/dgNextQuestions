def findLongestChain(lst):
    lst.sort()
    n = len(lst)
    i = 0 
    largestCounter = 0
    while i < n:
        counter = 1
        for j in range(1, n-i):
            if lst[i] == lst[i+j]-j:
                counter = counter+1
            else:
                if largestCounter<counter:
                    largestCounter=counter
                    largestSubSet = lst[i:i+largestCounter]
                break
        i = i + counter + 1
    return (largestCounter, largestSubSet)


