from random import choice


def game(bot, player):
    if player == bot:
        print('Ничья\n')
    elif player == 'Камень' and bot == 'Бумага' or player == 'Ножницы' and bot == 'Камень' or player == 'Бумага' and \
            bot == 'Ножницы':
        print('Ты проиграл\n')
    else:
        print('Ты выиграл!\n')


def main():
    choice_list = ['Камень', 'Ножницы', 'Бумага']
    player_choice = choice_list[int(input('1)Камень\n'
                                          '2)Ножницы\n'
                                          '3)Бумага\n')) - 1]
    bot_choice = choice(choice_list)
    game(bot_choice, player_choice)
    if input('Хочешь сыграть еще раз? y/n\n') == 'y':
        main()
    else:
        print('Ну ладно, пока\n')


if __name__ == '__main__':
    main()