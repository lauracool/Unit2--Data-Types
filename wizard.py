
def wizard(owner,N,duels):
    last_owner = owner
    changes = 0
    print(duels[0][1])
wizard("A",3,["BA","CB"])
#check if wand changed hands
def wizards(N,start,duels):
    owner = start
    num_owners=1
    for i in range(N):
        if duels[i][1] == owner:
            owner = duels[i][0]
            num_owners +=1
    print(owner, num_owners)

wizards(3, "A", ["BA", "CB", "DA"])
