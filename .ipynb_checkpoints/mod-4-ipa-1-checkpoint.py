'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''  
def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

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
    

    
    from_member_following=(social_graph.get(from_member)).get("following")
    to_member_following=(social_graph.get(to_member)).get("following")
    follower= False 
    followed_by= False 
    friends= False 
    no_relationship= False 
    for username in from_member_following: 
        if username==to_member: 
            follower= True 

    for username in to_member_following:
        if username==from_member:
            followed_by=True 

    if follower==True and followed_by==True: 
        return('friends')
    elif follower == True and followed_by==False:
        return('follower')
    elif follower== False and followed_by==True:
        return('followed by')
    else:
        return('no relationship')

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

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


    winner=""
    caseholder=[]
    boarddim=len(board)
    upper_left_to_lower_right=[board[i][i] for i in range(boarddim)]
    caseholder.append(upper_left_to_lower_right)
    lower_left_to_upper_right= [board[boarddim-1-i][i] for i in range(boarddim)]
    caseholder.append(lower_left_to_upper_right)
    columns=[i for i in zip(*board)]
    column_list=[caseholder.append(col) for col in columns]
    #add the board itself
    [caseholder.append(row) for row in board]
    for case in caseholder: 
        bool=all(j == case[0] for j in case)
        if bool==True:
            winner=case[0]
            return(winner)
    if winner=='':
        return('NO WINNER')

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

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



    if (first_stop, second_stop) in route_map:
        case1=(route_map.get((first_stop, second_stop))).get('travel_time_mins')
        return(case1)

    time=0
    for key in route_map.keys(): 
        if key[0]==first_stop:
            base_travel_time=(route_map.get(key)).get('travel_time_mins')
            time+=base_travel_time
            if key[1]==second_stop:
                return(time)
            first_stop= key[1]
    return(time)



