import random
import os
import platform

if platform.system() == 'Windows':
    from msvcrt import getch
else:
    print("")

STRING_N = 20
COLUMN_N = 70
GOAL = 20000
START_SCORE = 0

CAR_X = 1
GAME_STATUS = 'On'

# вероятность что каждый n-ый объект трассы будет препятствием, где n - complexity
complexity = 5

car_symb = ">"
track_line_symb = "="
track_obstacle_symb = "#"

car_symb_2d = "O O==>O O"
track_line_symb_2d = "---   ---"
track_obstacle_symb_2d = "#u#fagbro"

NUMBER_OF_D = int(len(car_symb_2d) ** (1/2))

main_track_list = [[0 for i in range(COLUMN_N)] for j in range(STRING_N)]
main_track_list[CAR_X][0] = 2


def obstacle_gen(obstacle_list, difficulty):
    for string in range(STRING_N):
        if random.randint(1, difficulty) // difficulty == 1:
            obstacle_list[string][COLUMN_N - 1] = 1


def command_input():
    global GAME_STATUS
    while True:
        command = ord(getch())
        if command == 27:  # ESC
            GAME_STATUS = "lose"
            break
        elif command == 224:  # Special keys (arrows, f keys, ins, del, etc.)
            command = ord(getch())
            if command == 72:  # Up
                return "UP"
            elif command == 80:  # Down
                return "DOWN"
            elif command == 77:  # Right
                return "FORWARD"
            # Left == 75

            # else:
            #     return command_input()


def move_car_forward(track_list):
    global CAR_X, GAME_STATUS, STRING_N
    input_cmd = command_input()
    if input_cmd == "UP":
        if CAR_X > 0:
            if track_list[CAR_X-1][1] != 1:
                CAR_X -= 1
                track_list[CAR_X][1] = 2
            else:
                GAME_STATUS = "lose"
        else:
            # print("Can't move, the limit is reached")
            # move_car_forward(track_list)
            if track_list[STRING_N-1][1] != 1:
                CAR_X = STRING_N-1
                track_list[CAR_X][1] = 2
            else:
                GAME_STATUS = "lose"
    elif input_cmd == "DOWN":
        if CAR_X < STRING_N - 1:
            if track_list[CAR_X+1][1] != 1:
                CAR_X += 1
                track_list[CAR_X][1] = 2
            else:
                GAME_STATUS = "lose"
        else:
            # print("Can't move, the limit is reached")
            # move_car_forward(track_list)
            if track_list[0][1] != 1:
                CAR_X = 0
                track_list[CAR_X][1] = 2
            else:
                GAME_STATUS = "lose"

    else:
        if track_list[CAR_X][1] != 1:
            track_list[CAR_X][1] = 2
        else:
            GAME_STATUS = "lose"


def move_track_forward(track_list):
    for string in range(STRING_N):
        track_list[string].pop(0)
        track_list[string].append(0)


def move_forward(track_list, difficulty):
    move_car_forward(track_list)
    move_track_forward(track_list)
    obstacle_gen(track_list, difficulty)


def main_cycle(track_list, difficulty, car, track, obstacle):
    global GAME_STATUS, START_SCORE, GOAL
    while True:
        os.system('cls')
        print("Welcome to the game, your score: {}, your goal: {}".format(START_SCORE + 1, GOAL))
        track_print(track_list, car, track, obstacle)
        # track_print_2d(track_list, car, track, obstacle, NUMBER_OF_D)
        move_forward(track_list, difficulty)
        if GAME_STATUS == "lose":
            print("YOU FAILED")
            break
        START_SCORE += 1
        if START_SCORE == GOAL:
            print('You win, gr8, m8')
            break


def track_print(track_list, car, track, obstacle):
    for string in range(STRING_N):
        for symbol in track_list[string]:
            if symbol == 0:
                print(track, end='')
            elif symbol == 2:
                print(car, end='')
            else:
                print(obstacle, end='')
        print()


def track_print_2d(track_list, car, track, obstacle, number_of_d):
    for string in range(STRING_N):
        for d in range(number_of_d):
            for symbol in track_list[string]:
                if symbol == 0:
                    print(track[d*number_of_d:(d+1)*number_of_d], end='')
                elif symbol == 2:
                    print(car[d*number_of_d:(d+1)*number_of_d], end='')
                else:
                    print(obstacle[d*number_of_d:(d+1)*number_of_d], end='')
            print()
    print()

main_cycle(main_track_list, complexity, car_symb, track_line_symb, track_obstacle_symb)
# main_cycle(main_track_list, complexity, car_symb_2d, track_line_symb_2d, track_obstacle_symb_2d)
