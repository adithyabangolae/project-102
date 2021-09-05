import cv2

def take_snapshot():
    videoCaptureObj= cv2.VideoCapture(0)
    result = True

    while (result):
        ret,frame = videoCaptureObj.read()
        cv2.imwrite("newPic.jpg",frame)
        result = False

        videoCaptureObj.release()
        cv2.destroyAllWindows()

take_snapshot()