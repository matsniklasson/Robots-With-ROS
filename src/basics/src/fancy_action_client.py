#! /usr/bin/python3

import rospy
import time
import actionlib
from basics.msg import TimerAction, TimerGoal, TimerResult, TimerFeedback

def feedback_cb(feedback: TimerFeedback):
    print(f'[Feedback] Time elapsed: {feedback.time_elapsed.to_sec()}')
    print(f'[Feedback] Time remaining: {feedback.time_remaining.to_sec()}')

rospy.init_node('timer_action_client')
client = actionlib.SimpleActionClient('timer', TimerAction)
client.wait_for_server()

goal = TimerGoal()
goal.time_to_wait = rospy.Duration.from_sec(5.0)
# Server-side abort
goal.time_to_wait = rospy.Duration.from_sec(500.0)
client.send_goal(goal, feedback_cb=feedback_cb)

# Goal preemption
time.sleep(3.0)
client.cancel_goal()

client.wait_for_result()
print(f"[Result] State: {client.get_state()}")
print(f"[Result] Status: {client.get_goal_status_text()}")
print(f"[Result] Time elapsed: {client.get_result().time_elapsed.to_sec()}")
print(f"[Result] Updates sent: {client.get_result().updates_sent}")
