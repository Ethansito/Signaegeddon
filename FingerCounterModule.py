import cv2 as cv

leftTipIds = [25, 29, 33, 37, 41]
rightTipIds = [4, 8, 12, 16, 20]

def finger_count(img, detector, on_lock_in, clear_text):
    lm_list = detector.findPosition(img, draw=False)

    # if len(lmList) != 0:
    if len(lm_list) > 21:
        
        left_fingers = []
        # Thumb
        if lm_list[leftTipIds[0]][1] < lm_list[leftTipIds[0] - 1][1]:
            left_fingers.append(1)
        else:
            left_fingers.append(0)
        # 4 Fingers
        for ident in range(1, 5):
            if lm_list[leftTipIds[ident]][2] < lm_list[leftTipIds[ident] - 2][2]:
                left_fingers.append(1)
            else:
                left_fingers.append(0)
        total_left_fingers = left_fingers.count(1)

        if total_left_fingers == 0 and not detector.leftLocked:
            # do lock logic here
            on_lock_in(lm_list)
            # print("Total: {} Fingers: {}".format(totalRightFingers, rightFingers))
            detector.leftLocked = True
        elif total_left_fingers > 0:
            detector.leftLocked = False

        # print("Total: {} Fingers: {}".format(totalFingers, leftFingers))
        cv.putText(img, str(total_left_fingers), (597, 47), cv.FONT_HERSHEY_PLAIN,
                    2, (0, 0, 0), 2)
        cv.putText(img, str(total_left_fingers), (595, 45), cv.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 255), 2)
    
    elif len(lm_list) != 0:
        left_fingers = []
        # Thumb
        if lm_list[leftTipIds[0]-21][1] < lm_list[leftTipIds[0] - 1-21][1]: # subtract by 21 due to single hand index shift in lmList
            left_fingers.append(1)
        else:
            left_fingers.append(0)
        # 4 Fingers
        for ident in range(1, 5):
            if lm_list[leftTipIds[ident]-21][2] < lm_list[leftTipIds[ident] - 2-21][2]: # subtract by 21 due to single hand index shift in lmList
                left_fingers.append(1)
            else:
                left_fingers.append(0)
        total_left_fingers = left_fingers.count(1)

        if total_left_fingers == 0 and not detector.leftLocked:
            # do lock logic here
            clear_text()
            # print("Total: {} Fingers: {}".format(totalRightFingers, rightFingers))
            detector.leftLocked = True
        elif total_left_fingers > 0:
            detector.leftLocked = False

        # print("Total: {} Fingers: {}".format(totalFingers, leftFingers))
        cv.putText(img, str(total_left_fingers), (597, 47), cv.FONT_HERSHEY_PLAIN,
                    2, (0, 0, 0), 2)
        cv.putText(img, str(total_left_fingers), (595, 45), cv.FONT_HERSHEY_PLAIN,
                    2, (255, 0, 255), 2)

    return lm_list
