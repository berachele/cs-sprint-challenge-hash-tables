#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    #variables needed: route = list for route order, 
    #find = to change which source I'm looking for
    #index --> keep track of index in list of tickets, not index of result
    #while loop until reaches the end (len = route length)
        #first find NONE/'find'
            #add that destination to route
            #reassign find to destination
        #need to change index before looping again
        #if length -1 (to keep in loop) = index
            #reassign index to 0
        #otherwise increment index
    #return route

    route = []
    find = "NONE"
    index = 0
    while len(route) < length:
        if tickets[index].source == find:
            route.append(tickets[index].destination)
            find = tickets[index].destination

        if index == length -1:
            index = 0
        else:
            index += 1
    return route




#TESTER
# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
#             ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


reconstruct_trip(tickets, 10)