#function definitions

'''fuction to calculate total batting points'''

def battingScore(details):
    name = details['name']
    runs = details['runs']
    balls = details['balls']
    nFour = details['4']
    nSix = details['6']
    field = details['field']
    
    points = runs/2
    
    strikeRate = (runs/balls)*100
    
    if runs >= 50:
        points = points + 5
        
    if runs >= 100:
        points = points + 10
        
    if strikeRate >= 80:
        points = points + 2
        
    if strikeRate > 100:
        points = points + 4
        
    totalPoints = points + nFour + 2*nSix + 10*field
    
    result = {'name': name, 'batscore': totalPoints}
    
    return result

'''function to calculate total bowling points'''

def bowlingScore(details):
    name = details['name']
    wickets = details['wkts']
    overs = details['overs']
    runs = details['runs']
    field = details['field']
    
    ecoRate = runs/overs

    points = 10*wickets

    if wickets >= 3:
        points = points + 5

    if wickets >= 5:
        points = points + 10

    if ecoRate >= 3.5 and ecoRate <= 4.5:
        points = points + 4

    elif ecoRate >= 2 and ecoRate < 3.5:
        points = points + 7

    elif ecoRate < 2:
        points = points + 10

    totalPoints = points + 10*field

    result = {'name': name, 'bowlscore': totalPoints}

    return result

'''function to decide the topmost player'''

def Verdict(finallist, scorelist):
    for z in finallist:
        if z['score'] == max(scorelist):
            Player = z['name']

    return Player


        











    
    

