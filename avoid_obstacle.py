#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(scan_data):
    min_range = min(scan_data.ranges[0:10] + scan_data.ranges[-10:])  # Check front
    rospy.loginfo("Min distance in front: %f", min_range)

    cmd = Twist()
    if min_range < 0.5:
        cmd.linear.x = 0.0
        cmd.angular.z = 0.5  # Turn if obstacle is close
    else:
        cmd.linear.x = 0.2
        cmd.angular.z = 0.0  # Move forward

    pub.publish(cmd)

rospy.init_node('obstacle_avoider')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)

rospy.spin()
