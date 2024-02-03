# SoundSeeker_TartanHacks

This app is called “SoundSeeker”. It is an Optical Music Recognition (OMR) app that allows users to upload images of music notes on a staff, and in turn, the app will label each note with the appropriate letter. There is also an interactive component past the recognition phase, in which the user can select specific notes on a separate staff, and the app will play the sound of that note.

This project was developed in Python. We built our OMR framework upon Ojaas Hampiholi’s open source project available on GitHub, (“Optical_Music_Recognition.”) The input image is analyzed and notes are recognized based on the space between the detected note and lines on the staff. This is achieved through edge detection and template matching based on previously provided training data. 

The output image contains the detected notes along with the appropriate letter. Boxes are also drawn around each note that was recognized for easier readability. This is what is displayed on the app interface. 

