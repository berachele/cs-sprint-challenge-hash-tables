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
    #variables needed: route = list for route order, find = to change which source I'm looking for
    route = []
    find = "NONE"
    #while loop until reaches the end
    while len(route) < length:
        #first find NONE/'find'
        #need a for loop?
        for ticket in tickets:
            for index in ticket:
                if tickets[index].source == find:
                    #add that destination to route
                    route.append(tickets[index].destination)
                    #reassign find to destination
                    find = tickets[index].destination
    #return route

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

reconstruct_trip(tickets, 3)