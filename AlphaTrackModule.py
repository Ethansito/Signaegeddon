X, Y, Z = 0, 1, 2
rightTipIds = [4, 8, 12, 16, 20]

def readAlpha(lm_list):
    pos = initVals(lm_list)
    return '_' if isSpace(lm_list, pos) \
        else 'A' if isA(lm_list, pos) \
        else 'B' if isB(lm_list, pos) \
        else 'C' if isC(lm_list, pos) \
        else 'D' if isD(lm_list, pos) \
        else 'E' if isE(lm_list, pos) \
        else 'F' if isF(lm_list, pos) \
        else 'G' if isG(lm_list, pos) \
        else 'H' if isH(lm_list, pos) \
        else 'I' if isI(lm_list, pos) \
        else 'J' if isJ(lm_list, pos) \
        else 'K' if isK(lm_list, pos) \
        else 'L' if isL(lm_list, pos) \
        else 'M' if isM(lm_list, pos) \
        else 'N' if isN(lm_list, pos) \
        else 'O' if isO(lm_list, pos) \
        else 'P' if isP(lm_list, pos) \
        else 'Q' if isQ(lm_list, pos) \
        else 'R' if isR(lm_list, pos) \
        else 'S' if isS(lm_list, pos) \
        else 'T' if isT(lm_list, pos) \
        else 'U' if isU(lm_list, pos) \
        else 'V' if isV(lm_list, pos) \
        else 'W' if isW(lm_list, pos) \
        else 'X' if isX(lm_list, pos) \
        else 'Y' if isY(lm_list, pos) \
        else 'Z' if isZ(lm_list, pos) \
        else ''


def initVals(lm_list):
    fx = tuple(lm_list[rightTipIds[i] - 2][1] - lm_list[rightTipIds[i]][1] for i in range(5))
    fy = tuple(lm_list[rightTipIds[i] - 2][2] - lm_list[rightTipIds[i]][2] for i in range(5))
    diff = abs(sum(fy)) - abs(sum(fx))
    orientation = 1 if diff > 0 else 0
    # orientation = Z if abs(diff) < 70 else Y if diff > 0 else X
    #print(orientation)
    return (fx, fy, orientation)

def isSpace(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    for id in range(1, 5):
        if pos[Y][id] < 0:
            return False
        if lm_list[rightTipIds[0]][1] < lm_list[rightTipIds[id]][1]:
            return False
    return True

def isA(lm_list, pos):
    # print("X: {} Y: {}".format(pos[0], pos[1]))
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    if lm_list[rightTipIds[0]][1] < lm_list[rightTipIds[1] - 1][1]:
        return False
    if lm_list[rightTipIds[0] - 2][2] < lm_list[rightTipIds[3]][2]:
        return False
    for id in range(1, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isB(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    for id in range(1, 5):
        if pos[Y][id] < 0:
            return False
    return True

def isC(lm_list, pos):
    if pos[Z] == Y:
        return False
    if pos[X][0] > 0:
        return False
    for id in range(1, 5):
        if pos[X][id] > 0:
            return False
    return True

def isD(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    if pos[Y][1] < 0:
        return False
    if lm_list[rightTipIds[0]][1] < lm_list[rightTipIds[2] - 2][1]:
            return False
    if lm_list[rightTipIds[0]][2] < lm_list[rightTipIds[2]][2]:
            return False
    for id in range(2, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 2][2]:
            return False
    return True

def isE(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    for id in range(1, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 2][2]:
            return False
        if lm_list[rightTipIds[0]][2] < lm_list[rightTipIds[id] - 1][2]:
            return False
    return True

def isF(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    if lm_list[rightTipIds[1]][2] < lm_list[rightTipIds[1] - 2][2]:
        return False
    for id in range(2, 5):
        if lm_list[rightTipIds[id]][2] > lm_list[rightTipIds[id] - 2][2]:
            return False
    return True

def isG(lm_list, pos):
    if pos[Z] == Y:
        return False
    if lm_list[rightTipIds[1]][1] > lm_list[rightTipIds[1] - 2][1]:
        return False
    for id in range(2, 5):
        if lm_list[rightTipIds[id]][1] < lm_list[rightTipIds[id] - 2][1]:
            return False
    return True

def isH(lm_list, pos):
    if pos[Z] == Y:
        return False
    if lm_list[rightTipIds[1]][1] > lm_list[rightTipIds[1] - 2][1]:
        return False
    if lm_list[rightTipIds[2]][1] > lm_list[rightTipIds[2] - 2][1]:
        return False
    for id in range(3, 5):
        if lm_list[rightTipIds[id]][1] < lm_list[rightTipIds[id] - 2][1]:
            return False
    return True

def isI(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    if lm_list[rightTipIds[0]][1] < lm_list[rightTipIds[1] - 1][1]:
        return False
    for id in range(1, 4):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    if lm_list[rightTipIds[4]][2] > lm_list[rightTipIds[4] - 3][2]:
            return False
    return True

def isJ(lm_list, pos):
    if pos[Z] == Y:
        return False
    if pos[X][0] < 0:
        return False
    if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[1] - 1][2]:
        return False
    for id in range(1, 4):
        if lm_list[rightTipIds[id]][1] < lm_list[rightTipIds[id] - 3][1]:
            return False
    if lm_list[rightTipIds[4]][1] > lm_list[rightTipIds[4] - 3][1]:
            return False
    return True

def isK(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    if lm_list[rightTipIds[0]][1] < lm_list[rightTipIds[1]][1]:
        return False
    if lm_list[rightTipIds[1]][1] < lm_list[rightTipIds[2]][1]:
        return False
    for id in range(0, 3):
        if lm_list[rightTipIds[id]][2] > lm_list[rightTipIds[id] - 2][2]:
            return False
    for id in range(3, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isL(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] > 0:
        return False
    for id in range(1, 2):
        if lm_list[rightTipIds[id]][2] > lm_list[rightTipIds[id] - 2][2]:
            return False
    for id in range(2, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isM(lm_list, pos):
    if pos[Z] == X:
        return False
    if lm_list[rightTipIds[1]][1] < lm_list[rightTipIds[2]][1]:
        return False
    if lm_list[rightTipIds[0]][1] > lm_list[rightTipIds[3]][1]:
        return False
    for id in range(1, 2):
        if lm_list[rightTipIds[0]][2] < lm_list[rightTipIds[id] - 2][2]:
            return False
    for id in range(1, 4):
        if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[id]][2]:
            return False
    if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[4] - 1][2]:
        return False
    return True

def isN(lm_list, pos): #NEEDS WORK -------------------------------------------------
    if pos[Z] == X:
        return False
    # if pos[Y][0] < 0:
    #     return False
    # if lm_list[rightTipIds[1]][1] < lm_list[rightTipIds[2]][1]:
    #     return False
    if lm_list[rightTipIds[0]][1] > lm_list[rightTipIds[2] - 2][1]:
        return False
    if lm_list[rightTipIds[0]][1] > lm_list[rightTipIds[2]][1]:
        return False
    for id in range(1, 3):
        if lm_list[rightTipIds[0]][2] < lm_list[rightTipIds[id] - 2][2]:
            return False
    for id in range(1, 3):
        if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[id]][2]:
            return False
    for id in range(3, 5):
        if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[id] - 1][2]:
            return False
    return True

def isO(lm_list, pos):
    if pos[Z] == Y:
        return False
    if pos[X][0] < 0:
        return False
    for id in range(1, 5):
        if pos[X][id] < 0:
            return False
    return True

def isP(lm_list, pos):
    if pos[Z] == Y:
        return False
    for id in range(0, 3):
        if lm_list[rightTipIds[id]][1] < lm_list[rightTipIds[id] - 2][1]:
            return False
    for id in range(3, 5):
        if lm_list[rightTipIds[id]][1] > lm_list[rightTipIds[id] - 3][1]:
            return False
    return True

def isQ(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] > 0:
        return False
    if pos[Y][1] > 0:
        return False
    # for id in range(0, 2):
    #     if lm_list[rightTipIds[id]][1] < lm_list[rightTipIds[id] - 2][1]:
    #         return False
    # for id in range(2, 5):
    #     if lm_list[rightTipIds[id]][1] > lm_list[rightTipIds[id] - 3][1]:
    #         return False
    return True

def isR(lm_list, pos):
    if pos[Z] == X:
        return False
    if lm_list[rightTipIds[1]][1] > lm_list[rightTipIds[2]][1]:
        return False
    for id in range(3, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    for id in range(1, 3):
        if lm_list[rightTipIds[id]][2] > lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isS(lm_list, pos):
    if pos[Z] == X:
        return False
    if lm_list[rightTipIds[0] - 2][2] > lm_list[rightTipIds[3]][2]:
        return False
    for id in range(1, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isT(lm_list, pos):
    if pos[Z] == X:
        return False
    if lm_list[rightTipIds[1]][1] < lm_list[rightTipIds[2]][1]:
        return False
    if lm_list[rightTipIds[0]][1] > lm_list[rightTipIds[1] - 2][1]:
        return False
    for id in range(1, 2):
        if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[id]][2]:
            return False
    if lm_list[rightTipIds[0]][1] < lm_list[rightTipIds[2] - 2][1]:
        return False
    if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[4] - 1][2]:
        return False
    return True

def isU(lm_list, pos):
    if pos[Z] == X:
        return False
    for id in range(1, 3):
        if lm_list[rightTipIds[id]][2] > lm_list[rightTipIds[id] - 3][2]:
            return False
    for id in range(3, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isV(lm_list, pos):
    if pos[Z] == X:
        return False
    for id in range(1, 3):
        if lm_list[rightTipIds[id]][2] > lm_list[rightTipIds[id] - 3][2]:
            return False
    for id in range(3, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 2][2]:
            return False
    return True

def isW(lm_list, pos):
    if pos[Z] == X:
        return False
    for id in range(1, 4):
        if lm_list[rightTipIds[id]][2] > lm_list[rightTipIds[id] - 3][2]:
            return False
    for id in range(4, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isX(lm_list, pos):
    if pos[Z] == X:
        return False
    # if pos[Y][1] < 0:
    #     return False
    if lm_list[rightTipIds[1]][2] < lm_list[rightTipIds[1] - 1][2]:
            return False
    for id in range(2, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isY(lm_list, pos):
    if lm_list[rightTipIds[0]][2] > lm_list[rightTipIds[0] - 3][2]:
        return False
    if lm_list[rightTipIds[4]][2] > lm_list[rightTipIds[4] - 3][2]:
        return False
    for id in range(1, 4):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    return True

def isZ(lm_list, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    if pos[Y][1] < 0:
        return False
    for id in range(2, 5):
        if lm_list[rightTipIds[id]][2] < lm_list[rightTipIds[id] - 3][2]:
            return False
    if lm_list[rightTipIds[0]][1] > lm_list[rightTipIds[2] - 2][1]:
            return False
    return True
