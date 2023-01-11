
#! IMPORTS

# We use face_recognition to do the actual face detection
import face_recognition as fr

# Cv2 is only used to get video footage from the webcam and to display the bounding box
import cv2

# numpy is only used to get the closest person out of the the database of faces (only from a certain certainty)
import numpy as num

# time is only used to delay
import time

# mss and PIL are used for rapid screen captures
from mss import mss
from PIL import Image

# Deepface is used for emotion detection
from deepface import DeepFace

# TESSERACT text detection
from PIL import Image
from pytesseract import pytesseract

# NLTK kind of text detection
#import nltk
#from sklearn.feature_extraction.text import TfidfVectorizer
#from sklearn.ensemble import GradientBoostingClassifier
#from sklearn.metrics import classification_report

# pyttsx3 text to speech
import pyttsx3

#! BRIEF EXPLANATION
# This script is a simple face recognition script. It uses the face_recognition library to detect faces and compare them to a database of faces.
# The database of faces is a folder with images of the people you want to recognize. The script will compare the faces in the database to the faces in the video footage.
# The script will then display the name of the person with the highest certainty.
# The script does this by using a bounding box around the face and displaying the name of the person in the bounding box.
# It allows for easy expansion of the database of faces. This is done by adding more images of the person to the database folder.
# This is very convenient for people who want to use this script for their own purposes, as it is low effort to expand the database of faces.

#! GLOBAL VARIABLES
StopFaceDetection = False

# If true use the method where you get the closest person out of the database of faces
# If false use the method were you get the first match out of the database of faces
NearestMode = True

# If true display a bounding box around the face and show video output
# If false don't display a bounding box around the face and show text output
VisualMode = False

# If true work from the camera webcam
# If false work from capturing parts of the screen
CameraMode = False

# If true find age
# If false skip age (faster)
SkipAge = True

# If True find text in image
# If False do not find text in image
FindText = True

# If True find questions in text
# If False do not find questions in text
FindQuestions = True

# If true do speech
# If false do not do speech
TextSpeech = True

#! Text to speech settings
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')

#! Google search settings
from googlesearch import search

####################################
# TODO: CHANGE THIS TO CUSTOM BEGIN#
####################################

# nltk.download('nps_chat')
#posts = nltk.corpus.nps_chat.xml_posts()


#posts_text = [post.text for post in posts]

# divide train and test in 80 20
#train_text = posts_text[:int(len(posts_text)*0.8)]
#test_text = posts_text[int(len(posts_text)*0.2):]

# Get TFIDF features
# vectorizer = TfidfVectorizer(ngram_range=(1, 3),
#                             min_df=0.001,
#                             max_df=0.7,
#                             analyzer='word')

#X_train = vectorizer.fit_transform(train_text)
#X_test = vectorizer.transform(test_text)

#y = [post.get('class') for post in posts]

#y_train = y[:int(len(posts_text)*0.8)]
#y_test = y[int(len(posts_text)*0.2):]

# Fitting Gradient Boosting classifier to the Training set
#gb = GradientBoostingClassifier(n_estimators=400, random_state=0)
# Can be improved with Cross Validation

#gb.fit(X_train, y_train)

#predictions_rf = gb.predict(X_test)

# Accuracy of 86% not bad
#print(classification_report(y_test, predictions_rf))

##################################
# TODO: CHANGE THIS TO CUSTOM END#
##################################

#! Find location
#TODO: this

#! LOAD FACE DATABASE
obama_image = fr.load_image_file("obama.jpg")
obama_face_encoding = fr.face_encodings(obama_image)[0]

joost_image = fr.load_image_file("joost_train.jpg")
joost_face_encoding = fr.face_encodings(joost_image)[0]

lars_image = fr.load_image_file("lars.jpg")
lars_face_encoding = fr.face_encodings(lars_image)[0]

michel_image = fr.load_image_file("michel.jpg")
michel_face_encoding = fr.face_encodings(michel_image)[0]

# We create an array of the face encodings
TrainedFaceEncodings = [
    obama_face_encoding,
    joost_face_encoding,
    lars_face_encoding,
    michel_face_encoding
]

# We create an array of the names of the people in the database
TrainedFaces = [
    "Barack Obama",
    "Joost Grunwald",
    "Lars van der A",
    "Michel van Wijk"
]

# Two list to store face locations and encodings into
FacesLocations = []
FacesEncodings = []

# Create variables to store the face names and wether to process a frame or not
NamesOfFaces = []
toProcess = True
lastname = ""

ScreenPart = {'left': 100, 'top': 100, 'width': 400, 'height': 400}

video_capture = ""
if CameraMode == True:
    # Get video capture from the webcam
    video_capture = cv2.VideoCapture(0)


#! INDEFINITE FACE RECOGNITION LOOP
while not StopFaceDetection:

    fourthFrameRGB = ""
    ret = ""
    singleFrame = ""
    if CameraMode == True:
        # Get single frame from the video capture
        ret, singleFrame = video_capture.read()
    else:
        with mss() as sct:
            Shot = sct.grab(ScreenPart)
            img = Image.frombytes('RGB', (Shot.width, Shot.height), Shot.rgb)
            cv2.imshow('test', num.array(img))
            fourthFrame = num.array(img)

    # Only process half of frames
    if toProcess:

        if FindText:

            # Get path to tesseract module
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

            # Set tesseract path correct in python module
            pytesseract.tesseract_cmd = path_to_tesseract

            # Convert singleFrame to pillow image
            img = Image.fromarray(fourthFrame, 'RGB')

            # Get text with pytesseract
            text = pytesseract.image_to_string(img)

            if FindQuestions:

                # Foreach line in text
                for line in text.splitlines():
                    # Find questions
                    if "?" in line:

                        # Cut off line after question mark
                        line = line[:line.index("?")+1]

                        # Print question
                        print(line)

            # TODO: parse text to find math equations
            # TODO: parse text to find basic questionsW

        if CameraMode:
            # We resize the frame to 1/4 of its original size to make the face detection faster
            fourthFrame = cv2.resize(singleFrame, (0, 0), fx=0.25, fy=0.25)

        # Get a grayscale version
        fourthFrameGrey = cv2.cvtColor(fourthFrame, cv2.COLOR_BGR2GRAY)

        # We have to convert the image from BGR to RGB color format
        fourthFrameRGB = fourthFrame[:, :, ::-1]

        # Process the current frame for faces and face encodings
        FacesLocations = fr.face_locations(fourthFrameRGB)
        FacesEncodings = fr.face_encodings(fourthFrameRGB, FacesLocations)

        NamesOfFaces = []
        for face_encoding in FacesEncodings:
            # Check if the face matches a face in our database
            matches = fr.compare_faces(TrainedFaceEncodings, face_encoding)
            name = "Face not found"

            if NearestMode:
                # From the (possible) matches, get the face nearest to the face we are looking at
                FaceDistance = fr.face_distance(
                    TrainedFaceEncodings, face_encoding)
                MatchInList = num.argmin(FaceDistance)

                # If there is a proper match, save the name
                if matches[MatchInList]:
                    name = TrainedFaces[MatchInList]
            elif True in matches:
                # Get the first match in our face encoding database
                first_match_index = matches.index(True)
                # Get the name corresponding to this first match
                name = TrainedFaces[first_match_index]

            NamesOfFaces.append(name)

    # Flip processing to skip half of frames
    toProcess = not toProcess

    if VisualMode:
        # Display the results
        for (t, r, b, l), FoundName in zip(FacesLocations, NamesOfFaces):

            # Multiply dimensions by 4 because the frame was resized to 1/4 size
            t = t * 4
            r = r * 4
            b = b * 4
            l = l * 4

            # We create a bounding box and draw it
            cv2.rectangle(singleFrame, (l, t), (r, b), (0, 0, 255), 2)

            # We create a place to put the name
            cv2.rectangle(singleFrame, (l, b - 35),
                          (r, b), (0, 0, 255), cv2.FILLED)

            # We put the name in the place
            myFont = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(singleFrame, FoundName, (l + 6, b - 6),
                        myFont, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', singleFrame)

    else:
        name = "unknown"
        for (t, r, b, l), FoundName in zip(FacesLocations, NamesOfFaces):

            # If name not unknown
            if FoundName != "unknown" and lastname != FoundName:
                # Set name to the found name
                name = FoundName
                print("Name: " + name)

                # If texttospeech, say name
                if TextSpeech:
                    engine.say(name)
                    engine.runAndWait()

                # Set lastname to name
                lastname = name
            elif lastname == FoundName:
                lastname = "unknown"

            if not SkipAge:
                #cv2.imwrite('C:/Users/Joost/Documents/currentImage.jpg', fourthFrame)
                face_analysis = DeepFace.analyze(img_path=fourthFrame, actions=[
                                                 'age', 'emotion'], enforce_detection=False)
            else:
                face_analysis = DeepFace.analyze(img_path=fourthFrame, actions=[
                                                 'emotion'], enforce_detection=False)
            # Get the dominant_emotion from json object
            dominant_emotion = face_analysis['dominant_emotion']

            if not SkipAge:
                # Get the age from json object
                age = face_analysis['age']

                print("Age: " + str(age) +
                      " Dominant emotion: " + dominant_emotion)
            else:
                print(" Dominant emotion: " + dominant_emotion)

            # Sleep to not be too speedy
            time.sleep(1)

    # Catch q and break if pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        StopFaceDetection = True
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
