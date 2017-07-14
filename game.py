import random

def kampf():
    """Kampf gegen monster
    retörn 0 wenn spieler gewinnt
    retörn1 wenn spieler verlieirt"""
    print("Spiele Schere Stein Papier mit dem Monster")
    while True:
            
        print("wehle Schere, Stein oder Papier")
        command=input("?")
        if command not in ("Schere","Stein","Papier"):
            return
        gegnerzug=random.choice(("Schere","Stein","Papier"))
        print("Du spielst {} Monster spielt {}".format(command,gegnerzug))
        if  gegnerzug==command:
            print("unentschiden nochmal spilen")
            continue
        if (gegnerzug=="Schere" and command=="Papier") or (gegnerzug=="Stein" and command=="Schere") or (gegnerzug=="Papier" and command=="Stein"):
            print("Monster gewinnt")
            return 1
        print("du gewinnst")
        return 0
        




def shop(geld,semmeln):
    """tausche geld gegen essen"""
    print("Willckommen im shop")
    print("eine Wurstsemmel kostet 2$")
    print("wie viele Wurstsemmeln willst du kaufen?")
    menge=input("?")
    try:
       menge=int(menge)
    except:
        print("Auf Wiedersehen")
        return geld,semmeln
    #Zahl wurde eingegeben
    if menge*2 >geld:
        print("Nein leider nicht genug Geld")
        return geld,semmeln
        
    semmeln+=menge                                                                                                   
    geld-=menge*2
    
    print("Danke für ihren Einkauf")
    return geld,semmeln
    
        






def kiste():
    """gib dem hero ein Mathe Rätsel"""
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=a*b
        antwort=input("wie viel ist {} x {} ?".format(a,b))
        try:
            antwort=int(antwort)
        except:
            print("zahl eingeben du lusche")
            continue
        if antwort==c:
            print("bravo richtig")
            return
        print("falsche Zahl")
        print(a,"x",b,"=",c)
        
         


dungeon1="""
########################################################################
#....M.............wwwwwww.$$$$$$$......w......................##......#
#######...########.#............................$$$.........w..#......##
#...........$$......#......... #######..................$......#.....###
#.........................$....w.####....?????????...............#.....#
#>.....1.kk....w.........?....MMM....#..........................#......#
###################################.####################################
"""

dungeon2="""
###########################dd#######d###################################
#..............#...w.....?.......w......#############.##################
#......................#...w...........................................#
#........................................#.............$$$$$$$$$.......#
#........................#................#...................$$$$$$$4.#
#<.....2........>.........#................#...........................#
##################################################dd####################
"""

dungeon3="""
##################################################.#####################
#.......3.......<...........wwwwwwww...................................#
###########################################................wMMMMMMMMMMM#
#.....?...................................#..................#######.###
#.................w..............M........#.......w.........#.P.......#
#.....................$...............s......................#.....t...#
#.........$................................................?.#.....MMM##
########################################################################
"""
#"..s.w.$$..s...$...w....w...?...s...?..w....$....?.....$.....w.....o....p"
level=[]
for d in (dungeon1,dungeon2,dungeon3):
    dungeon = []
    for line in d.splitlines():
        dungeon.append(list(line))
    level.append(dungeon)
   

        
    


hero='|'


herox=1
heroy=2
heroz=0
herogold=0
herowurst=0
herohunger=0
heroschlüssel=0
herohp=101

while True:
    for z, dungeon in enumerate(level):
        if z != heroz:
            continue
        for y, line in enumerate(dungeon):
            #if y != heroy:
            #    print(line)
            #else:
            for x,b in enumerate(line):
                if x ==herox and y==heroy:
                    print(hero,end="")
                else:
                    print(b,end="")
            print()
    #herox=int(input())
    command=input("gold:{} semmeln:{} hunger:{} schlüssel:{} hp:{}   ???".format(herogold,herowurst,herohunger,heroschlüssel,herohp))
    
    
    
    
    #herohunger+=1
    #steigt der hunger? 20% chance
    if random.random()<0.2:
        herohunger+=random.randint(5,10)
        print("Ich habe einen riesen Hunger")
    #bewegung
    dx=0
    dy=0
            
    if command=="w":
            dy=-1
    if command=="s":
            dy=1
    if command=="a":
            dx=-1
    if command =="d":
            dx=1
    if command=="up":
        if level[heroz][heroy][herox]=="<":
            heroz-=1
            continue
        else:
            print("Finde erst ein Stiegenhaus >")          
    
    if command=="down":
        if level[heroz][heroy][herox]==">":       
            heroz+=1
            continue
        else:
            print("Finde erst ein Stiegenhaus <")
    
   
    if command =="jump":
            dx=5
    if command =="kill":
        print("game over zum beenden enter drücken")
        break
        
        
    if command =="jump s":
            dy=5
    if command =="jump n":
            dy=-5
    #if command =="up":
        #heroz+=5
        
#    herohunger+=2
    # --- in mauer gelaufen ? ------
    ziel=level[heroz][heroy+dy][herox+dx]
    if ziel =="#":
        print("aua")
        dx = 0
        dy = 0
    if ziel =="M":
        print("Ein Monster blockiert deinen Weg")
        resultat=kampf()
        if resultat==0:
            level[heroz][heroy+dy][herox+dx]=random.choice(("w","$","?","."))
        else:
            herohp-=random.randint(10,20)
            print("Das Monster tut dir weh")
            if herohp <1:
                break
        dx=0
        dy=0
                
        
        
        
    
    # bewegung!
    herox+=dx
    heroy+=dy
    if command =="eat":
      if  herowurst>0: 
          herohunger-=10
          herowurst-=1
      
            #----auswertung------ 
    stuff=level[heroz][heroy][herox]
    
    if stuff =="k":
        print("Uh ein Schlüssel")
        heroschlüssel+=1
        level[heroz][heroy][herox]="."
    if stuff == "$":  
        print("hurra Geld")
        herogold+=1
        level[heroz][heroy][herox]="."
    if stuff == "?":
        print("welches Rätsel wird wohl kommen?")
        kiste()
    if stuff == "p":
        print("hurra ich habe sie gefunden!!")
    if stuff == "w":
        print("Miami gute Wurstsemmel")
        herowurst+=1
        level[heroz][heroy][herox]="."
    if herohunger<0:
        print("geplatzt")
        break
        herogold,herowurst=shop(herogold,herowurst)
    if herohunger>100:
    
    
        
        
        print("game over")
        
        
        
        
        print("du bist Verhungert")
        break
        
