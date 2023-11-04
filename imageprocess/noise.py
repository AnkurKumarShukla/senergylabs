import cv2
import numpy as np

# Load color image
img = cv2.imread('imageprocess\image.png')
print(img)
# print(img.shape())
# Add Gaussian noise of varying levels
noise1 = np.random.normal(loc=0, scale=10, size=img.shape) 
noise2 = np.random.normal(loc=0, scale=40, size=img.shape)
noise3 = np.random.normal(loc=0, scale=100, size=img.shape)

noisy_img1 = np.clip(img + noise1, 0, 255).astype(np.uint8)
noisy_img2 = np.clip(img + noise2, 0, 255).astype(np.uint8) 
noisy_img3 = np.clip(img + noise3, 0, 255).astype(np.uint8)

# Non-local means filter with small window
filtered1 = cv2.fastNlMeansDenoisingColored(noisy_img1, None, h=10, hColor=10, templateWindowSize=3, searchWindowSize=7)

# Non-local means filter with medium window 
filtered2 = cv2.fastNlMeansDenoisingColored(noisy_img2, None, h=10, hColor=10, templateWindowSize=5, searchWindowSize=15)

# Non-local means filter with large window
filtered3 = cv2.fastNlMeansDenoisingColored(noisy_img3, None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21) 

# Save filtered images
cv2.imwrite('filtered_low_noise.jpg', filtered1)
cv2.imwrite('filtered_med_noise.jpg', filtered2)
cv2.imwrite('filtered_high_noise.jpg', filtered3)