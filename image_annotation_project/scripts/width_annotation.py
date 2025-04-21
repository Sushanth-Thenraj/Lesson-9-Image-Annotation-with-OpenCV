import cv2
import matplotlib.pyplot as plt
import os

# Load the image
image_path = 'image_annotation_project/original_images/example.jpg'  # Corrected path
print(f"Loading image from: {os.path.abspath(image_path)}")  # Debugging tip
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Image not found at path: {image_path}")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Determine the width of the image
height, width, _ = image.shape

# Create Bi-directional lines along the width
line_start = (20, height - 50)  # Start near the bottom-left
line_end = (width - 20, height - 50)  # End near the bottom-right

# Draw the lines on the image
cv2.arrowedLine(image, line_start, line_end, (255, 0, 0), 3, tipLength=0.05)
cv2.arrowedLine(image, line_end, line_start, (255, 0, 0), 3, tipLength=0.05)

# Annotate width length onto line
width_position_label = (width // 2, height - 60)  # Position above the line
cv2.putText(image, f'Width: {width}px', width_position_label, cv2.FONT_HERSHEY_SIMPLEX, .8, (255, 0, 0), 2, cv2.LINE_AA)

# Display the image with annotations
plt.figure(figsize=(12, 8))
plt.imshow(image)
plt.title("Width of Image")
plt.axis('off')
plt.show()

# Save the annotated image
cv2.imwrite('image_annotation_project/output_images/Width_Annotation.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

# Close all windows
cv2.destroyAllWindows()