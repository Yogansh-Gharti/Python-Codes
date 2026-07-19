import cv2
import face_recognition
import os
import csv
from datetime import datetime

known_face_encodings = []
known_face_names = []

# Load known faces
for file in os.listdir("known_faces"):

    if file.endswith(".jpg") or file.endswith(".png"):

        image = face_recognition.load_image_file(
            os.path.join("known_faces", file)
        )

        encoding = face_recognition.face_encodings(image)

        if encoding:
            known_face_encodings.append(encoding[0])
            known_face_names.append(
                os.path.splitext(file)[0]
            )

marked_today = set()

today = datetime.now().strftime("%d-%m-%Y")

if os.path.exists("attendance.csv"):

    with open("attendance.csv", "r") as file:

        reader = csv.reader(file)

        next(reader, None)

        for row in reader:

            if len(row) == 3 and row[1] == today:
                marked_today.add(row[0])

camera = cv2.VideoCapture(0)

print("Press Q to Exit")

while True:

    success, frame = camera.read()

    if not success:
        break

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    locations = face_recognition.face_locations(rgb)

    encodings = face_recognition.face_encodings(
        rgb,
        locations
    )

    for face_encoding, location in zip(
        encodings,
        locations
    ):

        matches = face_recognition.compare_faces(
            known_face_encodings,
            face_encoding
        )

        name = "Unknown"

        if True in matches:

            index = matches.index(True)

            name = known_face_names[index]

            if name not in marked_today:

                now = datetime.now()

                with open(
                    "attendance.csv",
                    "a",
                    newline=""
                ) as file:

                    writer = csv.writer(file)

                    if file.tell() == 0:
                        writer.writerow(
                            ["Name", "Date", "Time"]
                        )

                    writer.writerow([
                        name,
                        today,
                        now.strftime("%H:%M:%S")
                    ])

                marked_today.add(name)

                print(f"{name} Marked Present")

        top, right, bottom, left = location

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0,255,0),
            2
        )

        cv2.putText(
            frame,
            name,
            (left, top-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow(
        "Face Recognition Attendance",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
