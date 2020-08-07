def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #variables needed: result = list for end result, and cache = dict to check numbers
    result = []
    cache = {}
    #check each array in arrays
        #check each number in array
            #if the number is in cache
                #add 1 to cache
            #otherwise, cache[num] = 0
    #have a cache with key, values
    #wanting to find the key with the most values
        #if value is the len of arrays,
            #add the key to result list
    #return result
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
