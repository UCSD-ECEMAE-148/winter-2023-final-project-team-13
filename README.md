#<center>Final Project: Robot Mapping and Navigation</center>

*<center>Team 13: Girish, Muhammad, Andy, and Van</center>*

Welcome to the project report for Team 13! This page contains a report of all the progress we made throughout this busy and fun quarter, including our final project.

![](/images/car.jpg)

*<center>Team 13's assembled RC Car with the lidar placed at the front.</center>*



##<center>The Team</center>

|![](/images/girish.jpeg)|![](/images/muhammad.png)|![](images/andy.png)|![](/images/van.jpeg)|
|---|---|---|---|
|**Girish Krishnan** [[LinkedIn](https://linkedin.com/in/girk)]|**Muhammad Bintang Gemilang** |**Andy Zhang** |**Zhengyu (Van) Huang** |
|Electrical Engineering|Mechanical Engineering|Electrical Engineering|Computer Engineering|

##<center>Final Project Abstract</center>

Our final project was themed around **mapping an unknown environment**. Our project involved the following tasks:

* To implement SLAM (Simultaneous Localization and Mapping) using a lidar. This effectively creates a map of the environment around the robot, showing the locations of all objects present.
* To display the map generated from SLAM in real-time using a web application.

The challenges faced during the project were:

* Integrating the web application for live previewing (HTML/CSS/JS) with the Python code needed to run SLAM.
* Avoiding delays in the updating map.

The accomplishments of the project were:

* We were able to achieve a decent visualization that updates over time as the robot is driven around
* The visualization/map can be saved easily for tasks such as path planning.


*[Link to Final Presentation](https://docs.google.com/presentation/d/1ybNZCItvh3Inb4xyIm9jMdvE7QkdUHSAgcw-_27GDpM/edit?usp=sharing)*

<iframe width="560" height="315" src="https://www.youtube.com/embed/89NYezgTyDc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

##<center>Hardware Setup</center>

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

####<center>Base Plate</center>

![](/images/base_plate.png)

*<center>All measurements shown above are in millimeters (mm)</center>*

Our base plate was laser cut on a thick acrylic sheet. The circular hole at the end of the base plate is meant to hold the power on/off button. The long holes in the side of the plate are meant for wires to easily pass to and from the bottom of the plate.

####<center>Camera Mount</center>

|![](/images/camera_mount.png)|![](/images/camera_mount_base.png)|
|---|---|
|Camera Holder|Base for attachment to base plate|

The two parts of the camera mount shown above were screwed together. The angle of the camera was carefully chosen (facing downward approximately 10 degrees from the vertical) so that the road ahead is clearly visible. This is essential for accurate results in OpenCV/ROS2 autonomous laps.

One of our older camera mount designs is shown below.

|![](/images/camera_mount_rotate.png)|
|---|

This camera mount consists of three parts: one base for attachment to the base plate, one middle piece to connect the base and the camera, and the camera holder. This camera mount design allows you to rotate the camera up and down. However, it is important that the rotating hinge is screwed securely so that the hinge doesn't wobble out while the robot does autonomous laps!

####<center>Jetson Nano Case</center>

*Credit to flyattack from Thingiverse, see: https://www.thingiverse.com/thing:3532828*


|![](/images/jetson_case.jpeg)|
|---|

This case is excellent because it is robust and doesn't break easily, unlike most common Jetson Nano cases.

####<center>Electronics Circuit Diagram</center>

![](/images/circuit.png)

*<center>Note: some of these components and connections will vary depending on the exact components you have - check the component specifications carefully.</center>*

##<center>Software Documentation</center>



##<center>Autonomous Laps</center>

##<center>Acknowledgements</center>

Thanks Prof. Jack Silberman and TAs Moises Lopez and Kishore Nukala for an awesome quarter! See you in DSC 178, professor Jack ;)