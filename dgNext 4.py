def rangeMerge(lstTuples):
    sortedLstTuples = sorted(lstTuples, key=lambda x: x[0])
    finalLst = []
    n= len(lstTuples)
    i = 0
    
    while i < n:
        currentTuple = sortedLstTuples[i]
        print((i,currentTuple))
        counter = 1
        if i == n-1:
            finalLst.append(currentTuple)
            break
        while currentTuple[1] > sortedLstTuples[i+counter][0]:
            print(i+counter)
            if currentTuple[1] < sortedLstTuples[i+counter][1]:
                currentTuple=(currentTuple[0], sortedLstTuples[i+counter][1])
            if i + counter + 1 == n:
                break
            else:
                counter = counter+1
        finalLst.append(currentTuple)
        print(finalLst)
        i = i+counter
        print(i)
    return finalLst
