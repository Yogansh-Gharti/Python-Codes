import cv2
import os

# Load Haar Cascade
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open webcam.")
    exit()

os.makedirs("detected_faces", exist_ok=True)

image_count = 1

print("Press 'S' to save detected faces.")
print("Press 'Q' to quit.")

while True:

    success, frame = camera.read()

    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Faces: {len(faces)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow("Face Detection", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):

        for (x, y, w, h) in faces:

            face = frame[y:y+h, x:x+w]

            filename = f"detected_faces/face_{image_count}.jpg"

            cv2.imwrite(filename, face)

            print(f"Saved: {filename}")

            image_count += 1

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
