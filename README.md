# OVERVIEW
- 
This script detects and labels objects in an image using OpenCV. It reads the input image, converts it to grayscale, and applies a binary threshold to create a mask for segmentation. Contours are then detected from the mask, and small contours are filtered out based on a minimum area threshold. For each detected object, a bounding rectangle and label are drawn on the image. The processed image is displayed in a window, showing the objects identified and labeled. This program is useful for basic object detection and segmentation tasks.

# HOW IT WORKS
### 1. Input Image:
- Specify the path to the image (image_path).
- The image is loaded using OpenCV's imread function.
- Ensure the path points to a valid file, or the program will output an error.

### 2. Processing:
- The image is converted to grayscale (cv2.cvtColor), which simplifies analysis.
- A binary mask is created by applying a threshold (cv2.threshold), segmenting the image into foreground and background.

### 3. Contour Detection:
- The cv2.findContours function detects contours in the binary mask.
- Small contours are filtered out to reduce noise by setting a minimum area threshold.

### 4. Visualization:
- Each detected object is enclosed in a green rectangle.
- Labels (Object 1, Object 2, etc.) are added near each bounding box for identification.

### 5. Output:
- Displays the processed image with contours and labels.
- Press any key to close the OpenCV window.

# KEY PARAMETERS
- Threshold: Adjust the threshold value in cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY) to optimize object detection.
- Minimum Area: Change if cv2.contourArea(contour) > 100 to filter small, irrelevant contours.
