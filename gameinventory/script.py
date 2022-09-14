inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    total_items = 0
    for k,v in inv.items():
        print(k+": " + str(v))
        total_items += 1
    print("Total number of items: " + str(total_items))

def addToInventory(inv,addedItems):
    for item in addedItems:
        inv.setdefault(item,0)
        inv[item] += 1
    return inv
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv,loot)
displayInventory(inv)