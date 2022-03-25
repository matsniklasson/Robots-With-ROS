#! /usr/bin/python3

from multiprocessing.connection import wait
import rospy

from basics.srv import WordCount

import sys

rospy.init_node('service_client')

rospy.wait_for_service('word_count')

word_counter = rospy.ServiceProxy('word_count', WordCount)

words = ' '.join(sys.argv[1:])
word_count = word_counter(words)

print(f"Words: {words}, Count: {word_count.count}")