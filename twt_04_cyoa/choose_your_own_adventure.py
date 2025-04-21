def game():
    name = input("Введите ваше имя: ")
    print("Приветствую", name, "в этом приключении!")

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
        0: ("Вы находитесь на даче. Вы можете пойти налево *left* в лес или направо *right* к магазину. Также можно закончить *end* игру",
            {"left": 1, "right": 2, "end": 5}),
        1: ("Вы направляетесь к лесу. {}".format(
            "По пути вы видите фонарь, лежащий у канавы. Вы можете поднять *pick* его, " if items_in_game["light"] else "Вы можете ") +
            "пойти вперед *foreward* к лесу или повернуть назад *return* к дому.",
            {"pick": 3, "foreward": 4, "return": 0}),
        2: ("Вы пришли к магазину. Он закрыт. Вы можете вернуться *return* к дому",
            {"return": 0}),
        3: ("Вы подняли фонарь. Вы можете пойти вперед *foreward* к лесу или повернуть назад *return* к дому.",
            {"foreward": 4, "return": 0}, pick_light),
        4: ("Вы пришли в лес. Тут очень темно. Вы можете вернутья назад *return* к дому.",
            {"return": 0}),
        5: ("Спасибо за игру. Всего хорошего, {}".format(name),
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
            choose = input("Ваши действия ({}): ".format("/".join(options.keys())))

        current_pos = options[choose]

game()
