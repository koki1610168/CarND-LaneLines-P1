# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 6 helper functions. First, I converted the image to grayscale in order to reduce the size of an image.
Then, I blured the image to smooth it out. Thirdly, I used the canny edge detection with the threshold 15, min_lane 10 max_gap 200. Next, I masked the image with the traingle shape. The fun part was puting lines on them. Finally, combine the lines and the original image.

![alt text][image1]


### 2. Identify potential shortcomings with your current pipeline

One potential shortcoming of this pipeline is that it might not detect correct lines when it is heavy rain.

### 3. Suggest possible improvements to your pipeline

A possible improvement would be to write a class to make the pipeline easy to read.
