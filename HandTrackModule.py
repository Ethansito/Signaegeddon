import cv2 as cv
import mediapipe as mp


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon = 0.5, trackCon = 0.5):

        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.leftLocked = True

        self.mpHands = mp.solutions.hands
        #Temporarily removed parameters to work code
        self.hands = self.mpHands.Hands(self.mode, self.maxHands)#, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.custom_hand_connections_style = self.mpDraw.DrawingSpec(
            color=(0, 255, 0),  # Green color (BGR format)
            thickness=2, 
            circle_radius=2
        )

        self.custom_hand_landmarks_style = self.mpDraw.DrawingSpec(
            color=(255, 0, 0),  # Blue color
            thickness=2, 
            circle_radius=2
        )

    def findHands(self, img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        #self.results = self.hands.process(imgRGB)
            #print(results.multi_hand_landmarks)

        self.results = self.hands.process(cv.cvtColor(img, cv.COLOR_BGR2RGB))
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    #self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS,
                                               self.custom_hand_landmarks_style,
                                               self.custom_hand_connections_style)
        return img
    
    def findPosition(self, img, handNo=0, draw=True):

        lmList = []
        if self.results.multi_hand_landmarks:
            hand1, hand2 = 0, 1
            primaryHand = self.results.multi_hand_landmarks[hand1]
            secondaryHand = None

            primary_handedness = self.results.multi_handedness[hand1]
            primary_left = primary_handedness.classification[0].label == 'Right'
            # print(primary_left)

            # primary_hand_color = (255,0,255) if primary_left else (255,0,0)
            # secondary_hand_color = (255,0,0) if primary_left else (255,0,255)
            primary_id_offset = 21 if primary_left else 0
            secondary_id_offset = 0 if primary_left else 21

            for id, lm in enumerate(primaryHand.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                #print(id, cx, cy)
                lmList.append([id + primary_id_offset, cx, cy])
                # if draw:
                #    cv.circle(img, (cx,cy), 5, primary_hand_color, cv.FILLED)
                #    cv.circle(img, (cx,cy), 5, (255,0,255), cv.FILLED)
                #Changes the color and adds circle shape to the node
                #if id == 0:
            
            if len(self.results.multi_hand_landmarks) > 1:
                secondaryHand = self.results.multi_hand_landmarks[hand2]
                
                for id, lm in enumerate(secondaryHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    lmList.append([id + secondary_id_offset, cx, cy])
                    # if draw:
                    #     cv.circle(img, (cx,cy), 5, secondary_hand_color, cv.FILLED)

        return sorted(lmList, key=lambda index: index[0])
        # return lmList
