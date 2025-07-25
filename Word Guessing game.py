#This is Hangman, except that the man is already hanged.......
import random  #Got the below one from Gemini,it didn't have commas after words so i was not able to directly make them into a list,Sooo the method below is what i used to make that list!
words="APPLE, BAKER, CANDY, DREAM, EAGLE, FAITH, GRAPE, HOUSE, IVORY, JEWEL, KNIFE, LEMON, MAGIC, NIGHT, OCEAN, PLANT, QUEEN, ROBOT, SHAPE, TABLE, UNION, VALUE, WATCH, XENON, YOUTH, ZEBRA, ABOUT, ABOVE, ACTOR, ACUTE, ADMIT, ADOPT, ADULT, AFTER, AGAIN, AGENT, AGREE, AHEAD, ALARM, ALIVE, ALLOW, ALONG, ALTER, AMBER, AMPLY, ANGEL, ANGER, ANGLE, ANGRY, ANKLE, APART, APPLY, ARENA, ARGUE, ARISE, AROMA, ARRAY, ASIDE, ASSAY, ASSET, AUDIO, AUDIT, AVOID, AWAKE, AWARD, AWARE, AWFUL, BADGE, BADLY, BASIC, BASIN, BASSY, BATCH, BATHS, BEACH, BEGIN, BEING, BELOW, BENCH, BENTO, BIRCH, BIRDS, BLADE, BLAME, BLIND, BLOCK, BLOOD, BOARD, BOAST, BONUS, BOOST, BOOTS, BOOTH, BOUND, BRAIN, BRAND, BRAVE, BREAD, BREAK, BRIBE, BRICK, BRING, BROAD, BROWN, BRUSH, BUILD, BULKY, BUNCH, BURST, CABIN, CABLE, CACHE, CACTI, CATCH, CAUSE, CEASE, CHAIN, CHAIR, CHALK, CHAMP, CHANT, CHAOS, CHARM, CHART, CHASE, CHEAP, CHECK, CHEER, CHEST, CHIEF, CHILD, CHILL, CHINA, CHOKE, CHORD, CHUNK, CIVIL, CLAIM, CLASH, CLASS, CLEAN, CLEAR, CLERK, CLICK, CLIFF, CLING, CLOCK, CLOSE, CLOUD, CLOWN, COAST, COLOR, COMET, COMFY, COMIC, CRANK, CRASH, CRAVE, CRAZY, CREAM, CRIME, CRISP, CROWN, CRUDE, CRUEL, CRUMB, CRUSH, CRYPT, CUBIC, CURLY, CYNIC, DAISY, DANCE, DANDY, DREAM, DRINK, DRIVE, DRONE, DRYER, DUCHY, DULLY, DUMMY, DUSTY, EAGER, EARLY, EARTH, EASEL, EASYB, EATEN, EBONY, ECHOE, EDGEP, EIGHT, ELECT, ELITE, EMPTY, ENJOY, ENTER, ENTRY, EQUAL, ERROR, ESSAY, ETHIC, EVADE, EVENT, EVERY, EXACT, EXCEL, EXERT, EXIST, EXPEL, EXTRA, FABLE, FACET, FAIRY, FALSE, FANCY, FANCY, FANCY, FARMS, FAULT, FAVOR, FEAST, FEWER, FIELD, FIERY, FIFTH, FIFTY, FIGHT, FINAL, FIRST, FLAME, FLARE, FLASH, FLEET, FLESH, FLICK, FLING, FLOOR, FLOUR, FLUID, FLUSH, OPENH, OPERA, OTHER, OUTDO, OUTER, OVALS, OZONE, PACER, PADDY, PANIC, PAPER, PARKS, PARTY, PASTA, PASTE, PATCH, PATIO, PAUSE, PEACE, PEARL, PECAN, PENAL, PERCH, PERIL, PHOTO, PIANO, PICKS, PILOT, PINCH, PINEA, PINKY, PITCH, PLACE, PLAIN, PLANE, PLANK, PLATE, PLAZA, PLEAD, PLUCK, POINT, POISE, POLAR, POLES, PORCH, POUND, POWER, PRAYE, PRESS, PRICE, PRIDE, PRIME, PRINT, PRIOR, PRIZE, PROBE, PROOF, OZONE, PACER, PADDY, PANIC, PAPER, PARKS, PARTY, PASTA, PASTE, PATCH, PATIO, PAUSE, PEACE, PEARL, PECAN, PENAL, PERCH, PERIL, PHOTO, PIANO, PICKS, PILOT, PINCH, PINEA, PINKY, PITCH, PLACE, PLAIN, PLANE, PLANK, PLATE, PLAZA, PLEAD, PLUCK, POINT, POISE, POLAR, POLES, PORCH, POUND, POWER, PRAYE, PRESS, PRICE, PRIDE, PRIME, PRINT, PRIOR, PRIZE, PROBE, PROOF, PULSE, PUPIL, PUREL, PURGE, PURSE, PUSHU, QUAKE, QUALM, QUART, QUERY, QUEST, QUICK, QUIET, QUILL, QUILT, QUITE, QUOTA, RADAR, RADIO, RAISE, RALLY, RAMPS, RANCH, RANGE, RAPID, RASPY, RIVAL, RIVER, ROADS, ROAST, ROBIN, ROBOT, ROCHA, ROCKY, ROGUE, ROMAN, ROUGH, ROUND, ROUTE, ROYAL, RUDDY, RUGBY, RUINS, RULER, RUMOR, RURAL, RUSTY, SABER, SALAD, SALES, SALLY, SALON, SALTY, SALVE, SAMBA, SANCT, SANDY, SAUCE, SCALE, SCALY, SCAMP, SCANS, SCARE, SCENE, SCENT, SCOOP, SCOPE, SCORE, SCOUT, SCRAP, SCREW, SHADE, SHADY, SHAKE, SHALL, SHAME, SHAPE, SHARE, SHARK, SHARP, SHEAR, SHINE, SHINY, SHIRT, SHOCK, SHOOT, SHORE, SHORT, SHOTS, SHOUT, SHOVE, SHOWN, SIGHT, SIGMA, SIGNS, SILAS, SILKY, SILLY, SILVA, SIMON, SINGS, SINKC, SIXTH, SKILL, SKINS, SKIRT, SKULL, SLACK, SLATE, SLAVE, SLEEK, SLEEP, SLEET, SLICE, SLICK, SLIDE, SLING, SLOPE, SMACK, SMALL, SMART, SMELL, SMILE, SMOGG, SMOKE, SMOKY, SNACK, SNAIL, SNAKE, SNEAK, SNEER, SNIFF, SNORT, SNOWY, SOAPY, SOBER, SOLAR, SOLID, SOLVE, SONAR, SONGS, SONIC, SOUND, SOUPY, SPACE, SPARE, SPARK, SPEAR, SPELL, SPEND, SPICE, SPICY, SPIKE, SPINE, SPIRL, SPLIT, SPOIL, SPOKE, SPORT, SPOTL, SPRAT, SPRAY, SPREE, SQUAD, SQUAT, STAFF, STAGE, STAIN, STAIR, STAKE, STALL, STAMP, STAND, STARE, START, STATE, STAYS, STEAL, STEAM, STEEL, STEEP, STEER, STICK, STIFF, STILL, STING, STOCK, STONE, STOOL, STOPP, STORE, STORM, STORY, STRAP, STRAW, STRAY, STRIP, STUDY, STUFF, STUMP, STYLE, SUGAR, SUING, SUITE, SUNNY, SUPER, SUREL, SURGE, SWEEP, SWEET, SWELL, SWIFT, SWIML, SWING, SWIRL, SYRUP, TABLE, TACOS, TAKEN, TALES, TALLY, TANGO, TAPES, TAROT, TASTE, TASTY, TEACH, TEAMS, TEARS, TEASE, TEDDY, TEMPO, TENSE, TENTH, TEXAS, THAWY, THEIR, THEME, THESE, THICK, THIEF, THING, THINK, THIRD, THORN, THREE, THROW, THUMB, TIARA, TIGHT, TIMER, TODAY, TOKEN, TONGS, TOPIC, TOTAL, TOUCH, TOUGH, TOWEL, TOWER, TOXIC, TRACE, TRACK, TRADE, TRAIL, TRAIN, TRASH, TREAD, TREAT, TREND, TRIBE, TRICK, TRIED, TRIPE, TRIPN, TROOP, TRUCK, TRULY, TRUST, TRUTH, TUBES, TULIP, TUMOR, TUNEG, TURBO, TURNS, TWICE, TWINE, TWIRL, ULTRA, UNCLE, UNDER, UNION, UNTIL, UPPER, URBAN, USAGE, USUAL, UTTER, VAGUE, VALID, VALUE, VALVE, VAPOR, VAULT, VEGAN, VENOM, VENUE, VERGE, VERSE, VIDEO, VIGOR, VINYL, VIRAL, VITAL, VIVID, VOCAL, VODKA, VOICE, VOIDB, VOLTS, VOTER, WAGON, WAIST, WALKS, WALTZ, WANTS, WARLY, WATCH, WATER, WAVED, WEARY, WEAVE, WEDGE, WEIGH, WEIRD, WHALE, WHARF, WHEAT, WHEEL, WHERE, WHICH, WHILE, WHITE, WHOLE, WHORE, WIDTH, WIGHT, WILDW, WINCE, WINDY, WINGS, WINKS, WINTER, WIPES, WIRES, WISEL, WISHY, WOMAN, WOMEN, WORLD, WORRY, WORSE, WORTH, WOUND, WOVEN, WRATH, WRIST, WRITE, WRONG, YACHT, YIELD, YOUNG, YOURS, YOUTH, YUMMY, ZEBRA, ZEROX, ZILCH, ZINGS, ZONAL ,$,"
new_words=[]
ek_word=""
k=o=0
t=True
while t: #If it were True instead of t,new_words was getting appended by alotta commmas by its end so to solve this problem i introduced t
    char=words[k]
    if char=="$":
        break
    while t:
        charc=words[o]
        if o==5116:
            t=False
            break
        if charc==",":
            o=o+1
            break
        o+=1
        if not charc==" ": #To remove that extra space blank every word was getting
           ek_word=ek_word+charc
    new_words.append(ek_word)
    ek_word=""
    k+=1
#print(words.index("$")) I introduced a dollar sign at the very end of word,as a checkpoint
#print(new_words) #To check what was the list that i was getting
k=random.randint(0,len(new_words)-1)
ek_word=new_words[k]
p=True
while p:
    print("Alrighty,sooo this is like a walmart version of HANGMAN that i made and to not make it gore,i won't hang anyone.....yet :)")
    print("I have already chosen a 5 lettered word and you have 4 chances to guess the correct word")
    print("If the letter you've typed is not present in the word that i've chosen then i'd replace it with '-'")
    print("If the letter that you've typed is present in the exact position that it is in the actual word then i'd replace it with the same letter but in UPPERCASE")
    print("If the letter that you've typed in is present in the word but not in the position as it is in the actual word then i'd replace it with the same letter but in LOWERCASE")
    print("Remember you have only 3 tries")
    o=3
    k=0
    print("SOOOO,go ahead,type in that 5 lettered word that you think that i'm thinking")
    b=t=True
    word=""
    while t:
        word=""
        if not o<=0:
            print(f"You currently {o} chances left")
            attempt=input("Give your shot")
            if len(attempt)==5 or not attempt.isalpha():
                for i in range(5):
                    char=attempt[i]
                    if not char in ek_word.lower():
                        word=word+"-"
                    else:
                        if char==ek_word[i].lower():
                            word=word+char.upper()
                        else:
                            word=word+char.lower()
                o-=1
                print(word)
                if attempt==ek_word.lower():
                    t=b=False
            else:
                if k==0:
                    print("OHH MY GAWWDD!!!,INPUT A FIVE LETTERED WORD!!....YOU KNOW FIVE?,THAT RHYMES WITH LIFE?,SOMETHING THAT YOU DON'T HAVE!!")
                if k==1:
                    print("BRO ARE YOU SERIOUS!!!???....YOUR INTELLIGENCE IS THE SOLE REASON THAT ALIENS AVOID EARTH!!!")
                    print("JUST TYPE IN A FIVE LETTERED WORDDDD!!!!")
                if k==2:
                    print("LAST CHANCE!!...I AM GIVING YOU LAST CHANCE TO REDEEM YOURSELF!!..DO NOT MESS THIS UP!!!...*GUN CLICKS*🔫🔫")
                    print("TYPE IN A FIVE LETTERED WORD.....PWEASEEEEEE!!!! (┬┬﹏┬┬)")
                if k>2:
                    print("I QUIT")
                    t=False
                k+=1
        else:
            break
    if not b and not t:
        print(f"CONGRATULATIONS!!...YOU GUESSED THE WORD, YES IT WAS {ek_word}")
    if b and not t:
        print("OH NO NO NO....YOU DON'T EVEN DESERVE A REPLY AFTER SOO MANY ERRORS🤬🤬")
    if b and t:
        print(F"YOU RAN OUT OF TRIES,THE WORD WAS {ek_word}")
    play_again=input("Would you like to play again?(Y/N)")
    if play_again.upper()=="Y":
        p=True
    elif play_again.upper()=="N":
        p=False
    else:
        print("*SIGH*......You didn't follow the code....never mind,not the first time you're disappointing someone....i take it as a yes ")
        p=True
print("Thank you for playing!!")