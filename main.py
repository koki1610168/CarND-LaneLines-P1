from detect_lanes import LaneDetection
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import os

#image = mpimg.imread('test_images/solidWhiteRight.jpg')
#print('This image is:', type(image), 'with dimentions:', image.shape)
#plt.imshow(image)
#plt.show()

#dimentions of (540, 960, 3)

kernel_size = 5
low_threshold = 50
high_threshold = 150
#vertices = np.array([[0, image.shape[0]], [490, 310], [image.shape[1], image.shape[0]]])
rho = 1
theta = np.pi/180
threshold = 15
min_line_len = 10
max_line_gap = 160

#line_detection = LaneDetection(image)
#final_image = line_detection.process_image(image, low_threshold, high_threshold, vertices, rho, theta, threshold, min_line_len, max_line_gap, kernel_size)

#files = os.listdir('test_images')

#plt.figure(figsize=(10, 5))

#for i in range(len(files)):
#    image = mpimg.imread('test_images/' + files[i])
#    line_detection = LaneDetection(image)
#    final_image = line_detection.process_image(image, low_threshold, high_threshold, vertices, rho, theta, threshold, min_line_len, max_line_gap, kernel_size)
#    plt.subplot(3, 2, i+1)
#    plt.axis('off')
#    plt.tight_layout()
#    plt.imshow(final_image)

cap = cv2.VideoCapture('test_videos/solidYellowLeft.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
while(cap.isOpened()):
    _, frame = cap.read()
    vertices = np.array([[0, frame.shape[0]], [490, 325], [frame.shape[1], frame.shape[0]]])
    lane_detection = LaneDetection(frame)
    final_image = lane_detection.process_image(frame, low_threshold, high_threshold, vertices, rho, theta, threshold, min_line_len, max_line_gap, kernel_size)
    cv2.imshow('result', final_image)

    if cv2.waitKey(int(fps//2)) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#plt.show()
