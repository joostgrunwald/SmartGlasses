
#! IMPORTS

# We use face_recognition to do the actual face detection
import face_recognition as fr

# Cv2 is only used to get video footage from the webcam and to display the bounding box
import cv2

# numpy is only used to get the closest person out of the the database of faces (only from a certain certainty)
import numpy as num

#! BRIEF EXPLANATION
# This script is a simple face recognition script. It uses the face_recognition library to detect faces and compare them to a database of faces.
# The database of faces is a folder with images of the people you want to recognize. The script will compare the faces in the database to the faces in the video footage.
# The script will then display the name of the person with the highest certainty.
# TODO: The script will also display the certainty of the person with the highest certainty.
# The script does this by using a bounding box around the face and displaying the name of the person in the bounding box.
# It allows for easy expansion of the database of faces. This is done by adding more images of the person to the database folder.
# This is very convenient for people who want to use this script for their own purposes, as it is low effort to expand the database of faces.

#! GLOBAL VARIABLES
StopFaceDetection = False

# If true use the method where you get the closest person out of the database of faces
# If false use the method were you get the first match out of the database of faces
NearestMode = True

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

#! LOAD FACE DATABASE
obama_image = fr.load_image_file("obama.jpg")
obama_face_encoding = fr.face_encodings(obama_image)[0]

joost_image = fr.load_image_file("joost_train.jpg")
joost_face_encoding = fr.face_encodings(joost_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    joost_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joost Grunwald"
]

# Initialize some variables
FacesLocations = []
FacesEncodings = []
face_names = []
process_this_frame = True

#! INDEFINITE FACE RECOGNITION LOOP

while not StopFaceDetection:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        FacesLocations = fr.face_locations(rgb_small_frame)
        FacesEncodings = fr.face_encodings(rgb_small_frame, FacesLocations)

        face_names = []
        for face_encoding in FacesEncodings:
            # See if the face is a match for the known face(s)
            matches = fr.compare_faces(known_face_encodings, face_encoding)
            name = "Face not found"

            if NearestMode:
                # Or instead, use the known face with the smallest distance to the new face
                FaceDistance = fr.face_distance(
                    known_face_encodings, face_encoding)
                MatchInList = num.argmin(FaceDistance)
                if matches[MatchInList]:
                    name = known_face_names[MatchInList]
            elif True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(FacesLocations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6),
                    font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
