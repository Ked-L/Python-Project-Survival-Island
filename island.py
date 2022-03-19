import time

print('''

      88           88                                 88  
""           88                                 88  
             88                                 88  
88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
       
       

                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
       
       
       
       
       
       


                    
                                        This is Survival Island
                        Your actions will determine if you will survive or be killed...
                          Unlock the secrets of how you got here and escape the island







''')


# countdown timer
def countdown(t):
    while t: # while t > 0 for clarity
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r") # overwrite previous line
      time.sleep(1)
      t -= 1

t = 15





print("*Woosh*...*Woosh*...")
time.sleep(2)
print("...")
time.sleep(2)
print("You awaken to the sound water, gently mashing itself upon the ground beneath you. You look down, and to your surprised, you see sand.")
print("You began to tilt your head in confusion, and began to stare at scenery surrounding you. You began to question your emergence...\n")
time.sleep(3)
print("*GWAKKKKK*........*SQREEEEAKKKK*")
time.sleep(3)
print("You hear chaotic wildlife in the distance. You deduce that the place you are at is a island. You decide to stand up but before you do, you see three items in front of you\n")
time.sleep(3)
answer_1 = input("In front of you lays a " + '\033[1m' + 'knife'", gun, pen." '\033[0m'+ " Which do you choose?\n")

if answer_1 == "knife" or "Knife":
    print("You pick up the knife and inspect it. It seems rusty and has what looks like to be a symbol on it. Not being interested enough of the logo, you stuff the knife into your pocket and began to get up.")
    time.sleep(3)
    print("As you stand up you hear a loud, ferocious rumble behind you. Frightened and startled, you quickly turn around and to your surprised, you see a small and yet, adorable creature staring at you.")
    print("You realize that this small, fury creature couldn't have produce such a roar and decide to go towards it.")
    time.sleep(3)
    print("As you get closer you realize that the creatures 'teeth' were replaced with large, razor sharp edges that seemed like it can shred you to bits. You immediately fall on your bottom, shocked.")
    time.sleep(3)
    print("QRRRAAAAARRRRR...The creature pounces onto you. It jumps and grabs onto your chest. It drags you unto the ground, biting at your face. Fueled with adrenaline, you started to act. ")
    time.sleep(3)
    print("With proficient force, you throw the animal off you. In seconds, it will pounce on you again but this time you may not get lucky. You feel something inside your pocket. It is the knife you had earlier\n ")
    time.sleep(3)

    answer_12 = input("Do you use this knife to " + '\033[1m' + 'attack'" or flee" '\033[0m' + "?  Choose wisely...\n")

    if answer_12 == "attack":
        print("You securely grab the knife and prepare yourself for the creature's attack. In almost an instant, the creature leaps with its gnashing teeth ready to devour you.  ")
        time.sleep(2)
        print("You raise the knife in your hand, at a fixed angle above your chest. The creature, as it is already in the air, makes contact with the edge of the knife. However, the jaw force of the creature is so strong that its bite forces itself onto your chest ")
        time.sleep(2)
        print("You let out a huge cry and look down to see the creatures jaw onto your chest. However, the creature did not continue moving and it looks like it is no longer alive.")
    elif answer_12 == "flee":
        print("You realize the safest option would be to make a run for it. Desperately, you turn towards the trees behind you and began storming to the sounds of wildlife in front of you...")
        time.sleep(3)
        print("*CRACKKKAKS*...*BBKKAARRQQRQQ*......*SAQWWWWWAK*....You ")
    else:
        print("You stand there, panicking on what to do. Frozen, you suddenly remember a vision....\n You are staring out a window-a plane window. Outside of the window you see a bright light that seems to distort everything around you. ")
        time.sleep(2)
        print("'MAYDAY, MAYDAY, MAYDAY....*STATIC*....B-274 GOING DOWN..I REP-*STATIC*...DOWN....'")
        time.sleep(3)
        print("The bright light erupts around the scenery in front of you and produced a blast in what seemed tremble the area around it. Suddenly your vision begans to fade....")
        time.sleep(3)
        print("You feel of the most excruciating pain of teeth, ripping at your flesh. You let out at what seems a cry of help, and lifted both eyes to see the creature onto you, tearing at what's left of your carcass.")
        time.sleep(3)
        print("The sounds of cry continues to be drowned by the sounds of gnashing teeth tearing you apart...")

#if answer_1 == "gun" or "Gun":

#if answer_1 == "pen" or "Pen":

#else:
  #  print("Just then the water in front of you lifts. As you stare into the sea, the water then engulfs you until you become nothing more.")
   # print("'Hush now, you are forgotten...' ")
    #exit()
