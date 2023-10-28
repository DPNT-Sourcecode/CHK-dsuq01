

# noinspection PyUnusedLocal
# skus = unicode string
itemprice = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
multibuy = {'A':[[5,50],[3,20]], 'B':[2,15]}

def checkout(skus):
    sumprice = 0
    multibuy_count = {}
    for item in skus:
        if item in itemprice: # check item exists
            sumprice += itemprice[item] # add price to sum
            if item in multibuy: # process discount
                if item in multibuy_count:
                    multibuy_count[item] += 1
                else:
                    multibuy_count[item] = 1
                if multibuy_count[item] == multibuy[item][0]: #enough for discount
                    sumprice -= multibuy[item][1]
                    multibuy_count[item] = 0 
            
        else:
            sumprice = -1
            break
    return sumprice



