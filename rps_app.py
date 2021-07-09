import tensorflow as tf
model = tf.keras.models.load_model("my_model.hdf5")
import streamlit as st
st.write("""
         # Image Classification CIFAR10
         """
         )
st.write("This is a simple image classification web app")
file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
        img=image_data.resize((32,32))
        #size = (32,32)    
        #image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        #image = np.asarray(image)
        #img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        xtest=tf.convert_to_tensor(np.array([np.asarray(img)]))
        
        
    
        prediction = np.asfarray(model(xtest))
        
        return prediction[0]
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    
    if np.argmax(prediction) == 0:
        st.write("It is an airplane!")
    elif np.argmax(prediction) == 1:
        st.write("It is an automobile!")
    elif np.argmax(prediction) == 2:
        st.write("It is a bird!")
    elif np.argmax(prediction) == 3:
        st.write("It is a cat!")
    elif np.argmax(prediction) == 4:
        st.write("It is a deer!")
    elif np.argmax(prediction) == 5:
        st.write("It is a dog!")
    elif np.argmax(prediction) == 6:
        st.write("It is a frog!")
    elif np.argmax(prediction) == 7:
        st.write("It is a horse!")
    elif np.argmax(prediction) == 8:
        st.write("It is a ship!")
    else:
        st.write("It is a truck!")

    
    st.text("Probability (0: Airplane, 1: Automobile, 2: Bird, 3: Cat, 4: Deer, 5: Dog, 6: Frog, 7: Horse, 8: Ship, 9: Truck)")
    st.write(prediction)