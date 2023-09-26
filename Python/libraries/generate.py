# from random 
# coin = random.choice(["heads", "tails"])
# print(coin)


#    #ramdint
# import random
# number = random.randint(1,10)
# print(number)




#     #shuffle

# import random
# cards = ["Jack","Queen","King"]
# random.shuffle(cards)
# for card in cards:
#     print(card)


#     #statistics

# import statistics
# print(statistics.mean([100, 90]))



    #commandline interface, sys

# import sys
#         #check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("TOo many arguments")
#     #print the name tag
# print("Hello, my name is", sys.argv[1])



#       #slices
#  import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:]:
# print("Hello, my name is", arg)   

       
#         #packages

# import cowsay
# import sys
# if len(sys.argv) == 2:
#     cowsay.trex("Hello," + sys.argv[1])
