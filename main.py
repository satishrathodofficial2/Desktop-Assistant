from src.helper import wish_me,takeCommand,speak
import wikipedia
import datetime
import webbrowser
import cv2

if __name__ == "__main__":

    wish_me()
    while True:
        query = takeCommand()
        query = query.lower()

        if "wikipedia" in query:
            speak("Searching in wikipedia")
            query = query.replace('according to wikipedia', "")
            query = query.replace('as per wikipedia', "")
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" == query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif "youtube" in query:
            speak("searching on youtube")
            query = query.replace("youtube", "")
            url = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(url)

        elif "open google" == query:
            speak("Opening google")
            url = "https://www.google.com"
            webbrowser.open(url)

        # program to capture single image from webcam in python 
        elif "take selfie" == query:
            speak("smile please")
            # Create a VideoCapture object
            cap = cv2.VideoCapture(0)

            # Check if the camera is opened successfully
            if not cap.isOpened():
                print("Unable to open camera")
                exit()

            # Capture a frame
            ret, frame = cap.read()

            # Check if the frame is not empty
            if not ret:
                print("No frame received")
                exit()

            # Display the frame
            cv2.imshow('Frame', frame)

            # Wait for a key press
            cv2.waitKey(0)

            # Release the camera
            cap.release()

            # Close all windows
            cv2.destroyAllWindows()

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir time is {strtime}")
        
        elif "kiran" in query:
            speak("Kiran is a famous trader in hyderabad, who is born in karnataka, he has 3 brothers who call him choutu")

        elif 'bye' in query:
            speak("ok sir. I am always here for you. bye bye")
            exit()
            
        