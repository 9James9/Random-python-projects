inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inv):
    total_items = 0
    for k,v in inv.items():
        print(k+": " + str(v))
        total_items += 1
    print("Total number of items: " + str(total_items))
displayInventory(inv)