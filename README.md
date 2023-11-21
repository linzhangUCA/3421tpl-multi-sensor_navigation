# Final Project (Project 3): Multi-Sensor Navigation

## Background
Navigation is an essential functionality for any mobile robot (e.g. [Warthog](https://youtu.be/GAveEaNZZZE?si=BLWMSZ36F_Ti4tfm), [Roomba](https://youtu.be/CvZTF6YNZUw?si=JsgiMpYMYitBodM5), [Proteus](https://youtu.be/LUnZXBL_lqA?si=6UPZwneYxQJavZvq), [custom robot](https://youtu.be/jkoGkAd0GYk?si=mJk2F5EOqjExs9uL), etc.). To achieve autonomous navigation, some robots rely on complicated mathematical models, and some require fine maps. However, even without these more advanced tools, we can still navigate the robots we have built in Robotics I. In this project, we will navigate our robots through out of the maze in LSCA 105.

## Requirements:
Start the robot at he starting line. The robot needs to autonomously navigate to the destinition using all kinds of sensors. The navigation is broken down into 3 stages with 3 different but essential sensors:
1. Encoder navigation
2. Lidar navigation
3. Camera navigation
The 3 sensors listed above are mandatory in the corresponding stage. **You cannot use any of these 3 in other stages (e.g. CANNOT use encoder in Lidar navigation)**. However, you are welcome to include sensors not on this list to help you complete the navigation.
![]()

**Note: DO NOT HARD CODE. Use at least one sensor. Or, 45% credits will not be given.**

### (50%) Robot Performance:
- (5%) Modes:
    - The robot has 3 modes: **WORK**, **PAUSE** and **OFF**. 
    - One LED will be used to indicate the robot's status ("always on" for **WORK**, "fade-in-fade-out" for **PAUSE**, "off" for **OFF**).
    - A button will be used to switch modes bewteen **WORK** and **PAUSE**.

- (10%) Checkpoint 1
    - The robot successfully passes the `Checkpoint 1` line starting from the `Start` line.
- (10%) Checkpoint 2
    - The robot successfully passes the `Checkpoint 2` line starting from the `Start` line.
- (10%) Checkpoint 3
    - The robot successfully passes the `Checkpoint 3` line starting from the `Start` line.
- (15%) Finish Marker
    - (5%) The robot successfully reached the `Finish` marker starting from the `Start` line.
    - (5%) The robot stopped at the `Finish` marker within 0.5 meters radius.
    - (5%) Turn off everything (except Raspberry Pi) on board.
    
**Note: you can guide your robot using ArUco marker after the robot passed Checkpoint 3.**
    

### (50%) Documentation
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
