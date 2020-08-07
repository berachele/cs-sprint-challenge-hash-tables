def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #variables needed: result = list to return, neg = list for negative numbers
    result = []
    neg = []
    #check list of arrays
    for item in a:
        #if number is less than 0, its a neg
        if item < 0:
            #add to neg list
            neg.append(item)
    #check number in neg list
    for num1 in neg:
        #check number in array list
        for num2 in a:
            #if array number == the absolute number of the negative number
            if num2 == abs(num1):
                #add to result
                result.append(num2)

    #return result
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
