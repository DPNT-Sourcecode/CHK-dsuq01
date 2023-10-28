

# noinspection PyUnusedLocal
# skus = unicode string
itemprice = {'A':50, 'B':30, 'C':20, 'D':15, 'E': 40}
multibuy = {'A':[(5,200),(3,130)], 'B':[(2,45)]}
multifree = {'E': ['B', 2, 1]}

def checkout(skus):
    totalprice = 0
    itemcount = {} # count the number of every different item, so that when I deduct free items, the count does not go beyond 0
    itemlist = []
    for item in skus:
        if item in itemprice: # check item exists
            if item in itemcount:
                itemcount[item] += 1
            else:
                itemcount[item] = 1
                itemlist.append(item) # to be iteratable
    
        else:
            return -1

    for item in itemlist:
        if item in multifree:
            itemn = itemcount[item]
            qnum = multifree[item][1] # number of items to buy to qualify
            freeitem = multifree[item][0]
            freenum = multifree[item][2] # number of items to go free per qualification for this offer
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
                totalprice += offernum * discount
                itemcount[item] -= offernum * num
            totalprice += itemcount[item] * itemprice[item]
        else:
            totalprice += itemcount[item] * itemprice[item]


    return totalprice


def test():
    items = 'E'
    price = 200+130+45+30+20+15+40
    total = checkout(items)
    print(price==total, price, total)

test()

