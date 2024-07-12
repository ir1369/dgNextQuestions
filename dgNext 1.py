def MatrixBinarySearch(matrix, target):
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    left = 0
    right = rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return (True, mid // cols, mid % cols)
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
