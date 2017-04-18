lab_list = [['1', '1', '*', '1', '1', '1', '1', '1', '1'],
            ['1', '1', '0', '0', '0', '0', '1', '0', '1'],
            ['1', '1', '1', '1', '1', '0', '1', '0', '1'],
            ['1', '1', '0', '0', '0', '0', '0', '0', '1'],
            ['1', '1', '0', '1', '1', '1', '1', '0', '1'],
            ['1', '0', '0', '0', '0', '0', '0', '1', '1'],
            ['1', '1', '1', '1', '1', '#', '1', '1', '1']]


def display_map():
    global lab_list
    for i in range(len(lab_list)):
        for j in range(len(lab_list[i])):
            print(lab_list[i][j] + "\t", end="")
        print()


def search_asterisc(lab):
    for i in range(len(lab)):
        for j in range(len(lab[i])):
            if lab[i][j] == '*':
                return i, j


def check_move(choose):
    global lab_list
    aux_flag = ''
    i_pos, j_pos = search_asterisc(lab_list)
    if choose == 'L':
        if lab_list[i_pos][j_pos - 1] != '1':
            print("To left <--")
            aux_flag = lab_list[i_pos][j_pos - 1]
            lab_list[i_pos][j_pos] = '0'
            lab_list[i_pos][j_pos - 1] = '*'
        else:
            print("MUAHAHA HERE IS THE WALL")
    elif choose == 'R':
        if lab_list[i_pos][j_pos + 1] != '1':
            print("To right -->")
            aux_flag = lab_list[i_pos][j_pos + 1]
            lab_list[i_pos][j_pos] = '0'
            lab_list[i_pos][j_pos + 1] = '*'
        else:
            print("MUAHAHA HERE IS THE WALL")
    elif choose == 'U':
        if lab_list[i_pos - 1][j_pos] != '1':
            print("      A")
            print("To up |")
            aux_flag = lab_list[i_pos - 1][j_pos]
            lab_list[i_pos][j_pos] = '0'
            lab_list[i_pos - 1][j_pos] = '*'
        else:
            print("MUAHAHA HERE IS THE WALL")
    elif choose == 'D':
        if lab_list[i_pos + 1][j_pos] != '1':
            print("To down |")
            print("        V")
            aux_flag = lab_list[i_pos + 1][j_pos]
            lab_list[i_pos][j_pos] = '0'
            lab_list[i_pos + 1][j_pos] = '*'
        else:
            print("MUAHAHA HERE IS THE WALL")
    elif choose == 'display':
        display_map()
        return ''

    return aux_flag


def main():
    flag = ''
    print("================= WELCOME TO THE GAME OF BEHEMONTH lml ===========")
    print("***************** Can you escape from hell?            ***********")
    print(">>L-->Left >>R-->Right >>U-->Up >>D-->Down")
    while flag != '#':
        option = input("Enter your choose [L|R|U|D] >> ")
        flag = check_move(option)
    print("=============================")
    print("= YOU ARE THE WINNER!!! lml =")
    print("=============================")


if __name__ == '__main__':
    main()
