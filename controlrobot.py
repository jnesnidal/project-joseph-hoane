#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

def flip_and_move_chess_piece_farther():
    rospy.init_node('ur10e_chess_piece_mover', anonymous=True)
    
    pub = rospy.Publisher('/eff_joint_traj_controller/command', JointTrajectory, queue_size=10)
    
    rospy.sleep(1)
    
    traj = JointTrajectory()
    traj.joint_names = [
        'shoulder_pan_joint',
        'shoulder_lift_joint',
        'elbow_joint',
        'wrist_1_joint',
        'wrist_2_joint',
        'wrist_3_joint'
    ]


    point1 = JointTrajectoryPoint()
    point1.positions = [3.14, -1.2, 1.0, -0.8, 0.0, 0.0]  # 180 degrees flip on the shoulder_pan_joint
    point1.time_from_start = rospy.Duration(2.0)

    point2 = JointTrajectoryPoint()
    point2.positions = [3.14, -1.5, 1.4, -1.0, 0.0, 0.0]
    point2.time_from_start = rospy.Duration(4.0)

    point3 = JointTrajectoryPoint()
    point3.positions = [3.14, -1.3, 1.2, -0.8, 0.0, 0.0]
    point3.time_from_start = rospy.Duration(6.0)

    point4 = JointTrajectoryPoint()
    point4.positions = [1.50, -1.3, 1.2, -0.8, 0.0, 0.0]  # Extended reach on the opposite side
    point4.time_from_start = rospy.Duration(8.0)

    point5 = JointTrajectoryPoint()
    point5.positions = [2.50, -1.5, 2.4, -2.0, 0.0, 0.0]
    point5.time_from_start = rospy.Duration(10.0)

   

    traj.points = [point1, point2, point3, point4, point5]

    pub.publish(traj)

    rospy.sleep(12)
    rospy.loginfo("Chess piece moved successfully .")

if __name__ == '__main__':
    try:
        flip_and_move_chess_piece_farther()
    except rospy.ROSInterruptException:
        pass
