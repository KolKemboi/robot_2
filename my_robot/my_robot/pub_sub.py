#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class Publisher(Node):
    def __init__(self):
        super().__init__("Publisher")
        self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.send_vel_cmd)

    def send_vel_cmd(self):
        msg = Twist()
        msg.linear.x = 4.0
        msg.angular.z = 2.0
        self.cmd_vel_pub.publish(msg)
        self.get_logger().info("Publisher")


class Subscriber(Node):
    def __init__(self):
        super().__init__("Subscriber")
        self.subscriber = self.create_subscription(Pose, 
                                                   "/turtle1/pose", 
                                                   self.pose_callback, 
                                                   10)##creates a subscription taking in the datatype 'Pose',then the topic name, then a callback and a queue size for laggy systems
    

    def pose_callback(self, msg: Pose):
        self.get_logger().info(str(msg))#parses the msg recieved from the publisher and logs it


def publisher(args = None):
    rclpy.init(args = args)
    pub = Publisher()
    rclpy.spin(pub)
    rclpy.shutdown()

def subscriber(args = None):
    rclpy.init(args = args)
    sub = Subscriber()
    rclpy.spin(sub)
    rclpy.shutdown()