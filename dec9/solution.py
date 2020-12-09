from collections import deque
with open('input.txt', 'r') as data:
    data = [int(line.rstrip('\n')) for line in data]

def twoSum(num_arr, pair_sum):
    hashTable = {}
    counter = 0

    for i in range(len(num_arr)):
        complement = pair_sum - num_arr[i]
        if complement in hashTable:
            counter += 1
            break
        else:
            counter +=1
            if counter == len(num_arr):
                return pair_sum
        hashTable[num_arr[i]] = num_arr[i]

def arraySum(num_array, target_sum):
    for i in range(len(num_array)):
        current_sum = num_array[i]
        j = i + 1
        while j <= len(num_array):
            if current_sum == target_sum and j != i + 1:
                return num_array[i:j]
            if current_sum > target_sum or j == len(num_array):
                break
            current_sum += num_array[j]
            j += 1



preamble_length = 25
error_value = 0

l = deque(maxlen=preamble_length)
for num in data:
    if len(l) == preamble_length:
        return_val = twoSum(l, num)
        if return_val is not None:
            error_value = return_val
    l.append(num)

print(error_value)
sub_array = arraySum(data, error_value)
sub_array.sort()
print(sub_array[0] + sub_array[-1])

