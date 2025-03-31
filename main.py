import cv2 as cv
import HandTrackModule as htm
import FingerCounterModule as fcm
import AlphaTrackModule as atm


if __name__ == "__main__":
    text, chr = "", ""
    cap = cv.VideoCapture(0, cv.CAP_DSHOW)
    detector = htm.handDetector()

    def onLockIn(lmList):
        global text
        # text += "A"
        text = text.replace('_', ' ', 1)
        # textLen = len(text)
        # if textLen >0 and text[textLen-1] == '_':
        #     text[textLen-1] = ' '
        text += atm.readAlpha(lmList)

    def clearText():
        global text
        text = ""

    while True:
        success, img = cap.read()
        img = detector.findHands(img)

        lmList = fcm.fingerCount(img, detector, onLockIn, clearText)

        chr = "" if len(lmList) == 0 else atm.readAlpha(lmList)
        # if chr == ' ':
        #     chr = '_'

        if success:
            cv.putText(img, text, (28, 468), cv.FONT_HERSHEY_PLAIN,
                    4, (0, 0, 0), 4)
            cv.putText(img, text, (25, 465), cv.FONT_HERSHEY_PLAIN,
                    4, (255, 0, 255), 4)
            cv.putText(img, chr, (28, 68), cv.FONT_HERSHEY_PLAIN,
                    4, (0, 0, 0), 4)
            cv.putText(img, chr, (25, 65), cv.FONT_HERSHEY_PLAIN,
                    4, (0, 255, 255), 4)
            cv.imshow('Image', img)

        if cv.waitKey(20) &  0xFF==ord('d'):
            break

    cap.release()
    cv.destroyAllWindows()
