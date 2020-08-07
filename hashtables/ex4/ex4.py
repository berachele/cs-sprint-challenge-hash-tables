def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #variables needed: result = list to return, neg = list for negative numbers
    #check list of arrays
        #if number is less than 0, its a neg
            #add to neg list
    #check number in neg list
        #check number in array list
            #if array number == the absolute number of the negative number
                #add to result
    #return result

    result = []
    neg = []
    for item in a:
        if item < 0:
            neg.append(item)
    for num1 in neg:
        for num2 in a:
            if num2 == abs(num1):
                result.append(num2)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
