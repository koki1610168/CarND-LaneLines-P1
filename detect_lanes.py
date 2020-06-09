import numpy as np
import cv2


class LaneDetection:
    def __init__(self, image):
        self.image = image

    def grayscale(self, image):
        return cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

    def canny(self, image, low_threshold, high_threshold):
        return cv2.Canny(image, low_threshold, high_threshold)

    def gaussian_blur(self, image, kernel_size=5):
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    def region_of_interest(self, image, vertices):
        """
        Applies an image mask
        cut off an uneccesary part of the image
        """
        mask = np.zeros_like(image)

        if len(image.shape) > 2:
            channel_count = image.shape[2]
            ignore_mask_color = (255,) * channel_count
        else:
            ignore_mask_color = 255

        cv2.fillPoly(mask, vertices, ignore_mask_color)

        masked_image = cv2.bitwise_and(image, mask)
        return masked_image

    def draw_lines(self, image, lines, color=[255, 0, 0], thickness=2):
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(image, (x1, y1), (x2, y2), color, thickness)

    def hough_lines(self, image, rho, theta, threshold, min_line_len, max_line_gap):
        lines = cv2.HoughLinesP(image, rho, theta, threshold, np.array([]), min_line_len, max_line_gap)
        line_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        self.draw_lines(line_image, lines)

        return line_image

    def weighted_image(self, image, initial_image, a=0.8, b=1, y=0.):
        return cv2.addWeighted(initial_image, a, image, b, y)

    def process_image(self, image, low_threshold, high_threshold, vertices, rho, theta, threshold, min_line_len, max_line_gap, kernel_size=5):
        grayscaled_image = self.grayscale(image)
        gaussian_blured_image = self.gaussian_blur(grayscaled_image, kernel_size)
        canny_image = self.canny(gaussian_blured_image, low_threshold, high_threshold)
        masked_edges = self.region_of_interest(canny_image, [vertices])
        line_image = self.hough_lines(masked_edges, rho, theta, threshold, min_line_len, max_line_gap)
        combined_image = self.weighted_image(line_image, self.image)
        return combined_image
