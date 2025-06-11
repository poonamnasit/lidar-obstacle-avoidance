# LIDAR Obstacle Avoidance with TurtleBot3

🤖 This project uses LIDAR sensor data from a TurtleBot3 robot to detect obstacles and navigate around them in a simulated ROS environment.

---

## 🎯 Project Goal

To implement a basic obstacle avoidance algorithm using `/scan` LIDAR data and `geometry_msgs/Twist` to make the robot react in real-time.

---

## 💻 What I Did

- Subscribed to `/scan` topic (LaserScan)
- Processed LIDAR data to detect close obstacles in front of the robot
- Published velocity commands to `/cmd_vel` to avoid collisions
- Ran the simulation using The Construct platform with TurtleBot3 in Gazebo

---

## 🧠 Key Learnings

- Real-time data subscription in ROS
- Basic reactive robot behaviors
- LIDAR distance filtering and angle slicing
- Writing callback functions with rospy

---

## 📁 File Structure

robot_movement/ scripts/ avoid_obstacle.py

---

## ▶️ How to Run

In your ROS environment:

```bash
# Terminal 1
roscore

# Terminal 2
rosrun robot_movement avoid_obstacle.py
```
---

Watch the robot move forward, detect obstacles with LIDAR, and turn to avoid them.

## 🛠 Tools Used

- ROS Noetic
- TurtleBot3
- Python (rospy)
- Gazebo Simulator
- The Construct platform
