'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
     if to_member in social_graph[from_member]["following"]:
        follower = True
    else:
        follower = False

    if from_member in social_graph[to_member]["following"]:
        followed_by = True
    else:
        followed_by = False
        

    
    # if username of from_member is in dict of to_member and vice versa and vice versa then dating
    if follower == True and followed_by == True :
        status = "friends"
        
    # if username of from_member is in dict of to_member but not vice versa then follower
    if follower == True and followed_by == False:
        status = "follower"
        
    # if username of to_member is in dict of from_member but not vice versa then followed by
    if follower == False and followed_by == True:
        status= "followed by"
    # if neither follows each other then no relationship
    if follower == False and followed_by == False:
        status = "no relationship"
    return status


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
     # WINNER CONDITIONS
        # if same symbol three times in a row in list (index (0, 1, 2), index (1,2,3), etc.)
        # if same symbol three times in a row in same index across 3 lists in a row ( board[1][3] board[2][3] board[3][3])
        # if same symbol three times in a row as index increases by 1 going into next list ( [2][1] [3][2] [4][3] }
        # if same symbol three times in a row index decreases by 1 going into next list ( [1][3] [2][2] [3][1] )
    # if same symbol three times in a row in list (index (0, 1, 2), index (1,2,3), etc.)
    for x in range(0,len(board)):
        horizontal_x = ""
        horizontal_o = ""
        #if x put x if o put o
        for y in range (0, len(board)):
            if board[x][y] == "X":
                horizontal_x += "X"
            elif board[x][y] == "O":
                horizontal_o += "O"
                
        #if it matches the win con the thing wins
        if horizontal_x == "X" * len(board):
            return "X"
        elif horizontal_o == "O" * len(board):
            return "O"
        else:
            continue
    # if same symbol three times in a row in same index across 3 lists in a row ( board[1][3] board[2][3] board[3][3])
    for x in range(0,len(board)):
        vertical_x = ""
        vertical_o = ""
        for y in range (0, len(board)):
            if board[y][x] == "X":
                vertical_x += "X"
            elif board[y][x] == "O":
                vertical_o += "O"
        if vertical_x == "X" * len(board):
            return "X"
        elif vertical_o == "O" * len(board):
            return "O"
        else:
            continue
    # if same symbol three times in a row as index increases by 1 going into next list ( [2][1] [3][2] [4][3] }
    right_x = ""
    right_o = ""
    for x in range(0,len(board)):
        if board[x][x] == "X":
            right_x += "X"
        elif board[x][x] == "O":
            right_o += "O"

        if right_x == "X" * len(board):
            return "X"
        elif right_o == "O" * len(board):
            return "O"
        else:
            continue
    # if same symbol three times in a row index decreases by 1 going into next list ( [1][3] [2][2] [3][1] )
    left_x = ""
    left_o = ""
    for x in range(0,len(board)):
        if board[x][(len(board) - 1) - x] == "X":
            left_x += "X"
        elif board[x][(len(board) - 1) - x] == "O":
            left_o += "O"

        if left_x == "X" * len(board):
            return "X"
        elif left_o == "O" * len(board):
            return "O"
        else:
            continue

    return "NO WINNER" 

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    # getting keys of dictionary
    keys_route_map = route_map.keys()
    keys_route_map = list(keys_route_map)
    
    #first stop
    index = 0
    while keys_route_map[index][0] != first_stop:
        index += 1
    
    #finding second stop
    second_index = 0
    while keys_route_map[second_index][1] != second_stop:
        second_index += 1
        
    #getting total time
    total_time = route_map[keys_route_map[index]]["travel_time_mins"]
    
    while index != second_index:
        index += 1

        if index > len(keys_route_map)-1:
            index = 0
        
        total_time += route_map[keys_route_map[index]]["travel_time_mins"]
    
    return total_time