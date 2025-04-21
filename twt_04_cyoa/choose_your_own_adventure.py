def game():
    name = input("Input your name: ")
    print("Hello", name, "in this adventure!")

    items_in_game = {
        "light": True
    }

    items_in_inventory = set()

    def pick(item):
        if item in items_in_game and items_in_game[item] is True:
            items_in_game[item] = False
            items_in_inventory.add(item)

    def pick_light(core):
        pick("light")

        text, opt = core[1]
        opt.pop("pick", None)
        core[1] = (text, opt)

    core = {
        0: ("You are in the countryhouse. You could go left to the forest or right to the shop. Also you could end the game.\n"
            "Type: left - go to the forest; right - go to the shop; end - end the game.",
            {"left": 1, "right": 2, "end": 5}),
        1: ("You are going to the forest. {} go foreward to the forest or return back to home.\n"
            "Type: {}foreward - go to the forest; return - go back to home"
            .format("On the road you see the light. You could pick it," if items_in_game["light"] else "You could",
                    "pick - pick the light; " if items_in_game["light"] else ""),
            {"pick": 3, "foreward": 4, "return": 0}),
        2: ("You came to the shop. It is closed. You could return back to home",
            {"return": 0}),
        3: ("You have picked the light. You could go to the forest or return back to home.",
            {"foreward": 4, "return": 0}, pick_light),
        4: ("You came to the forest. It is too dark. You could return back to home.",
            {"return": 0}),
        5: ("Thank you for the game! Buy, {}".format(name),
            {})
    }

    current_pos = 0
    while True:
        print(items_in_game)
        if len(core[current_pos]) == 3:
            text, options, action = core[current_pos]
            action(core)
        else:
            text, options = core[current_pos]

        print(text)
        if not options:
            break

        choose = ""
        while choose not in options.keys():
            choose = input("Your actions ({}): ".format("/".join(options.keys())))

        current_pos = options[choose]

game()
