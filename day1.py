def part_one(data):
    expenses = strings_to_integers(data)
    first, second = find_two_sum(expenses, 2020)
    return first * second

def strings_to_integers(data):
    return list(map(int, data.split()))

def find_two_sum(integers, target_sum):
    integers = sorted(integers)
    low_index = 0
    high_index = -1
    total = 0
    count = 0
    # sum lowest and highest, decrementing highest if sum is > 2020,
    while total != target_sum:
        count += 1
        total = integers[low_index] + integers[high_index]
        if total > 2020:
            high_index -= 1
        elif total < 2020:
            high_index = -1
            low_index += 1
        else:
            print(f'Number of iterations {count}')
            return (integers[high_index], integers[low_index])

