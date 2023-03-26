# Final Project: Robot Mapping

*Team 13: Girish, Muhammad, Andy, and Van*

Welcome to the project report for Team 13! This page contains a report of all the progress we made throughout this busy and fun quarter, including our final project.

|![](/images/car.jpg)| ![](/images/car2.jpg)|
|---|---|

*Team 13's assembled RC Car with the lidar placed at the front.*


## The Team 

|![](/images/girish.jpeg)|![](/images/muhammad.png)|![](images/andy.png)|![](/images/van.jpeg)|
|---|---|---|---|
|**Girish Krishnan** [[LinkedIn](https://linkedin.com/in/girk)]|**Muhammad Bintang Gemilang** |**Andy Zhang** |**Zhengyu (Van) Huang** |
|Electrical Engineering|Mechanical Engineering|Electrical Engineering|Computer Engineering|

## Final Project Abstract 

Our final project was themed around **mapping an unknown environment**. Our project involved the following tasks.

__What we promised__

* [✔] To implement SLAM (Simultaneous Localization and Mapping) using a lidar. This effectively creates a map of the environment around the robot, showing the locations of all objects present.
* [✔] To display the map generated from SLAM in real-time using a web application.

The __challenges faced__ during the project were:

* Integrating the web application for live previewing (HTML/CSS/JS) with the Python code needed to run SLAM.
* Avoiding delays in the updating map.

The __accomplishments__ of the project were:

* We were able to achieve a decent visualization that updates over time as the robot is driven around
* The visualization/map can be saved easily for tasks such as path planning.

__Final Presentation__

* *[Link to Final Presentation](https://docs.google.com/presentation/d/1ybNZCItvh3Inb4xyIm9jMdvE7QkdUHSAgcw-_27GDpM/edit?usp=sharing)*

* *[Link to video showing real-time mapping](https://youtu.be/89NYezgTyDc)*

__Weekly Update Presentations__

* [Project Proposal](https://docs.google.com/presentation/d/1BA-ZTRFRMCwjRi_ehfDn4Fll8nvdWeSgA-vcFacIhXk/edit?usp=sharing)
* [Week 8](https://docs.google.com/presentation/d/1aqbrDsI9-qD3Cdtn5Y08WQpj--RP-w43sHdjfP7Nmr0/edit?usp=sharing)
* [Week 9](https://docs.google.com/presentation/d/1mEIa4phqNgUHyFd5yaW6FJG1RRwc04al4UiSqWt_TiU/edit?usp=sharing)
* [Week 10](https://docs.google.com/presentation/d/1PwtRmnkmlwk-wUWYZGFs0CjX7lSMBmuzCTyH2MfmV7g/edit?usp=sharing)

__Gantt Chart__

![](/images/gantt.png)

## Hardware Setup 

* __3D Printing:__ Camera Mount, Jetson Nano Case, GPS (GNSS) Case.
* __Laser Cutting:__ Base plate to mount electronics and other components.

__Parts List__

* Traxxas Chassis with steering servo and sensored brushless DC motor
* Jetson Nano
* WiFi adapter
* 64 GB Micro SD Card
* Adapter/reader for Micro SD Card
* Logitech F710 controller
* OAK-D Lite Camera
* LD06 Lidar
* VESC
* Anti-spark switch with power switch
* DC-DC Converter
* 4-cell LiPo battery
* Battery voltage checker/alarm
* DC Barrel Connector
* XT60, XT30, MR60 connectors

*Additional Parts used for testing/debugging*

* Car stand
* USB-C to USB-A cable
* Micro USB to USB cable
* 5V, 4A power supply for Jetson Nano

#### Base Plate 

![](/images/base_plate.png)

*All measurements shown above are in millimeters (mm)*

Our base plate was laser cut on a thick acrylic sheet. The circular hole at the end of the base plate is meant to hold the power on/off button. The long holes in the side of the plate are meant for wires to easily pass to and from the bottom of the plate.

#### Camera Mount 

|![](/images/camera_mount.png)|![](/images/camera_mount_base.png)|
|---|---|
|Camera Holder|Base for attachment to base plate|

The two parts of the camera mount shown above were screwed together. The angle of the camera was carefully chosen (facing downward approximately 10 degrees from the vertical) so that the road ahead is clearly visible. This is essential for accurate results in OpenCV/ROS2 autonomous laps.

One of our older camera mount designs is shown below.

|![](/images/camera_mount_rotate.png)|
|---|

This camera mount consists of three parts: one base for attachment to the base plate, one middle piece to connect the base and the camera, and the camera holder. This camera mount design allows you to rotate the camera up and down. However, it is important that the rotating hinge is screwed securely so that the hinge doesn't wobble out while the robot does autonomous laps!

#### Jetson Nano Case 

*Credit to flyattack from Thingiverse, see: https://www.thingiverse.com/thing:3532828*


|![](/images/jetson_case.jpeg)|
|---|

This case is excellent because it is robust and doesn't break easily, unlike most common Jetson Nano cases.

#### Electronics Circuit Diagram 

![](/images/circuit.png)

*Note: some of these components and connections will vary depending on the exact components you have - check the component specifications carefully.*

## Software Documentation 



## Autonomous Laps 

As part of the class deliverables and as preparation for the final project, here are our autonomous laps videos:

__Donkey Sim__

* Local Computer: https://youtu.be/lXEStSEVikQ
* GPU training: https://youtu.be/4_BzKP9-XAQ
* External Server: https://youtu.be/Yvo1yqRJhX4

__Physical Robot__

* DonkeyCar: https://youtu.be/bPUSS2g0Ves
* Lane detection using OpenCV + ROS2: https://youtu.be/omcDCBSrl2I
* Inner lane: https://youtu.be/9hN8HUlGcas
* Outer lane: https://youtu.be/nXZNPscVlX0
* GPS: https://youtu.be/Y3I9AWW1R6o

## Acknowledgements 

Thanks Prof. Jack Silberman and TAs Moises Lopez and Kishore Nukala for an awesome quarter! See you in DSC 178 next quarter, professor Jack ;)

## Credit and References

* Jetson Nano Case Design: https://www.thingiverse.com/thing:3532828

* Lidar (LD06) Python Tutorial: https://github.com/henjin0/LIDAR_LD06_python_loder
* PyVESC: https://github.com/LiamBindle/PyVESC
* SLAM tutorial, Dominic Nightingale. https://gitlab.com/ucsd_robocar/ucsd_robocar_nav1_pkg/-/tree/master/