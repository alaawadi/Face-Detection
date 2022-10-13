from FaceDetector import FaceDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:
    success, img = cap.read()
    img, faces = detector.findFaces(img)
    if faces:
        print(faces[0])
    # if bboxs:
    #     center = bboxs[0]["center"]
    #     cv2.circle(img, center, 5, (82, 167, 54), cv2.FILLED)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()