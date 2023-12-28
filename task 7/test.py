for i in range(1,10):
    print(i)

for num in range(0,3):
    print(num)

    num = 66
    print(num)

#example 2
    list_wizards = ["fdf", "dfdf", "fdfd", "cow", "goat"]
    for wizard in list_wizards:
        print(wizard)
        print("----------------")
#example 3
        total = 0
        for number in range(1,6):
            print(f"the current value of number is : {number}")
            print(f"The current total is : {total}")
            total += number
            print(f"sum : {total}")
            print("********************")

#example4
        pokemons = ["test", "test2", "deer", "super", "kapoor"]
        # index = 0

        # for x in pokemons:
        #     print(index, x)
        #     index +=1
        # for count, poke in enumerate(pokemons, 1000):
        #     print(count, poke)
        print(pokemons[1])
        for pos, poke in enumerate(pokemons, 0):
            # if poke == "super":
                if poke in ["test", "test2", "deer", "super", "kapoor"]:
                #print(f"super is your{pos} pokemon")
                     print(f"{poke} you are fire type")
                else:
                     print(f"{poke} you are different type")

                break
