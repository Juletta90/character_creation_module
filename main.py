from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().

#from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Функция описывает урон противнику."""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон противнику '
                f'равный {5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    """Функция описывает блокировку удара."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал '
                f'{10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал '
                f'{10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал '
                f'{10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str) -> str:
    """Функция описывает специальные навыки."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное '
                f'умение «выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное '
                f'умение «атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное '
                f'умение «защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """Функция описывает выбор героя."""
    if char_class == 'warrior':
        print(f'{char_name}, ты воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты лекарь — чародей, способный исцелять раны.')
    print('потренируйся управлять своими навыками.')
    print('введи одну из команд: attack — чтобы атаковать '
          'противника, defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'тренировка окончена.'


def choice_char_class() -> str:
    """Функция описывает приветствие."""
    approve_choice: str = ''  # None
    char_class: str = ''      # None
    while approve_choice != 'y':
        char_class = input(
            'введи название персонажа, за которого хочешь играть: '
            'воитель — warrior, маг — mage, лекарь — healer: ')
        if char_class == 'warrior':
            print('воитель — дерзкий воин ближнего боя.'
                  'сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('маг — находчивый воин дальнего боя.'
                  'обладает высоким интеллектом.')
        if char_class == 'healer':
            print('лекарь — могущественный заклинатель.'
                  'черпает силы из природы, веры и духов.')
        approve_choice = input('нажми (y), чтобы подтвердить выбор,'
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


#if __name__ == '__main__':
#    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


#_____________________________________________________________________

TEST_DATA: list[tuple[int, str, bool]] = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: int, buf_effect: bool) -> float:
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(current_rep: float,
               rep_points: int, debuf_effect: bool) -> float:
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: str) -> str:
    current_rep: float = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return f"""После {len(duel_res)} поединков,
 репутация персонажа — {current_rep:.3f} очков."""


# Тестовый вызов функции main.
print(main(TEST_DATA))




