def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #variables needed: result = list for end result, and cache = dict to check numbers
    #check each array in arrays
        #check each number in array
            #if the number is in cache
                #add 1 to cache
            #otherwise, cache[num] = 1 (only in there once)
    #have a cache with key, values
    #wanting to find the key with the most values
        #if value is the len of arrays--showing that key is in all lists,
            #add the key to result list
    #return result
    result = []
    cache = {}
    for a in arrays:
        for num in a:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1
    for key, value in cache.items():
        if value == len(arrays):
            result.append(key)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(20, 30)) + [1, 2, 3])
    arrays.append(list(range(30, 40)) + [1, 2, 3])

    print(intersection(arrays))
