import cv2 as cv

leftTipIds = [25, 29, 33, 37, 41]
rightTipIds = [4, 8, 12, 16, 20]

def fingerCount(img, detector, onLockIn, clearText):
    lmList = detector.findPosition(img, draw=False)
    # if len(lmList) > 0:
    #     print("4: {}".format(lmList[4]))
    #     if len(lmList) > 21:
    #         print("39: {}".format(lmList[39]))

    # if len(lmList) != 0:
    if len(lmList) > 21:
        # rightFingers = []
        # # Thumb
        # if lmList[rightTipIds[0]][1] > lmList[rightTipIds[0] - 1][1]:
        #     rightFingers.append(1)
        # else:
        #     rightFingers.append(0)
        # # 4 Fingers
        # for id in range(1, 5):
        #     if lmList[rightTipIds[id]][2] < lmList[rightTipIds[id] - 2][2]:
        #         rightFingers.append(1)
        #     else:
        #         rightFingers.append(0)
        # totalRightFingers = rightFingers.count(1)
        # # print("Total: {} Fingers: {}".format(totalFingers, rightFingers))
        # cv.putText(img, str(totalRightFingers), (45, 145), cv.FONT_HERSHEY_PLAIN,
        #             10, (255, 0, 0), 25)
        
        leftFingers = []
        # Thumb
        if lmList[leftTipIds[0]][1] < lmList[leftTipIds[0] - 1][1]:
            leftFingers.append(1)
        else:
            leftFingers.append(0)
        # 4 Fingers
        for id in range(1, 5):
            if lmList[leftTipIds[id]][2] < lmList[leftTipIds[id] - 2][2]:
                leftFingers.append(1)
            else:
                leftFingers.append(0)
        totalLeftFingers = leftFingers.count(1)

        if totalLeftFingers == 0 and not detector.leftLocked:
            # do lock logic here
            onLockIn(lmList)
            # print("Total: {} Fingers: {}".format(totalRightFingers, rightFingers))
            detector.leftLocked = True
        elif totalLeftFingers > 0:
            detector.leftLocked = False

        # print("Total: {} Fingers: {}".format(totalFingers, leftFingers))
        cv.putText(img, str(totalLeftFingers), (597, 47), cv.FONT_HERSHEY_PLAIN,
                    2, (0, 0, 0), 2)
        cv.putText(img, str(totalLeftFingers), (595, 45), cv.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 255), 2)
    
    elif len(lmList) != 0:
        leftFingers = []
        # Thumb
        if lmList[leftTipIds[0]-21][1] < lmList[leftTipIds[0] - 1-21][1]: # subtract by 21 due to single hand index shift in lmList
            leftFingers.append(1)
        else:
            leftFingers.append(0)
        # 4 Fingers
        for id in range(1, 5):
            if lmList[leftTipIds[id]-21][2] < lmList[leftTipIds[id] - 2-21][2]: # subtract by 21 due to single hand index shift in lmList
                leftFingers.append(1)
            else:
                leftFingers.append(0)
        totalLeftFingers = leftFingers.count(1)

        if totalLeftFingers == 0 and not detector.leftLocked:
            # do lock logic here
            clearText()
            # print("Total: {} Fingers: {}".format(totalRightFingers, rightFingers))
            detector.leftLocked = True
        elif totalLeftFingers > 0:
            detector.leftLocked = False

        # print("Total: {} Fingers: {}".format(totalFingers, leftFingers))
        cv.putText(img, str(totalLeftFingers), (597, 47), cv.FONT_HERSHEY_PLAIN,
                    2, (0, 0, 0), 2)
        cv.putText(img, str(totalLeftFingers), (595, 45), cv.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 255), 2)

    return lmList





# import cv2 as cv

# tipIds = [4, 8, 12, 16, 20]

# def fingerCount(img, detector):
#     lmList = detector.findPosition(img, draw=False)

#     if len(lmList) != 0:
#         fingers = []
#         # Thumb
#         if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
#             fingers.append(1)
#         else:
#             fingers.append(0)
#         # 4 Fingers
#         for id in range(1, 5):
#             if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
#                 fingers.append(1)
#             else:
#                 fingers.append(0)
#         totalFingers = fingers.count(1)
#         print("Total: {} Fingers: {}".format(totalFingers, fingers))
#         cv.putText(img, str(totalFingers), (45, 145), cv.FONT_HERSHEY_PLAIN,
#                     10, (255, 0, 0), 25)
