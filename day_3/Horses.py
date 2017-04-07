import random


class Horse:
    def __init__(self, name, count = 0):
        self.name = name
        self.count = count

    def go_steps(self, step):
        self.count += step

    def get_name(self):
        return self.name

if __name__ == '__main__':
    count_1, count_2, g_count = 0, 0, 0
    step_1, step_2 = 0, 0
    horse_1 = Horse('Tranquilo')
    horse_2 = Horse('Alocado')
    print("Horse 1 is", horse_1.get_name().upper())
    print("Horse 2 is", horse_2.get_name().upper(), "\n")

    while True:
        g_count += 1
        print("Pasada #", g_count)
        step_1 = random.randrange(6)
        horse_1.go_steps(step_1)
        print("Horse #1 advance: ", step_1)
        step_2 = random.randrange(6)
        horse_2.go_steps(step_2)
        print("Horse #2 advance: ", step_2)
        count_1, count_2 = horse_1.count, horse_2.count
        print("-->Horse #1 is on ", count_1)
        print("-->Horse #2 is on ", count_2)

        if count_1 >= 20 or count_2 >= 20:
            break

    if count_1 == 20 and count_2 == 20:
        print("Tie")
    elif count_1 > count_2:
        print("The winner is: ", horse_1.get_name())
    else:
        print("The winner is: ", horse_2.get_name())