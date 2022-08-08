import easygui
score = 0
health = "100"
decision2 = True
while decision2 == True:
            score += 1
            choices = ("something exciting", "just walk around trying to find anything", "a water source")
            choice = easygui.buttonbox("what should you try and find?", "health :" + health, choices)
            if choice == choices[0] or choice == choices[1]:
                easygui.msgbox("you stumble across a abandon temple. covered in spiderwebs and old food scraps")
                decision10 = True
                decision2 = False
            elif choice == choices[2]:
                decision9 = True
                decision2 = False