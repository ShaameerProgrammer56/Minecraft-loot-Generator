import random 

loot = ["stone","Diamonds","Iron","Lapis","Steak","RedStone","Gold","Dirt"]
diamonds = 0

for loot_count in range(1,11) :
    random_item = random.choice(loot)
    print(f"CHEST {loot_count} : {random_item} inside chest")
    if random_item == "stone" : 
        print("Better than Nothing !")
    elif random_item == "Diamonds" :
        print("LESS GOO")
        diamonds += 1
    elif random_item == "Gold" :
        print("I wish i had this irl :(")
    else : 
        print("ATLEAST I HAVE SOMETHING I GUESS")

    print(f"You Got This Much Diamonds {diamonds}")
