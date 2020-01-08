# OpenCV Project Pages
## OpenCV project developed in *Python*

**Using Spyder 3.2.3 and Anaconda Navigator**

First project to explore simple facial recognition through the use of *Haar Features.*

This library is self-contained through the [OpenCV project](https://opencv.org) using its 4.1.2 packages. *(As of Dec. 23, 2019, OpenCV released 4.2.0)* I plan to update my computer vision detection project to OpenCV 4.2.0 in the next few iterations.

## OpenCV 4.1.2 in a Spyder framework or Microoft Visual Code

Overall, the opporunity presented more complex in the establishing the environment in *Anaconda.* The dependencies I highlighted briefly in my blog [jeremywood.ai](https://jeremywood.ai/python-environment-assembly-for-opencv/).
My initial run of my *python* code testing better inside *Visual Code 14.0.* I have since adjusted the computer vision detection lines to better accommodate a new *pyhton* environment that I have exported into [OpenCV_v3.txt](https://github.com/jeremywood-ai/computer-vision.github.io/blob/master/openCV_v3.1.txt) for others to reveiw. There are addition packages I have added for coding amenities and platform versatility I was able to refined it better to my workflow in *Spyder*.

## Computer Vision Proof of Detection

This projects set up how to use OpenCV's library to create a webcam person detection system.

### List of Detectors Used

- haarcascade_eye.xml                   : detect eye features
- haarcascade_frontalface_default.xml   : detect full face features
- haarcascade_smile.xml                 : detect a smile on a person

## A Note on the Python Environment for openCV project 1.0

One of the largest packages to disrupt the environment:

- **MKL 2019** : Intel's *Math Kernel Library* "highly optimized, extensively threaded, and thread-safe library of mathematical functions for engineering, scientific, and financial applications that require maximum performan" [Intel Developer Zone](https://software.intel.com/en-us/forums/intel-math-kernel-library/topic/796407). I wanted it for the multithreading ability that I will soon weave into newer versions. Additionally, Intel's *Deep Neural Networking* code was deprecrated, and soon will be incorporated into MKL.

- **Python 3.6.7** : This was my choice to launch the *python* platform. With a year of maturity, Oct. 2018 and its seventh maintenance update, I felt this version would have many of its bugs and nuiances understood. Additionally, for this project, the version would play a role in syntax and memory use. Later plans are for the code to update to *Python 3.8.x*.

- **DefusedXML 0.6.0** : Knowing that I am going to use XML for the *Haar Feature Detections*, I wanted to add into some hardened libraries to the environment, if case I needed it. This package would be used to protect the XML imports: "XML bomb protection for Python stdlib modules"

- **qtpy 1.9.0** : Versions proved with some challenges to find the one that would not break the environment. This was greatly needed for my *Spyder 3.2.3* IDE version.

- **pyflakes 2.1.1** : I added *pyflakes* for better syntax capture.

### Ending the Video Detector
Press `q` (letter **q**) when the video is active

---

### Project files:
- *myface_recognition.py*: Video detection of a person
- *myface_recognition_smile.py*: Video detection of face and a smile
---
> This is an academic course project with additional changes for my customized *Anaconda* environment, as part of [SuperDataScience](https://www.superdatascience.com/) instruction found on [Udemy](https://udemy.com) 2019
