# This is a sample Python script.
import random


def check_number() -> int:
    """Проверка ввода игроком цифры 1 или 2 : драться или  бежать"""
    while True:
        try:
            input_num = int(input('Введите число 1 или 2: '))  # type:int
            assert 1 <= input_num <= 2
            if input_num == 1:
                return 1
            if input_num == 2:
                break
        except ValueError:
            print("Введите пожалуйста число,а не буквы")
        except AssertionError:
            print("Введите пожалуйста числа 1 или 2")
        else:
            break
    return 0


def fight_program(creatures: dict) -> dict:
    """Программа по запуску битвы рыцаря и монстра"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # type:list
    random_numbers_health = random.choice(numbers)  # type:list
    random_numbers_power = random.choice(numbers)  # type:list
    creatures["monster"]["health"] = random_numbers_health
    creatures["monster"]["power"] = random_numbers_power
    print(f'БОЙ! Вы встретили чудовище {random_numbers_health} жизнями и с силой удара {random_numbers_power}')
    while creatures["knight"]["health"] > 0:
        creatures["knight"]["health"] = creatures["knight"]["health"] - creatures["monster"]["power"]
        creatures["monster"]["health"] = creatures["monster"]["health"] - creatures["knight"]["power"]
        if creatures["knight"]["health"] < 0:
            break
        if creatures["monster"]["health"] < 0:
            creatures["knight"]["victory"] = creatures["knight"]["victory"] + 1
            creatures["monster"]["health"] = 1
            creatures["monster"]["power"] = 1
            print(
                f'Победа!Вы одержали верх над чудовищем!У вас осталось {creatures["knight"]["health"]} единиц здоровья')
            return creatures
    return creatures


def health_program(creatures : dict) -> dict:
    """Программа по пополнению здоровья рыцарю"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # type:list
    random_numbers = random.choice(numbers)  # type:list
    creatures["knight"]["health"] = creatures["knight"]["health"] + random_numbers
    if creatures["knight"]["health"] > 100:
        creatures["knight"]["health"] = 100
        print(f'Вы достигли максимума здоровья!100 едининц')
    print(f'Вы достигли уровня здоровья {creatures["knight"]["health"]} единиц!')
    return creatures


def power_program(creatures: dict) -> dict:
    """Программа по пополнению мощности оружия рыцаря"""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # type:list
    random_numbers = random.choice(numbers)  # type:list
    creatures["knight"]["power"] = creatures["knight"]["power"] + random_numbers
    if creatures["knight"]["power"] > 100:
        creatures["knight"]["power"] = 100
        print(f'Вы достигли максимума силы!100 едининц')
    print(f'Вы достигли уровня силы {creatures["knight"]["power"]} единиц!')
    return creatures


def main() -> int:
    """Основной блок программы"""
    creatures = {'knight': {'health': 10, 'power': 10, 'victory': 0},
                 'monster': {'health': 1, 'power': 1}}
    type_of_move = [1, 2, 3]
    """Ходы рыцаря : (1)битва,пополнение (2)здоровья или (3)оружия"""
    while creatures['knight']['health'] > 0 and creatures['knight']['victory'] <= 10:
        random_move = random.choice(type_of_move)
        """Генерация раномного хода рыцаря"""
        if random_move == 1:
            if check_number() == 1:
                creatures = fight_program(creatures)
        elif random_move == 2:
            health_program(creatures)
        elif random_move == 3:
            power_program(creatures)
    if creatures['knight']['health'] < 0:
        print(f'Бой проигран')
    if creatures['knight']['health'] > 0 and creatures['knight']['victory'] >= 10:
        print(f'Вы победили!')
    return 0


if __name__ == "__main__":
    """К сожалению оформил без глобальных переменных,только под конец увидел"""
    main()
