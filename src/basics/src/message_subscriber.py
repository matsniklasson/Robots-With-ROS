#!/usr/bin/python3

import rospy

from basics.msg import Complex

def callback(msg):
    print('Real: ', msg.real)
    print('Imaginary: ', msg.imaginary)
    print('\n')

rospy.init_node('message_subscriber')

sub = rospy.Subscriber('complex', Complex, callback)

rospy.spin()