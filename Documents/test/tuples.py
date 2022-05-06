def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[::-1]:
        if char != prev:
            result.append(char)
            prev = char
    return result

print(unique_in_order([1,1,1,2,3,4,5,5,5,5,7,7,7,8,9,4,4,4]))