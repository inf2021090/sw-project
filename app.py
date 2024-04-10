import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Function to apply filter
def apply_filter(image, filter_type):
    if filter_type == 'Grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'Blur':
        return cv2.blur(image, (5, 5))
    elif filter_type == 'Canny Edge Detection':
        return cv2.Canny(image, 100, 200)
    else:
        return image

# Streamlit app
def main():
    st.title('Simple Image Filter App')
    
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.image(image, caption='Original Image', use_column_width=True)
        
        filter_type = st.selectbox('Select Filter', ('Grayscale', 'Blur', 'Canny Edge Detection'))
        
        if st.button('Apply Filter'):
            filtered_image = apply_filter(image, filter_type)
            st.image(filtered_image, caption='Filtered Image', use_column_width=True)
            
            # Display histogram for grayscale image
            if filter_type == 'Grayscale':
                hist = cv2.calcHist([filtered_image], [0], None, [256], [0, 256])
                plt.plot(hist)
                st.pyplot()

if __name__ == '__main__':
    main()
