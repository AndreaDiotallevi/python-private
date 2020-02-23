def movie(card, ticket, perc):
    n = 1
    a = ticket
    b = card + ticket * perc
    while (a < b):
        n += 1
        a += ticket
        b += ticket * perc ** n        
    return n
