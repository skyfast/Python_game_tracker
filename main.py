import counter
import datetime
TARGET_COUNT = 2200
FILE = "count"
ENDDATE = datetime.datetime(2021, 1, 11)


def show_hud(tracker):
    print("Hello, Welcome back to the LOL grind")
    print(f"Points {tracker.show_count()} / {TARGET_COUNT}")
    print(f"{tracker.show_left()} more needed!")
    print(f"days left: {tracker.time_left()}")


def get_input():
    return input("What would you like to do?")


def handle_input(user_input, counter):
    if user_input == "w":
        counter.take_a_win()
    elif user_input == "l":
        counter.take_a_lose()
    elif user_input == "q":
        counter.take_a_bonus(int(input("How much was the quest worth?")))
    elif user_input == "r":
        counter.hard_reset(int(input("What do you need to reset it too?")))
    else:
        return


if __name__ == '__main__':
    counter = counter.CounterBoi(TARGET_COUNT, FILE, ENDDATE)

    user_input = ""

    while user_input != "e":
        show_hud(counter)
        user_input = get_input()
        handle_input(user_input, counter)

    counter.save(FILE)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
