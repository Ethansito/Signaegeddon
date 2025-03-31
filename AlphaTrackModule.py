import cv2 as cv

X, Y, Z = 0, 1, 2

# class Finger:
#     THUMB, INDEX, MIDDLE, RING, PINKY = list(range(5))

rightTipIds = [4, 8, 12, 16, 20]

def readAlpha(lmList):
    pos = initVals(lmList)
    return '_' if isSpace(lmList, pos) \
        else 'A' if isA(lmList, pos) \
        else 'B' if isB(lmList, pos) \
        else 'C' if isC(lmList, pos) \
        else 'D' if isD(lmList, pos) \
        else 'E' if isE(lmList, pos) \
        else 'F' if isF(lmList, pos) \
        else 'G' if isG(lmList, pos) \
        else 'H' if isH(lmList, pos) \
        else 'I' if isI(lmList, pos) \
        else 'J' if isJ(lmList, pos) \
        else 'K' if isK(lmList, pos) \
        else 'L' if isL(lmList, pos) \
        else 'M' if isM(lmList, pos) \
        else 'N' if isN(lmList, pos) \
        else 'O' if isO(lmList, pos) \
        else 'P' if isP(lmList, pos) \
        else 'Q' if isQ(lmList, pos) \
        else 'R' if isR(lmList, pos) \
        else 'S' if isS(lmList, pos) \
        else 'T' if isT(lmList, pos) \
        else 'U' if isU(lmList, pos) \
        else 'V' if isV(lmList, pos) \
        else 'W' if isW(lmList, pos) \
        else 'X' if isX(lmList, pos) \
        else 'Y' if isY(lmList, pos) \
        else 'Z' if isZ(lmList, pos) \
        else ''

# def isA(lmList, pos):
#     # print([x[0] for x in lmList])
#     # Thumb
#     if lmList[rightTipIds[0]][2] > lmList[rightTipIds[0] - 1][2]:
#         # print('thumb')
#         return False
#     if lmList[rightTipIds[0]][1] < lmList[rightTipIds[1] - 1][1]:
#         return False
#     # 4 Fingers
#     for id in range(1, 5):
#         if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
#             # print(id)
#             return False
#     return True

# def isB(lmList, pos):
#     if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
#         return False
#     for id in range(1, 5):
#         if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 2][2]:
#             return False
#     return True

# def isC(lmList, pos):
#     if lmList[rightTipIds[0]][1] < lmList[rightTipIds[0] - 1][1]:
#         return False
#     for id in range(1, 5):
#         if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
#             return False
#     return True

# def isD(lmList, pos):
#     if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
#         return False
#     if lmList[rightTipIds[1]][2] > lmList[rightTipIds[1] - 2][2]:
#         return False
#     for id in range(2, 5):
#         if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 2][2]:
#             return False
#     return True

# def isE(lmList, pos):
#     if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
#         return False
#     if lmList[rightTipIds[0]][2] < lmList[rightTipIds[1] - 1][2]:
#         return False
#     for id in range(1, 5):
#         if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 2][2]:
#             return False
#     return True

# def isF(lmList, pos):
#     if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
#         return False
#     if lmList[rightTipIds[1]][2] < lmList[rightTipIds[1] - 2][2]:
#         return False
#     for id in range(2, 5):
#         if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 2][2]:
#             return False
#     return True

# def isG(lmList, pos):
#     if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
#         return False
#     if lmList[rightTipIds[1]][1] > lmList[rightTipIds[1] - 2][1]:
#         return False
#     for id in range(2, 5):
#         if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
#             return False
#     return True

# def isH(lmList, pos):
#     if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
#         return False
#     if lmList[rightTipIds[1]][1] > lmList[rightTipIds[1] - 2][1]:
#         return False
#     if lmList[rightTipIds[2]][1] > lmList[rightTipIds[2] - 2][1]:
#         return False
#     for id in range(3, 5):
#         if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
#             return False
#     return True

# def isI(lmList, pos):
#     if lmList[rightTipIds[0]][2] > lmList[rightTipIds[0] - 1][2]:
#         return False
#     for id in range(1, 4):
#         if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
#             return False
#     if lmList[rightTipIds[4]][2] > lmList[rightTipIds[4] - 1][2]:
#         return False
#     return True

# def isJ(lmList, pos): #GET BACK TO (Issue similar with I)-------------------------------------------------------------
#     if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
#         return False
#     for id in range(1, 4):
#         if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
#             return False
#     if lmList[rightTipIds[4]][1] > lmList[rightTipIds[4] - 2][1]:
#         return False
#     return True

# def isK(lmList, pos):
#     if lmList[rightTipIds[0]][2] > lmList[rightTipIds[0] - 1][2]:
#         return False
#     if lmList[rightTipIds[1]][2] > lmList[rightTipIds[1] - 1][2]:
#         return False
#     if lmList[rightTipIds[2]][2] > lmList[rightTipIds[2] - 1][2]:
#         return False
#     for id in range(3, 5):
#         if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
#             return False
#     return True

# def isL(lmList, pos):
#     if lmList[rightTipIds[0]][1] < lmList[rightTipIds[0] - 1][1]:
#         return False
#     if lmList[rightTipIds[1]][2] > lmList[rightTipIds[1] - 1][2]:
#         return False
#     for id in range(2, 5):
#         if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
#             return False
#     return True

# def isM(lmList, pos):
#     if lmList[rightTipIds[0]][2] > lmList[rightTipIds[4] - 1][2]:
#         return False
#     for id in range(1, 5):
#         if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 2][2]:
#             return False
#         if lmList[rightTipIds[0]][2] < lmList[rightTipIds[id] - 2][2]:
#             return False
#     if lmList[rightTipIds[4]][2] > lmList[rightTipIds[4] - 2][2]:
#         return False
#     return True

def initVals(lmList):
    fx = tuple(lmList[rightTipIds[i]-2][1] - lmList[rightTipIds[i]][1] for i in range(5))
    fy = tuple(lmList[rightTipIds[i]-2][2] - lmList[rightTipIds[i]][2] for i in range(5))
    diff = abs(sum(fy)) - abs(sum(fx))
    orientation = 1 if diff > 0 else 0
    # orientation = Z if abs(diff) < 70 else Y if diff > 0 else X
    #print(orientation)
    return (fx, fy, orientation)

def isSpace(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    for id in range(1, 5):
        if pos[Y][id] < 0:
            return False
        if lmList[rightTipIds[0]][1] < lmList[rightTipIds[id]][1]:
            return False
    return True

def isA(lmList, pos):
    # print("X: {} Y: {}".format(pos[0], pos[1]))
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    if lmList[rightTipIds[0]][1] < lmList[rightTipIds[1] - 1][1]:
        return False
    if lmList[rightTipIds[0]-2][2] < lmList[rightTipIds[3]][2]:
        return False
    for id in range(1, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isB(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    for id in range(1, 5):
        if pos[Y][id] < 0:
            return False
    return True

def isC(lmList, pos):
    if pos[Z] == Y:
        return False
    if pos[X][0] > 0:
        return False
    for id in range(1, 5):
        if pos[X][id] > 0:
            return False
    return True

def isD(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    if pos[Y][1] < 0:
        return False
    if lmList[rightTipIds[0]][1] < lmList[rightTipIds[2] - 2][1]:
            return False
    if lmList[rightTipIds[0]][2] < lmList[rightTipIds[2]][2]:
            return False
    for id in range(2, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 2][2]:
            return False
    return True

def isE(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    for id in range(1, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 2][2]:
            return False
        if lmList[rightTipIds[0]][2] < lmList[rightTipIds[id] - 1][2]:
            return False
    return True

def isF(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    if lmList[rightTipIds[1]][2] < lmList[rightTipIds[1] - 2][2]:
        return False
    for id in range(2, 5):
        if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 2][2]:
            return False
    return True

def isG(lmList, pos):
    if pos[Z] == Y:
        return False
    if lmList[rightTipIds[1]][1] > lmList[rightTipIds[1] - 2][1]:
        return False
    for id in range(2, 5):
        if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
            return False
    return True

def isH(lmList, pos):
    if pos[Z] == Y:
        return False
    if lmList[rightTipIds[1]][1] > lmList[rightTipIds[1] - 2][1]:
        return False
    if lmList[rightTipIds[2]][1] > lmList[rightTipIds[2] - 2][1]:
        return False
    for id in range(3, 5):
        if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
            return False
    return True

def isI(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    if lmList[rightTipIds[0]][1] < lmList[rightTipIds[1] - 1][1]:
        return False
    for id in range(1, 4):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    if lmList[rightTipIds[4]][2] > lmList[rightTipIds[4] - 3][2]:
            return False
    return True

def isJ(lmList, pos):
    if pos[Z] == Y:
        return False
    if pos[X][0] < 0:
        return False
    if lmList[rightTipIds[0]][2] > lmList[rightTipIds[1] - 1][2]:
        return False
    for id in range(1, 4):
        if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 3][1]:
            return False
    if lmList[rightTipIds[4]][1] > lmList[rightTipIds[4] - 3][1]:
            return False
    return True

def isK(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] < 0:
        return False
    if lmList[rightTipIds[0]][1] < lmList[rightTipIds[1]][1]:
        return False
    if lmList[rightTipIds[1]][1] < lmList[rightTipIds[2]][1]:
        return False
    for id in range(0, 3):
        if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 2][2]:
            return False
    for id in range(3, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isL(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] > 0:
        return False
    for id in range(1, 2):
        if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 2][2]:
            return False
    for id in range(2, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isM(lmList, pos):
    if pos[Z] == X:
        return False
    if lmList[rightTipIds[1]][1] < lmList[rightTipIds[2]][1]:
        return False
    if lmList[rightTipIds[0]][1] > lmList[rightTipIds[3]][1]:
        return False
    for id in range(1, 2):
        if lmList[rightTipIds[0]][2] < lmList[rightTipIds[id] - 2][2]:
            return False
    for id in range(1, 4):
        if lmList[rightTipIds[0]][2] > lmList[rightTipIds[id]][2]:
            return False
    if lmList[rightTipIds[0]][2] > lmList[rightTipIds[4] - 1][2]:
        return False
    return True

def isN(lmList, pos): #NEEDS WORK -------------------------------------------------
    if pos[Z] == X:
        return False
    # if pos[Y][0] < 0:
    #     return False
    # if lmList[rightTipIds[1]][1] < lmList[rightTipIds[2]][1]:
    #     return False
    if lmList[rightTipIds[0]][1] > lmList[rightTipIds[2] - 2][1]:
        return False
    if lmList[rightTipIds[0]][1] > lmList[rightTipIds[2]][1]:
        return False
    for id in range(1, 3):
        if lmList[rightTipIds[0]][2] < lmList[rightTipIds[id] - 2][2]:
            return False
    for id in range(1, 3):
        if lmList[rightTipIds[0]][2] > lmList[rightTipIds[id]][2]:
            return False
    for id in range(3, 5):
        if lmList[rightTipIds[0]][2] > lmList[rightTipIds[id] - 1][2]:
            return False
    return True

def isO(lmList, pos):
    if pos[Z] == Y:
        return False
    if pos[X][0] < 0:
        return False
    for id in range(1, 5):
        if pos[X][id] < 0:
            return False
    return True

def isP(lmList, pos):
    if pos[Z] == Y:
        return False
    for id in range(0, 3):
        if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
            return False
    for id in range(3, 5):
        if lmList[rightTipIds[id]][1] > lmList[rightTipIds[id] - 3][1]:
            return False
    return True

def isQ(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[Y][0] > 0:
        return False
    if pos[Y][1] > 0:
        return False
    # for id in range(0, 2):
    #     if lmList[rightTipIds[id]][1] < lmList[rightTipIds[id] - 2][1]:
    #         return False
    # for id in range(2, 5):
    #     if lmList[rightTipIds[id]][1] > lmList[rightTipIds[id] - 3][1]:
    #         return False
    return True

def isR(lmList, pos):
    if pos[Z] == X:
        return False
    if lmList[rightTipIds[1]][1] > lmList[rightTipIds[2]][1]:
        return False
    for id in range(3, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    for id in range(1, 3):
        if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isS(lmList, pos):
    if pos[Z] == X:
        return False
    if lmList[rightTipIds[0] - 2][2] > lmList[rightTipIds[3]][2]:
        return False
    for id in range(1, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isT(lmList, pos):
    if pos[Z] == X:
        return False
    if lmList[rightTipIds[1]][1] < lmList[rightTipIds[2]][1]:
        return False
    if lmList[rightTipIds[0]][1] > lmList[rightTipIds[1] - 2][1]:
        return False
    for id in range(1, 2):
        if lmList[rightTipIds[0]][2] > lmList[rightTipIds[id]][2]:
            return False
    if lmList[rightTipIds[0]][1] < lmList[rightTipIds[2] - 2][1]:
        return False
    if lmList[rightTipIds[0]][2] > lmList[rightTipIds[4] - 1][2]:
        return False
    return True

def isU(lmList, pos):
    if pos[Z] == X:
        return False
    for id in range(1, 3):
        if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 3][2]:
            return False
    for id in range(3, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isV(lmList, pos):
    if pos[Z] == X:
        return False
    for id in range(1, 3):
        if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 3][2]:
            return False
    for id in range(3, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 2][2]:
            return False
    return True

def isW(lmList, pos):
    if pos[Z] == X:
        return False
    for id in range(1, 4):
        if lmList[rightTipIds[id]][2] > lmList[rightTipIds[id] - 3][2]:
            return False
    for id in range(4, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isX(lmList, pos):
    if pos[Z] == X:
        return False
    # if pos[Y][1] < 0:
    #     return False
    if lmList[rightTipIds[1]][2] < lmList[rightTipIds[1] - 1][2]:
            return False
    for id in range(2, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isY(lmList, pos):
    if lmList[rightTipIds[0]][2] > lmList[rightTipIds[0] - 3][2]:
        return False
    if lmList[rightTipIds[4]][2] > lmList[rightTipIds[4] - 3][2]:
        return False
    for id in range(1, 4):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    return True

def isZ(lmList, pos):
    if pos[Z] == X:
        return False
    if pos[X][0] < 0:
        return False
    if pos[Y][1] < 0:
        return False
    for id in range(2, 5):
        if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 3][2]:
            return False
    if lmList[rightTipIds[0]][1] > lmList[rightTipIds[2] - 2][1]:
            return False
    return True
