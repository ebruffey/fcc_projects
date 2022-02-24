# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], pred_dict={}):

    #set the number for the pattern to consider
    #set the initial guess to R
    pattern = 6
    guess = 'R'

    #append the plays of the opponent to the list
    #leaves out the first play which is blank
    if prev_play != '':
        opponent_history.append(prev_play)

    #this starts the predictions after we've played 7 plays
    if len(opponent_history) >= (pattern + 1):
        #join the opponent plays 6 at a time 
        opp_hist = ''.join(opponent_history[-pattern:])
        #print(joint)
        
        #check if the pattern is in the prediction dictionary
        if ''.join(opponent_history[-(pattern + 1):]) in pred_dict.keys():
            #if it isnt then we add one count to our prediction dictionary
            #for that specific pattern
            pred_dict[''.join(opponent_history[-(pattern + 1):])] += 1
        else:
            #if the pattern isn't there we place a 1
            pred_dict[''.join(opponent_history[-(pattern + 1):])] = 1

        #the possibilities
        poss = [opp_hist + 'R', opp_hist + 'P', opp_hist + 'S']
        #print(poss)
        #loop through possibilities and if the possibility isn't
        #in the prediction dictionary, place 0 for that value of p
        for p in poss:
            if p not in pred_dict.keys():
                pred_dict[p] = 0
        #print(pred_dict)

        #then find between the possibilties and the max 
        #count in the prediciton dictionary
        pred = max(poss, key=lambda x: pred_dict[x])
        #print(pred)
        
        #foo = max([x for x in pred_dict.values()])
        #bar = [x for x in pred_dict.keys() if foo == pred_dict[x]]
        #print(f"pred: {pred}\t bar: {bar}\n")

        #then we guess
        if pred[-1] == 'P':
            guess = 'S'

        if pred[-1] == 'R':
            guess = 'P'

    return guess