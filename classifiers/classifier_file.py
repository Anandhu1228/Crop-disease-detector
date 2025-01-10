import sys
import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('ERROR')

# Class names for models
model_class_names = {
    '1': ['Early Blight', 'Late Blight', 'Healthy'],  # POTATO
    '2': ['Bacterial Spot', 'Healthy'],              # PEPPER
    '3': ['Healthy', 'Powdery Mildew'],              # CHERRY
    '4': ['Bacterial Spot', 'Healthy'],              # PEACH
    '5': ['Bacterial Blight', 'Blast', 'Brown Spot', 'Tungro'],  # RICE
    '6': ['Healthy', 'Leaf Scorch'],                 # STRAWBERRY
    '7': ['Common Rust', 'Gray Leaf Spot', 'Healthy', 'Northern Leaf Blight'],  # CORN
    '8': ['Leaf Blight', 'Black Measles', 'Black Rot', 'Healthy'],  # GRAPE
    '9': ['Healthy', 'Mosaic', 'Red Rot', 'Rust', 'Yellow Leaf']  # SUGARCANE
}

def load_trained_model(plant_id):
    base_dir = os.getcwd()
    model_path = os.path.join(base_dir,'classifiers', 'models', plant_id)
    model = load_model(model_path)
    return model

def load_image_from_directory(temp_image_path):
    # Load and preprocess the image directly from the directory without subdirectory constraints.
    imsz = 256
    # Find the first image in the directory
    image_files = [f for f in os.listdir(temp_image_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    if not image_files:
        raise FileNotFoundError(f"No images found in directory {temp_image_path}")

    # Load the first image
    image_path = os.path.join(temp_image_path, image_files[0])
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(imsz, imsz))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, axis=0)  # Add batch dimension

    return img_array



# IF WANTED TO USE TEST SUBDIRECTORY INSIDE TEMP_IMAGE LIKE STRUCTURE WHEN TRAINED
# def load_image_from_directory(temp_image_path):
#     """Load and preprocess the image from the directory."""
#     imsz = 256  # Image size
#     dataset = tf.keras.preprocessing.image_dataset_from_directory(
#         temp_image_path,
#         image_size=(imsz, imsz),
#         batch_size=1,
#         shuffle=False  # Load single image without shuffling
#     )

#     for images, labels in dataset.take(1):
#         # `images` contains the preprocessed image
#         # We don't need `labels` here as it's just for prediction
#         return images.numpy()



def predict_image(model, input_image, class_names):
    """Perform prediction and format the result."""
    predictions = model.predict(input_image)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]

    return predicted_class

def main():
    try:
        plant_id = sys.argv[1]
        temp_image_path = os.path.join(os.getcwd(),'classifiers', 'temp_image')

        model = load_trained_model(plant_id)
        class_names = model_class_names.get(plant_id, [])
        input_image = load_image_from_directory(temp_image_path)
        predicted_class = predict_image(model, input_image, class_names)

        sys.stdout.write(predicted_class)

    except Exception as e:
        sys.stderr.write(f"Error: {str(e)}\n")

if __name__ == "__main__":
    main()
