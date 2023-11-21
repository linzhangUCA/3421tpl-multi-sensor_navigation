# Final Project (Project 3): Multi-Sensor Navigation

## Background
Navigation is an essential functionality for any mobile robot (e.g. [Warthog](https://youtu.be/GAveEaNZZZE?si=BLWMSZ36F_Ti4tfm), [Roomba](https://youtu.be/CvZTF6YNZUw?si=JsgiMpYMYitBodM5), [Proteus](https://youtu.be/LUnZXBL_lqA?si=6UPZwneYxQJavZvq), [custom robot](https://youtu.be/jkoGkAd0GYk?si=mJk2F5EOqjExs9uL), etc.). To achieve autonomous navigation, some robots rely on complicated mathematical models, and some require fine maps. However, even without these more advanced tools, we can still navigate the robots we have built in Robotics I. In this project, we will navigate our robots through out of the maze in LSCA 105.

## Requirements:
Start the robot at the starting line. The robot needs to autonomously navigate to the destinition using all kinds of sensors. The navigation is broken down into 3 stages with 3 different but essential sensors:
1. Encoder navigation
2. Lidar navigation
3. Camera navigation

The 3 sensors listed above are mandatory in the corresponding stage. **You cannot use any of these 3 in other stages (e.g. CANNOT use encoder in Lidar navigation)**. However, you are welcome to include sensors not on this list to help you complete the navigation.

![ms_nav](https://github.com/linzhangUCA/3421tpl-preliminary_navigation/blob/2af4a8d311817a89cc7bffb8ad65318be96f1273/multi-sensor_navigation.png)


### (60%) Coding:
As there are more more than 1 solutions, the only criterion is to navigate use the designated sensor as the main source.  
- (20%) Stage 1 - Encoder Navigation:
    - **Start the robot on or behind the "Stage 1 Start Line"**.
    - Plan a good trajectory.
    - Calculate encoder counts based on planned distances.
    - (5%) **Stop at the "Stage 2 Start Area" in the end**.
    - Refer to [Assignment 5](https://classroom.github.com/a/vAs41PAP).

- (20%) Stage 1 - Lidar Navigation:
    - Use boxes and wall to do wall following.
    - (5%) **Stop at the "Stage 3 Start Area" in the end**.
    -  **Hint: you can hard code time to stop this stage**
    - Refer to [Assignment 6](https://classroom.github.com/a/0LxkqZrp).

- (20%) Stage 3 - Camera Navigation:
    - Use a ArUco to guide the robot approaching the final destination.
    - (5%) **Stop within 1 meter to the goal**.
    - Refer to [Robotic Vision's slides](https://linzhanguca.github.io/_docs/robotics_1-2023/1114/vision.pdf).
    
#### Helpful Resources:
- [Need send data from computer to micro-controller?](https://github.com/linzhangUCA/3421tpl-preliminary_navigation/blob/e9c1038da02bca8127d7bb059af717bda7670a1a/example_computer_talker_listener.py)
- [Need send data from micro-controller to computer?]()
- [Need remotely access RPi?]()

### (40%) Documentation
A well-documented project can help people who are interested to follow. Also, it will be helpful if you want to continue the work after a while.  
1. (20%) Methods
2. (5%) Part List.
3. (15%) Wiring Diagram.
4. (10%) Summary

## Methods
> Describe the navigation methods and all the related technical details (etc. sensors, motor speed offset, algorithms). You are encouraged to draw illustrative diagrams or upload assistive files.

## Part List
> List Name, Description, Quantity for each item (in a table).

## Wiring Diagram
> Create a wiring diagram to illustrate hardware configuration
> ![image name](link)

## Summary
> Summarize the project. State the achievements of your robot. Add more technical details that are related to your robot (e.g. designs, ideas, etc.). Any supplemental materials are welcome to upload/link. 
