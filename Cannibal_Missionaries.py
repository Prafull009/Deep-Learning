def display(bpass1, bpass2):
    print("\n\n\n")
    for _ in range(fm):
        print(" M ", end="")
    for _ in range(fc):
        print(" C ", end="")
    if flag == 0:
        print(f" __________WATER___________B0({bpass1},{bpass2})AT ", end="")
    else:
        print(f" BO({bpass1},{bpass2})AT__________WATER___________ ", end="")
    for _ in range(im):
        print(" M ", end="")
    for _ in range(ic):
        print(" C ", end="")
    print()

def win():
    return not (fc == 3 and fm == 3)

def solution():
    global fm, fc, im, ic, flag, select
    while win():
        if flag == 0:
            if select == 1:
                display('C', ' ')
                ic += 1
            elif select == 2:
                display('C', 'M')
                ic += 1
                im += 1
            if ((im - 2) >= ic and (fm + 2) >= fc) or (im - 2) == 0:
                im -= 2
                select = 1
                display('M', 'M')
                flag = 1
            elif (ic - 2) < im and (fm == 0 or (fc + 2) <= fm) or im == 0:
                ic -= 2
                select = 2
                display('C', 'C')
                flag = 1
            elif (ic <= im and fm >= fc):
                ic -= 1
                im -= 1
                select = 3
                display('M', 'C')
                flag = 1
        else:
            if select == 1:
                display('M', 'M')
                fm += 2
            elif select == 2:
                display('C', 'C')
                fc += 2
            elif select == 3:
                display('M', 'C')
                fc += 1
                fm += 1
            if win():
                if ((fc > 1 and fm == 0) or im == 0):
                    fc -= 1
                    select = 1
                    display('C', ' ')
                    flag = 0
                elif (ic + 2) > im:
                    fc -= 1
                    fm -= 1
                    select = 2
                    display('C', 'M')
                    flag = 0

fm, fc, im, ic = 0, 0, 3, 3
flag, select = 0, 0
print("MISSIONARIES AND CANNIBALS")
display(' ', ' ')
solution()
display(' ', ' ')
print("\n\n")
