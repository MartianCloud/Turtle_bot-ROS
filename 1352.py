#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math

def move_turtle():
    # Starts a new node
    rospy.init_node('node_turtle_revolve', anonymous=True)
    vel_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    #Velocity Initialization
    distance = 12.8
    vel_msg.linear.x = 1
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0.5

    while not rospy.is_shutdown():
        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            vel_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distance 
            current_distance=(t1-t0)
            #Loging Message and current distance
            rospy.loginfo("Moving in a Circle")
            rospy.loginfo(current_distance)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        #Force the robot to stop
        vel_publisher.publish(vel_msg)
        #Loging Message and Break Loop
        rospy.loginfo("goal reached")
        break

if __name__ == '__main__':
    try:
        #Staring
        move_turtle()
    except rospy.ROSInterruptException: pass