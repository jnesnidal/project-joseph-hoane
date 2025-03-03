#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def move_ur10e():
    # Initialize the ROS node
    rospy.init_node('ur10e_commander', anonymous=True)
    
    # Define the topic for the joint trajectory controller
    pub = rospy.Publisher('/eff_joint_traj_controller/command', JointTrajectory, queue_size=10)
    
    # Allow some time for the publisher to establish connection
    rospy.sleep(1)
    
    # Create a JointTrajectory message
    traj = JointTrajectory()
    traj.joint_names = [
        'shoulder_pan_joint',
        'shoulder_lift_joint',
        'elbow_joint',
        'wrist_1_joint',
        'wrist_2_joint',
        'wrist_3_joint'
    ]

    # Create a JointTrajectoryPoint message
    point = JointTrajectoryPoint()
    point.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Target joint positions in radians
    point.time_from_start = rospy.Duration(2.0)  # Duration to achieve the positions

    # Add the point to the trajectory
    traj.points.append(point)

    # Publish the command to move the robot
    rospy.loginfo("Sending joint trajectory command to UR10e...")
    pub.publish(traj)

    # Keep the node running until the movement is complete
    rospy.sleep(2)

    rospy.loginfo("Movement complete.")

if __name__ == '__main__':
    try:
        move_ur10e()
    except rospy.ROSInterruptException:
        pass
