
A = [1, -2, -3, 4]


def find_max_crossing_subarray(a, mid):

    sum = 0
    left_sum = 0
    max_left = None
    for i in range(mid, -1, -1):
        sum += a[i]

        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    right_sum = 0
    max_right = None
    for j in range(mid+1, len(a), 1):
        sum += a[j]

        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_max_subarray(a, low, high):

    # base case
    if low == high:
        return low, high, a[low]

    else:
        mid = (low + high) // 2

        left_low, left_high, left_sum = find_max_subarray(a, low, mid)

        right_low, right_high, right_sum = find_max_subarray(a, mid+1, high)

        cross_low, cross_high, cross_sum = find_max_crossing_subarray(a, mid)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum

        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum

        else:
            return cross_low, cross_high, cross_sum


def kadane(numbers):
    best_sum = 0
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


print(find_max_subarray(A, 0, len(A)-1))
print(kadane(A))