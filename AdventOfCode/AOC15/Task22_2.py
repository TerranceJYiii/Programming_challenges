#Rewrite Task22
Boss_hp = 71
Boss_atk = 10

Self_hp = 50
Self_mp = 500

magic_list = {"M":53, "D":73, "S":113, "P":173, "R":229}

def check_state(Bh, Sm, Stime, Ptime, Rtime):
    if Ptime > 0:
        Bh -= 3
    if Rtime > 0:
        Sm += 101
    return Bh, Sm, Stime-1, Ptime-1, Rtime-1

def Boss_turn(Bh, Ba, Sh, Sm, Stime, Ptime, Rtime):
    Bh, Sm, Stime, Ptime, Rtime = check_state(Bh, Sm, Stime, Ptime, Rtime)
    if Bh <= 0:
        return True, Bh, Ba, Sh, Sm, Stime, Ptime, Rtime
    else:
        if Stime > 0:
            Sh -= Ba - 7
        else:
            Sh -= Ba

        return False, Bh, Ba, Sh, Sm, Stime, Ptime, Rtime

def my_turn(Bh, Ba, Sh, Sm, Stime, Ptime, Rtime, usedmp, minmp, usedMagic):
    if Sh - 1 <= 0:
        print("Player die for this branch due to hard mode")
        return minmp

    Bh, Sm, Stime, Ptime, Rtime = check_state(Bh, Sm, Stime, Ptime, Rtime)
    if Bh <= 0:
        print("Boss die", usedMagic)
        return min(minmp, usedmp)
        
    for magic in magic_list:
        print(Sm, usedMagic)
        if Sm < magic_list[magic]:
            print("Out of Mana for this branch to use",magic , usedMagic)
            return minmp
        
        else:
            now_usedMagic = usedMagic + magic
            now_Sm = Sm - magic_list[magic]
            now_usedmp = usedmp + magic_list[magic]
            now_Bh = Bh
            now_Sh = Sh - 1
            now_Stime = Stime
            now_Ptime = Ptime
            now_Rtime = Rtime

        if magic == "M":
            now_Bh = Bh - 4
        elif magic == "D":
            now_Bh = Bh - 2
            now_Sh = Sh + 2
        elif magic == "S":
            if Stime > 0:
                continue
            else:
                now_Stime = 6
        elif magic == "P":
            if Ptime > 0:
                continue
            else:
                now_Ptime = 6
        elif magic == "R":
            if Rtime > 0:
                continue
            else:
                now_Rtime = 5

        if now_Bh <= 0:
            print("Boss die", now_usedMagic)
            return min(minmp, now_usedmp)

        Boss_die, now_Bh, Ba, now_Sh, now_Sm, now_Stime, now_Ptime, now_Rtime = Boss_turn(now_Bh, Ba, now_Sh, now_Sm, now_Stime, now_Ptime, now_Rtime)
        if Boss_die:
            print("Boss die", now_usedMagic)
            return min(minmp, now_usedmp)
        
        if now_Sh <= 0:
            print("Player die for this branch", now_usedMagic)
            return minmp
        
        minmp = my_turn(now_Bh, Ba, now_Sh, now_Sm, now_Stime, now_Ptime, now_Rtime, now_usedmp, minmp, now_usedMagic)
    
    return minmp


        
ans = my_turn(Boss_hp, Boss_atk, Self_hp, Self_mp, 0,0,0,0,1000000, "")
print(ans)


"""
My turn:
    check stats (poison, recharge)
    use magic and add mana used
    deal effect
    check boss die
Boss turn:
    check stats (poison, recharge)
    boss attack
    check player die
    
"""