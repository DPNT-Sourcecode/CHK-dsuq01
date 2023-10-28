

# noinspection PyUnusedLocal
# skus = unicode string
itemprice = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
multibuy = {'A':[[5,200],[3,20]], 'B':[2,15]}
multi_free = {'E': ['B', 2, 1]}

def checkout(skus):
    totalprice = 0
    itemcount = {} # count the number of every different item, so that when I deduct free items, the count does not go beyond 0
    #multifree_count = {}
    #multibuy_count = {}
    itemlist = []
    for item in skus:
        if item in itemprice: # check item exists
            if item in itemcount:
                itemcount[item] += 1
            else:
                itemcount[item] = 1
                itemlist.append(item) # to be iteratable
        '''
            totalprice += itemprice[item] # add price to sum
            if item in multibuy: # count total number of multibuy items
                if item in multibuy_count:
                    multibuy_count[item] += 1
                else:
                    multibuy_count[item] = 1
            if item in multi_free: # count total number of multifree items
                if item in multifree_count:
                    multifree_count[item] += 1
                else:
                    multifree_count[item] = 1
                    '''
        else:
            return -1

    for item in itemlist:
        if item in multifree:
            itemn = itemcount[item]
            qnum = multi_free[item][1] # number of items to buy to qualify
            freeitem = multi_free[item][0]
            freenum = multifree_count[2] # number of items to go free per qualification for this offer
            # I should do a class ...
            offernum = itemn // qnum # number of items to go free
            reducenum = offernum * freenum
            if reducenum <= itemcount[freeitem]:
                itemcount[freeitem] -= reducenum
            else:
                itemcount[freeitem] = 0
            
    for item in itemlist:
        if item in multibuy:
            cond = multibuy[item]
            for (num,discount) in cond:
                offernum = itemcount[item] // num



    return sumprice


