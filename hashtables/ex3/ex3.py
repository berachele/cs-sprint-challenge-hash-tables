def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #variables needed: result = list for end result, and cache = dict to check numbers
    result = []
    cache = {}
    #check each array in arrays
    for a in arrays:
        #check each number in array
        for num in a:
            #if the number is in cache
            if num in cache:
                #add 1 to cache
                cache[num] += 1
            #otherwise, cache[num] = 1 (only in there once)
            else:
                cache[num] = 1
    #have a cache with key, values
    #wanting to find the key with the most values
    for key, value in cache.items():
        #if value is the len of arrays,
        if value == len(arrays):
            #add the key to result list
            result.append(key)
    #return result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
