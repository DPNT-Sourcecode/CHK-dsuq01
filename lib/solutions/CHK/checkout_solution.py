

# noinspection PyUnusedLocal
# skus = unicode string
itemprice = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17, 'Y': 20, 'Z': 21}
multifree = {'E':('B',2,1),'F':('F',2,1),'N':('M',3,1), 'R':('Q',3,1), 'U':('U',3,1)}
multibuy = {'A':[(5,200),(3,130)], 'B':[(2,45)], 'H':[[10,80],[5,45]], 'K':[[2,150]], 'P':[[5,200]], 'Q':[[3,80]], 'V':[[3,130],[2,90]]}
group_buy = ['X','S','T','Y','Z']
def checkout(skus):
    totalprice = 0
    itemcount = {} # count the number of every different item, so that when I deduct free items, the count does not go beyond 0
    itemlist = []
    groupitem = []
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
            (freeitem, qnum, freenum) = multifree[item]#[1] # number of items to buy to qualify
            #freeitem = multifree[item][0]
            #freenum = multifree[item][2] # number of items to go free per qualification for this offer
            # I should do a class ...
            if freeitem == item:
                qnum += 1
                offernum = itemn // qnum # number of items to go free
                reducenum = offernum * freenum
                if freeitem in itemlist:
                    if reducenum <= itemcount[freeitem]:
                        itemcount[freeitem] -= reducenum
                    else:
                        itemcount[freeitem] = 0
            else:
                offernum = itemn // qnum # number of items to go free
                reducenum = offernum * freenum
                if freeitem in itemlist:
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
            if not (item in group_buy):
                totalprice += itemcount[item] * itemprice[item]
            else:
                groupitem.append(item)

    print(groupitem)

            


    
    
    return totalprice


def test():
    items = 'XYZ'
    price = 40
    total = checkout(items)
    print(price==total, price, total)

test()



