Boss_hp = 103
Boss_atk = 9
Boss_def = 2

Self_hp = 100
Self_atk = 0
Self_def = 0

Weapon = [[8,4],[10,5],[25,6],[40,7],[74,8]]
Armor = [[13,1],[31,2],[53,3],[75,4],[102,5]]
Ring = [[25,1,0],[50,2,0],[100,3,0],[20,0,1],[40,0,2],[80,0,3]]

Money = 0

for w in Weapon:
    for a in Armor:
        for r1 in range(-1,6):
            for r2 in range(-1,6):
                Self_def = a[1]        
                Self_atk = w[1]   
                if r1 > -1:
                    Self_atk += Ring[r1][1]
                    Self_def += Ring[r1][2]
                if r2 > -1 and r2 != r1:
                    Self_atk += Ring[r2][1]
                    Self_def += Ring[r2][2]

                Boss_dmg = Boss_atk - Self_def
                Self_dmg = Self_atk - Boss_def
                if Boss_dmg < 1:
                    Boss_dmg = 1
                if Self_dmg < 1:
                    Self_dmg = 1
                
                if (Self_hp % Boss_dmg):
                    extra = -1
                else:
                    extra = 0 

                if ((Boss_hp // Self_dmg) + extra) * Boss_dmg >= Self_hp:
                    cost = w[0] + a[0]
                    if r1 > -1:
                        cost += Ring[r1][0]
                    if r2 > -1 and r2 != r1:
                        cost += Ring[r2][0]
                        
                    Money = max(Money,cost)

print(Money)

            