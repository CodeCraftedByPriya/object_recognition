import cv2

# Define the path to the input image
image_path = r'C:\Users\Priyalakshmi\Pictures\Screenshots\desk.png'

# Print the file path to ensure it's correct
print(f"Image path: {image_path}")

# Read the input image
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print(f"Error: Could not open or find the image at {image_path}")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to the grayscale image to create a binary mask
    _, binary_mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the binary mask
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours and label each object on the original image
    object_count = 0
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Filter out small contours
            object_count += 1
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, f'Object {object_count}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the original image with contours and labels
    cv2.imshow('Original Image with Contours and Labels', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
