def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #variables needed: ht = {}, result = tuple, index for index in list
    for weight1 in weights:
        for weight2 in weights:
            if limit - weight2 == weight1:
                if weight1 < weight2:
                    result = (weight2, weight1)
                else:
                    result = (weight1, weight2)
            else:
                

    return result


weights = [ 4, 6, 10, 15, 16 ]

get_indices_of_item_weights(weights, 5, 21)