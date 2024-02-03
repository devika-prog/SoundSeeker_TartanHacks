# SoundSeeker_TartanHacks

This app is called “SoundSeeker”. It is an Optical Music Recognition (OMR) app that allows users to upload images of music notes on a staff, and in turn, the app will label each note with the appropriate letter. There is also an interactive component past the recognition phase, in which the user can select specific notes on a separate staff, and the app will play the sound of that note.

This project was developed in Python. We built our OMR framework upon Ojaas Hampiholi’s open source project available on GitHub, (“Optical_Music_Recognition.”) The input image is analyzed and notes are recognized based on the space between the detected note and lines on the staff. This is achieved through edge detection and template matching based on previously provided training data. 

The output image contains the detected notes along with the appropriate letter. Boxes are also drawn around each note that was recognized for easier readability. This is what is displayed on the app interface. 

-------------------------------------------------------------------------------------------------
References:
Sound Library: 
https://samplefocus.com/tag/piano-note

Music Notes Image:
 https://www.musora.com/musora-cdn/image/quality=85/https://pianote.s3.us-east-1.amazonaws.com/blog/2020/Read%20Ledger%20Lines/treble-clef.png

MIT License

Copyright (c) 2021 Ojaas Hampiholi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

