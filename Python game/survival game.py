import easygui, random

#sets all varibles to default
decision1 = False
decision2 = False
decision3 = False
decision4 = False
decision5 = False
decision6 = False
decision7 = False
decision8 = False
decision9 = False
decision10 = False
decision11 = False
decision12 = False
decision13 = False
decision14 = False
decision15 = False
decision16 = False
decision17 = False
decision18 = False
decision19 = False
decision20 = False
decision21 = False
decision22 = False

# creates a function if player dies.
def death():
    easygui.msgbox("you have died")
    play = easygui.ynbox("do you wish to play from the last check point?")
    #if player selects no
    if play == False:
        health = "0"
    #if player selects yes
    elif play == True:
        #resets health to 100
        health = "100"
# sees if player wants to play the game 
start = easygui.ynbox(" hello and welcome to the great jungle escape \n would you like to play ")
# if player says no. game will end. 
if start == False:
    easygui.msgbox(" ok then, goodbye")
# if player says yes. game will start
elif start == True:
    # sets health to full
    health = "100"
    #sets score to 0 
    score = 0
    #sets death count to 0
    death_count = 0
    # sets success and finsihed to false
    success = False
    finished = False
    #checks player is above age restiction 
    age = easygui.integerbox("how old are you?")
    if int(age) < 12:
        easygui.msgbox("sorry but you are too young")
    elif age >= 12:
        easygui.msgbox("awesome, you can play the game")
        # gets players name
        name = str(easygui.enterbox("what is your name"))
        while name == "":
            name = easygui.enterbox("sorry i didnt get that \n please type your name again")
        easygui.msgbox("hello " + name)
        #game starts
        easygui.msgbox("pilot: oh no " + name + ", the plane is going down \n get a parachute and jump \n NOW!!!")
        easygui.msgbox("you jump off and land safely but you are all alone and have nothing")
        decision1 = True 
        #decision one
        while decision1 == True:
            score += 1
            choices =  ("go exploring", "search for food", "stay still and wait for possible resue")
            choice = easygui.buttonbox("what to do first", "health :" + health, choices)
            if choice == choices[0]:
                decision2 = True
                decision1 = False
            elif choice == choices[1]:
                easygui.msgbox("you go searching for food and stumple across berries, mushrooms and cabage trees")
                decision8 = True
                decision1 = False
            elif choice == choices[2]:
                easygui.msgbox("the sun is beginging to set and there is no sign of resue")
                decision3 = True
                decision1 = False
        # decision 2
        while decision2 == True:
            score += 1
            choices = ("something exciting", "just walk around trying to find anything", "a water source")
            choice = easygui.buttonbox("what should you try and find?", "health :" + health, choices)
            if choice == choices[0] or choice == choices[1]:
                easygui.msgbox("you stumble across an abandoned temple. covered in spiderwebs and old food scraps")
                decision10 = True
                decision2 = False
            elif choice == choices[2]:
                decision9 = True
                decision2 = False
        #decision 3
        while decision3 == True:
            score += 1
            choices = ("search for food and shelter", "keep waiting")
            choice = easygui.buttonbox("what are you going to do now " + name, "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you go searching for food or shelter and stumple across berries, mushrooms and cabage trees")
                decision8 = True
                decision3 = False
            if choice == choices[1]:
                easygui.msgbox("you stay up and keep waiting for a rescue that may never happen")
                decision4 = True
                decision3 = False
        # decision 4
        while decision4 == True:
            score += 1
            choices = ("keep waiting", "sleep")
            choice = easygui.buttonbox("what are you going to do next?", "health :" + health, choices)
            if choice == choices[0]:
                # 25% chance of escape
                number = random.randint(1,4)
                if number == 1:
                    escape = True
                else:
                    #did not escape so game continues
                    easygui.msgbox("you realise that rescue isn't coming and decide to get some sleep.")
                    decision5 = True
                    decision4 = False
            elif choice == choices[1]:
                easygui.msgbox("you find a nice pile of leaves and try go to sleep")
                decision5 = True
                decision4 = False
        # decision 5
        while decision5 == True:
            score += 1
            choices = ("run away from the noise", "stand your ground", "go towards the noise")
            choice = easygui.buttonbox("you fall asleep and wake up to the sound of stomping feet", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you run away from the noise and find a safe space the catch your breath")
                decision7 = True
                decision5 = False
            elif choice == choices[1]:
                easygui.msgbox("you see hundreds of elephants, rhinos and horses running past you.")
                decision6 = True
                decision5 = False
            elif choice == choices[2]:
                easygui.msgbox("you go towards the noise only to get caught in the middle of a stampede,")
                death()
                death_count += 1
        # decision 6
        while decision6 == True:
            score += 1
            choices = ("run away incase of threat", "hope it is nothing and carry on")
            choice = easygui.buttonbox("animals usually stampede when they are in danger", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you run away and find a safe spot")
                decision7 = True
                decision6 = False
            elif choice == choices[1]:
                easygui.msgbox("the end of the stampede is approaching and you notice that they where running away from a pride of lions")
                death()
                death_count += 1
        # decision 7
        while decision7 == True:
            score += 1
            choices = ("go searching for food", "go exploring")
            choice = easygui.buttonbox("you decide that will be a good idea to serch for something", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you go searching for food and stumble across berries, mushrooms and cabbage trees")
                decision8 = True
                decision7 = False
            elif choice == choices[1]:
                decision2 = True
                decision7 = False
        # decision 8
        while decision8 == True:
            score += 1
            food = True
            choices = ("Cabbage tree", "Berries", "Mushrooms")
            choice = easygui.buttonbox("what do you eat", "health :" + health, choices)
            if choice == choices[0]:
                food_type = "cabbage tree"
                easygui.msgbox("you cut up the tree and eat the stems")
                easygui.msgbox("you decide it will be good to go exploring and try find a way out")
                decision2 = True
                decision8 = False 
            elif choice == choices[1]:
                food_type = "berries"
                easygui.msgbox("you pick some berries and eat as much as you can ")
                easygui.msgbox("you decide it will be good to go exploring and try find a way out")
                decision2 = True
                decision8 = False
            elif choice == choices[2]:
                food_type = "mushrooms"
                easygui.msgbox("un oh I don't think mushrooms were a smart idea")
                # sees if the mushrooms are poisionous or not
                number = random.randint(1,4)
                if number == 1:
                    easygui.msgbox("neverminded you just ate too fast ")
                    easygui.msgbox("you decide it will be good to go exploring and try find a way out")
                    decision2 = True
                    decision8 = False
                elif number == 2 or 3:
                    easygui.msgbox("you dont look very good (- 50 health)")
                    health = int(health)
                    health = health - 50
                    health = str(health)
                    easygui.msgbox("you decide it will be good to go exploring and try find a way out")
                    decision2 = True
                    decision8 = False
                else:
                    easygui.msgbox("oh no, that was a death cap, the most poisonous mushrooms in the world")
                    death()
                    death_count += 1
        #decision9
        while decision9 == True:
            score += 1
            choices = ("go for a swim", "follow the water downstream", "gather water")
            choice = easygui.buttonbox("you come across a water hole. What should you do?", "health :" + health, choices)
            if choice == choices[0]:
               easygui.msgbox("you go for a refreshing swim. then a hippopotamus comes and eats you ")
               death()
               death_count += 1
            elif choice == choices[1]:
               easygui.msgbox("you follow the river down stream, for hours")
               easygui.msgbox("seem all rivers lead to the sea you come across a beach")
               easygui.msgbox("you notice a family at the beach and as to borrow their phone. you are saved")
               success = True
               decision9 = False
            elif choice == choices[2]:
               easygui.msgbox("you gather water and continue walking")
               decision11 = True
               decision9 = False
        #decision10
        while decision10 == True:
            score += 1
            choices = ("walk past the temple","explore the temple")
            choice = easygui.buttonbox("what should you do?", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you walk past the temple, and you hear strange noises coming from the temple. you keep walk and monkeys begin to surround you.")
            elif choice == choices[1]:
                easygui.msgbox("you walk further into the temple and notice heaps of banana peels, you turn around only to notice about 14 monkeys staring straight at you")
            decision12 = True
            decision10 = False
        #decision11
        while decision11 == True:
            score += 1
            choices = ("no not me and walk away","run and help the stranger")
            choice = easygui.buttonbox("stranger: HELP, yes you " + name + " help me","health: " + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you walk away and attempt to find your own way out")
                decision12 = True
                decision11 = False    
            elif choice == choices[1]:
                easygui.msgbox("you go towards the stranger and help lift a large rock of them. you drop it on your foot ouch (- 20 health)")
                health = int(health) - 20
                health = str(health)
                easygui.msgbox('stranger: "thanks"' + name + "what are you doing in this forest anyways")
                easygui.msgbox('you: "i\'m lost"')
                easygui.msgbox("stranger: well of course you are, i can call in a couple of my friends to help you out. but you will need to get them some food.")
                decision14 = True
                decision11 = False 
        #decision12
        while decision12 == True:
            score += 1
            easygui.msgbox("monkey: hello young traveler I am king pan ruler of the wild, you seem to be lost, i can help you only if you help me")
            choices = ("sure, what do you need help with.","i am not lost","insult the monkey")
            choice = easygui.buttonbox("how do you reply", "health :" + health, choices)
            if choice == choices[2]:
                easygui.msgbox(" monkey: I would be more careful what you say, if i was you. now ill ask you one more time. would you like my help or not.")
                choices = ("Sure, what can I do","no thanks I dont need help")
                choice = easygui.buttonbox("what do you say back?", "health" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("monkey: my son rowan hes been missing for the couple of days, and you see i would go out to find him myself but my family cant survive with out me. ")
                decision16 = True
                decision12 = False
            elif choice == choices[1]: 
                easygui.msgbox("monkey: what ever you say.")
                easygui.msgbox("you continue walking")
                decision11 = True
                decision12 = False
        #decision13
        while decision13 == True:
            score += 1
            choices = ("try and jump the gap","swing across using the rope","look for a bridge")
            choice = easygui.buttonbox("you come across a rapid river which is far too dangerous to cross by foot. On the other side of the river there is a small vilage. \n How do you get across?", "health :" + health, choices)
            if choice == choices[0]:
                number = random.randint(1,4)
                if number == 1:
                    easygui.msgbox("you make the jump, and find a safe way home")
                    success = True
                elif number == 2:
                    easygui.msgbox("you miss the jump and hit your head.")
                    death()
                    death_count += 1
                else:
                    decision14 = True
                    decision13 = False
            elif choice == choices[1]:
                number = random.randint(1,2)
                if number == 1:
                    easygui.msgbox("you make it across safely")
                    success = True
                else:
                    easygui.msgbox("the rope breaks, you hit your head and die")
                    death()
                    death_count += 1
            elif choice == choices[2]:
                easygui.msgbox("you walk by the rivers edge and find a small plank and cross the river. you go back to the small village and call home for help.")
                success = True
                decision13 = False
        #decision14
        while decision14 == True:
            score += 1
            choices = ("swing across the rope","look for a bridge")
            choice = easygui.buttonbox("what to do now", "health :" + health, choices)
            if choice == choices[0]:
                number = random.randint(1,2)
                if number == 1:
                    easygui.msgbox("you make it across safely")
                    success = True
                else:
                    easygui.msgbox("the rope breaks, you hit your head and die")
                    death()
                    death_count += 1
                decision13 = False
            elif choice == choices[1]:
                easygui.msgbox("you walk by the rivers edge and find a small plank and cross the river. you go back to the small village and call home for help.")
                success = True
                decision13 = False
        #decision15
        while decision15 == True:
            score += 1
            choices = ("sure","no, its ok I will find my own way out")
            choice = easygui.buttonbox('stranger: "can you get me some food?"', "health :" + health, choices)
            if choice == choices[0]:
                if food == True:
                    easygui.msgbox("I have some " + food_type + " that I colected earlier")
                    easygui.msgbox('stranger: "oh no dear they don\'t eat' + food_type +'they enjoy to fresh meat but they will settle for some apples"')
                else:
                    easygui.msgbox('you: "what do they eat" \n stranger: "some good quality apples will do" ')
                easygui.msgbox('cant be to hard.\n you: "are there any apple trees near by?"')
                easygui.msgbox('stranger: "yea just a 10 minute walk that way. i\'ll call them over"')
                easygui.msgbox("you set off to get some apples")
                easygui.msgbox("you reach rows upon rows of the largest apple trees you have ever seen. and start to pick some")
                decision20 = True
                decision15 = False
            elif choice == choices[1]:
                easygui.msgbox('stranger: "ok then. your loss"')
                easygui.msgbox("you attempt to find your own way out")
                decision13 = True
                decision15 = False
        #decision16
        while decision16 == True:
            score += 1
            choices = ("ok i'll be back","no thanks to much work")
            choice = easygui.buttonbox("do you take the deal?", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox('monkey: "ok then"')
                easygui.msgbox("you continue walking")
                decision11 = True
                decision16 = False
            elif choice == choices[1]:
                easygui.msgbox('monkey:"Don\'t be long"')
                easygui.msgbox("you set out and try to find the monkeys son")
                easygui.msgbox("you notice a set of footsteps which are slightly larger than the average monkey and begin to follow them ")
                decision17 = True
                decision16 = False
        #decision17
        while decision17 == True:
            score += 1
            choices = ("wait outside for the monkeys son to come near","go inside")
            choice = easygui.buttonbox("they lead to a cave covered in moss", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("some strange creature gabs you and picks you up and takes you towards the cave")
                easygui.msgbox("he throws you in to a cell and you notice the monkeys son is in there with you")
                decision18 = True
                decision17 = False
            elif choice == choices[1]:
                easygui.msgbox("you walk inside and notice a monkey probably the kings son rowan in a cage you go up and try to free him ")
                decision19 = True
                decision17 = False
        #decision18
        while decision18 == True:
            score += 1
            choices = ("force the door open","look for keys")
            choice = easygui.buttonbox("how do you free him", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you shake the door, and the monkey looks at you with a worried look")
            elif choice == choices[1]:
                easygui.msgbox("you look around the cave but have no luck, the keys aren't near you and your eye sight isn't that good in the dark")
            easygui.msgbox("you hear a noise behind you, and you turn around slowly only to notice a large bull almost human like creature.")
            easygui.msgbox("he picks you up and chucks you in the cage with rowan that kind of hurt (-30 health)")
            health = int(health)
            health = health - 30
            health = str(health)
            decision19 = True
            decision18 = False
        #decision19
        while decision19 == True:
            score += 1
            choices = ("ask rowan for help","force the door open")
            choice = easygui.buttonbox("the bull like creature leaves and you know now is the time to escape ", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("he picks the lock using its tail")
                easygui.msgbox("you and rowan are free \n you go back to king pan" )
                easygui.msgbox('monkey pan: "thankyou for saving my son." \n you: " he saved me')
                easygui.msgbox("follow the river east and you shall find sanctuary ")
                easygui.msgbox("you follow the river and find a small village, and call your home. ( you are saved)")
                success = True
                decision19 = False
            elif choice == choices[1]:
                easygui.msgbox("you shake the door back and forth but nothing seems to happen. you try over and over again but nothing seems to happen")
                easygui.msgbox("the bull creature comes back.\n bull creature: yum human, don't get a lot of them these days. he grabs you forcefully ")
                death()
                death_count += 1
        #decision20
        while decision20 == True:
            score += 1
            choices = ("run away","bargin")
            choice = easygui.buttonbox("HEY!!, THOSE ARE MY APPLES. GO AWAY!!", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you run away but the loud angry creature reaches you and throws you away. (- 50 health)")
                health = int(health) - 50
                health = str(health)
                decision21 = True
                decision20 = False
            elif choice == choices[1]:
                easygui.msgbox("please sir, I just need a couple. its not like you could eat all these anyways. ")
                easygui.msgbox("creature: it doesn't matter these are my pride and joy")
                easygui.msgbox('you notice the creature is chained to a large weight and you have an idea \n you: "I can free you"')
                easygui.msgbox("you: but still possible")
                easygui.msgbox("creature: try your best, if you succeed you may take as many apples as your heart desires ")
                decision22 = True
                decision20 = False
        #decision21
        while decision21 == True:
            score += 1
            choices = ("go and try to sneak some apples","go back to the stranger and explain you couldn't get any apples","leave and try to find your own way out")
            choice = easygui.buttonbox("what to do next?", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you sneak back and pick about 8 apples and continue your way back")
                number = random.randint(1,4)
                if number == 1:
                    easygui.msgbox('creature: "I SAID GO AWAY."')
                    easygui.msgbox("the weird angry creature comes up and chucks you again (- 50 health)")
                    health = int(health) - 50
                    health = str(health)
                    death()
                    death += 1
                else:
                    easygui.msgbox("you make it back to the stranger mostly safe")
                    easygui.msgbox("you return and see the stranger standing with two beautiful black horses")
                    easygui.msgbox('you: "I got the apples you asked for"')
                    easygui.msgbox('stranger: "perfect chuck them here, then you should be on your way."')
                    easygui.msgbox("you jump on the larger horse and he speeds off to a nearby town. You say thanks and find a way to call home to come pick you up")
                    success = True
                    decision21 = False
            elif choice == choices[1]:
                easygui.msgbox("you return and see the stranger standing with two beautiful black horses")
                easygui.msgbox("I'm so sorry I couldn't get any apples")
                easygui.msgbox("stranger: that's ok turns out they just had a feast with the monkeys, and they are happy to help you")
                easygui.msgbox("you jump on the larger horse. and he speeds off to a near by town. you say thanks and find a way to call home to come pick you up")
                success = True
                decision21 = False 
            elif choice == choices[2]:
                decision13 = True
                decision21 = False
        #decision22
        while decision22 == True:
            score += 1
            choices = ("get it hot","try use a sharp rock","try and leave")
            choice = easygui.buttonbox("how do you break the chain?", "health :" + health, choices)
            if choice == choices[3]:
                easygui.msgbox("explain that you need to go get something and go back to the stranger and explain you couldn't get any apples, before he kills you ")
                easygui.msgbox("you return and see the stranger standing with two beautiful black horses")
                easygui.msgbox("I'm so sorry I couldn't get any apples")
                easygui.msgbox("stranger: that's ok turns out they just had a feast with the monkeys, and they are happy to help you")
                easygui.msgbox("you jump on the larger horse and he speeds off to a near by town. you say thanks and find a way to call home to come pick you up")
                success = True
                decision22 = False
            elif choice == choices[1]:
                easygui.msgbox("you use the rock and hit the chain multiple times, you slip and accidently hit the creature. he reacts and hits you back (- 25 health)")
                health = int(health) - 25
                health = str(health)
                choices = ("try and heat up the chain first", "keep using the rock")
                choice = easygui.buttonbox("how do you break the chain?", "health :" + health, choices)
            if choice == choices[0]:
                easygui.msgbox("you light a fire (with the creatures help) and heat up the chain until it begins to glow")
                easygui.msgbox("you find a near by rock and try to break the chain")
                easygui.msgbox("it makes a large cut in the chain and you try to un-hook the other side ouch that is hot (-20 health)")
                health = int(health) - 20
                health = str(health)
                easygui("you cut the other side, and the creature is free, you take some apples and return to the stranger")
            elif choice == choices[1]:
                easygui.msgbox("you hit him again (-25) and again (-25 health) but the chain finally comes free and you return to the stranger")
                health = int(health) - 50
                health = str(health)
            easygui.msgbox("you return and see the stranger standing with two beautiful black horses")
            easygui.msgbox('you: "I got the apples you asked for"')
            easygui.msgbox('stranger: "perfect chuck them here, then you should be on your way."')
            easygui.msgbox("you jump on the larger horse and he speeds off to a nearby town. You say thanks and find a way to call home to come pick you up")
            success = True
            decision22 = False
    while success == True:
        easygui.msgbox("congratulations you have survived")
        finsihed = True
    while finished == True:
        easygui.msgbox(" your final score is " + score + "\n you died a total of " + death_count + " times" )
