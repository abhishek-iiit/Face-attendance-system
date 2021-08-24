# Face Attendance System

An efficient way to manage the attendance records for employee or students. It uses face recognition technique to increase the accuracy and requires less time than any other method. The results showed improved performance over manual attendance system.

![Face-attendance-system](https://user-images.githubusercontent.com/69477761/130632299-3f1993df-01c5-4d92-9081-8e6fe20cfe73.png)

## Table of Content
- [Libraries Used](#libraries)
- [Advantages](#advantages)
- [Usage](#usage)
- [Flowchart](#flowchart)
- [Demo Video](#demo)
- [References](#references)
- [Bug Reporting](#bug-reporting)
- [Feature Request](#feature-request)
- [License](#license)

![Screenshot from 2021-03-19 14-09-58](https://user-images.githubusercontent.com/69477761/111753506-f1fc3900-88bc-11eb-8e27-237424a706a5.png)

<a id="libraries"></a>

## 📚 Libraries Used
1. [Python](https://www.python.org/downloads/) installed (version >= 3.6)
2. [OpenCV](https://pypi.org/project/opencv-python/) installed for face recognition
```sh
pip install opencv-python
```
3. [NumPy](https://numpy.org/install/) installed to perform the matrix task
```sh
pip install numpy
```
4. [Pandas](https://docs.python.org/3/library/tkinter.html) installed to store student information in local database
```sh
pip install pandas
```
5. [TKinter](https://docs.python.org/3/library/tkinter.html) installed to make GUI for better interaction with the program
```sh
pip install tk
```
6. [PIL](https://pypi.org/project/Pillow/) installed to create and save images
```sh
pip install Pillow
```

<a id="advantages"></a>

## 💫 Advantages

1. Zero dependencies
2. Simple to operate with good accuracy
3. Able to handle large database and store large number of images for training
4. Network connectivity is not required which result to no network related problems

<a id="usage"></a>

## 🎩 Usage

1. Run the below command in the terminal to open the interface:
```sh
python3 train.py
```
2. For first time user/registration, enter the `ID`, `Name` and click on `Take Images` to take multiples images one-by-one.
3. For confirmation, we are shown the details entered in `Notification`.
4. Click on `Train Images` to train your captured image you just took in Step2.
5. Once registered, you can now `Track Images` to take-up the attendance and store it in database (here excel).
6. For confirmation, we are shown the details captured in `Attendance`.

Now, you are ready to use the software.

<a id="Flowchart"></a>

## ⚔️ Flowchart

![Screenshot from 2021-08-25 01-15-59](https://user-images.githubusercontent.com/69477761/130680150-fb02f450-afe4-479e-918d-d40fc62783fc.png)

<a id="demo"></a>

## 🎮 Demo Video

https://user-images.githubusercontent.com/69477761/130678138-dada31a8-4d76-4e23-8ad0-f47f38f40123.mp4

<a id="references"></a>

## 🔬 References

* [Automatic Attendance System Using Face Recognition Technique](https://www.ijrte.org/wp-content/uploads/papers/v9i1/A2644059120.pdf).
* [Automated Student Attendance Management System Using Face Recognition](https://www.researchgate.net/publication/327671423_Automated_Student_Attendance_Management_System_Using_Face_Recognition).

<a id="bug-reporting"></a>

## 🐛 Bug Reporting

Feel free to [open an issue](https://github.com/abhishek-iiit/Face-attendance-system/issues) on GitHub if you find any bug.

<a id="feature-request"></a>

## ⭐ Feature Request

- Feel free to [Open an issue](https://github.com/abhishek-iiit/Face-attendance-system/issues) on GitHub to request any additional features you might need for your use case.
- Connect with me on [LinkedIn](https://www.linkedin.com/in/abhishek-iiit/). I'd love ❤️️ to hear where you are using this system.

<a id="license"></a>

## 📜 License

This software is open source, licensed under the [MIT License](https://github.com/abhishek-iiit/Face-attendance-system/blob/main/LICENSE).
