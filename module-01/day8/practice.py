# 1 Recursive sum 
def total(nums):
    if not nums:
        return 0
    return nums[0] + total(nums[1:])


def count_down(n):
    if n < 1:
        return
    print(n)
    count_down(n - 1)


# 2. Binary search
def binary_search(items, target):
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


# 3. Merge sort
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)


# 4. Sort with a key
tuples_list = [("Abdu", 500), ("Beki", 1200), ("sima", 300)]
sorted_by_balance = sorted(tuples_list, key=lambda x: x[1], reverse=True)


# 5. Two pointers
def has_pair(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return True
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return False

print("Total of [100, 250, 400]:", total([100, 250, 400]))
print("Countdown from 3:")
count_down(3)

balances = [100, 300, 500, 1200, 5000]
idx = binary_search(balances, 500)
print("Index of 500 in balances:", idx)
print("Index of 999 (missing):", binary_search(balances, 999))

unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print("Original:", unsorted_list)
print("Merge Sorted:", sorted_list)
print("Sorted by balance descending:", sorted_by_balance)
sorted_nums = [10, 20, 35, 50, 75]
print("Has pair summing to 70 (20+50):", has_pair(sorted_nums, 70))
print("Has pair summing to 100:", has_pair(sorted_nums, 100))