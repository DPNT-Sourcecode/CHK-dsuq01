'''
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |

'''
itemname = []
for i in range(26):
    itemname.append(chr(ord('A')+i))
price = [50,30,20,15,40,10,20,10,35,60,80,90,15,40,10,50,30,50,30,20,40,50,20,90,10,50]
itemprice = {}
for i in range(len(itemname)):
    itemprice[itemname[i]] = price[i]

multifree = {'E':('B',2,1),'F':('F',2,1),'N':('M',3,1), 'R':('Q',3,1), 'U':('U',3,1)}
multibuy = {'A':[(5,200),(3,130)], 'B':[(2,45)], 'H':[[10,80],[5,45]], 'K':[[2,150]], 'P':[[5,200]], 'Q':[[3,80]], 'V':[[3,130],[2,90]]}
print(itemprice)