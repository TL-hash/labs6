#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def get_train():
    """
    Запросить данные о поезде.
    """
    destination = input("Название пункта назначения? ")
    number = input("Номер поезда? ")
    time_str = input("Время отправления (ЧЧ:ММ)? ")

    try:
        departure_time = datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        print("Неверный формат времени. Используйте ЧЧ:ММ.", file=sys.stderr)
        return None

    return {
        'destination': destination,
        'number': number,
        'departure_time': departure_time
    }


def display_trains(trains_list):
    """
    Вывести список поездов в виде таблицы.
    """
    if not trains_list:
        print("Список поездов пуст.")
        return

    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 20,
        '-' * 15,
        '-' * 10
    )
    print(line)
    print(
        '| {:^20} | {:^15} | {:^10} |'.format(
            "Пункт назначения",
            "Номер поезда",
            "Время"
        )
    )
    print(line)

    for train in trains_list:
        print(
            '| {:<20} | {:<15} | {:>10} |'.format(
                train['destination'],
                train['number'],
                train['departure_time'].strftime("%H:%M")
            )
        )

    print(line)


def select_trains(trains_list, target_destination):
    """
    Выбрать поезда, направляющиеся в указанный пункт назначения.
    """
    return [
        train for train in trains_list
        if train['destination'].lower() == target_destination.lower()
    ]


def main():
    """
    Главная функция программы.
    """
    trains = []

    while True:
        command = input(">>> ").strip().lower()

        if command == 'exit':
            break

        elif command == 'add':
            train = get_train()
            if train is not None:
                trains.append(train)
                trains.sort(key=lambda item: item['departure_time'])

        elif command == 'list':
            display_trains(trains)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            if len(parts) < 2:
                print("Не указано название пункта назначения.", file=sys.stderr)
                continue

            target_destination = parts[1].strip()
            found_trains = select_trains(trains, target_destination)

            if found_trains:
                print(f"\nПоезда, направляющиеся в {target_destination}:")
                for train in found_trains:
                    print(
                        f"  Поезд №{train['number']}, отправление в {train['departure_time'].strftime('%H:%M')}"
                    )
            else:
                print(f"Поездов в пункт '{target_destination}' не найдено.")

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить информацию о поезде;")
            print("list - вывести список всех поездов;")
            print("select <пункт> - показать поезда, идущие в указанный пункт;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда: {command}", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())