#!/usr/bin/env python
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
"MAKE THE FILE EXECUTABLE BY RUNNING chmod +x vision.py"
bridge = CvBridge()
rospy.init_node('opencv_example', anonymous=True)   
def image_callback(img_msg):
     
    try:
         cv_image = bridge.imgmsg_to_cv2(img_msg, "bgr8")
    except(CvBridgeError, e):
         rospy.logerr("CvBridge Error: {0}".format(e))

    #ADD IMAGE FUNCTION HERE
    cv2.imshow("Image Window", cv_image)
    cv2.waitKey(3)

while not rospy.is_shutdown():
     sub_image = rospy.Subscriber("/rrbot/camera1/image_raw", Image, image_callback)
     rospy.spin()
    