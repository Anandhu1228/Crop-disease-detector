I HAD MOVED TRAINING FILE OF EACH CROP CATEGORY FROM MAIN DIRECTORY TO RESPECTIVE FOLDERS AFTER ALL TRAINING.

THEN REMOVED ALL THE IMAGE DATASET
YOU CAN GET IT FROM 
https://www.kaggle.com/datasets/nirmalsankalana/plant-diseases-training-dataset

ALSO EACH CROP FOLDER CONTAINS RESPECTIVE READ_ME FILES WHICH CONTAINS THE CLASS NAMES


ALSO THESE MODELS CURRESPONDS TO THESE FOLDERS:

{
    1: "POTATO",
    2: "PEPPER",
    3: "CHERRY",
    4: "PEACH",
    5: "RICE",
    6: "STRAWBERRY",
    7: "CORN",
    8: "GRAPE",
    9: "SUGARCANE",
}

TRIED QUANTIZED AWARE MODEL FOR PEPPER,BUT ACCURACY WAS NOT AS EXPECTED
ERROR IN TRAINING TOMATO CLASSIFIER AS VERY LARGE NUMBER OF DATASETS WITH HIGH COMPUTATION RESULTED IN MEMORY BECOMING FULL AND CRASHING CONTINUOUSLY.
TRIED TRANSFER LEARNING TECHNIQUE AS USED PRETRAINED POTATO MODEL UPTO DENSE LAYER IS USED TO REDUCE COMPUTATION.
WORKED , BUT CRASHED AT 9TH EPOCH DUE TO THE SAME MEMORY FULL REASON.
EITHER NEEDED TO REDUCE IMAGE SIZE, BATCH SIZE, NUMBER OF IMAGES, BUT RESULTS IN LESS ACCURACY. TRIED MULTILEWAYS.
BUT DUE TO HARDWARE LIMITATIONS, DROPPED FOR POTATO 


model and classes:

1:
['Potato___Early_blight', 
 'Potato___Late_blight', 
 'Potato___healthy']


2:
['Pepper__bell___Bacterial_spot', 
 'Pepper__bell___healthy']


3:
['Cherry___healthy', 
 'Cherry___powdery_mildew']


4:
['Peach___bacterial_spot', 
 'Peach___healthy']


5:
['Rice___bacterial_blight',
 'Rice___blast',
 'Rice___brown_spot',
 'Rice___tungro']


6:
['Strawberry___healthy', 
 'Strawberry___leaf_scorch']


7:
['Corn___common_rust',
 'Corn___gray_leaf_spot',
 'Corn___healthy',
 'Corn___northern_leaf_blight']


8:
['Grape___Leaf_blight',
 'Grape___black_measles',
 'Grape___black_rot',
 'Grape___healthy']


9:
['Sugercane___healthy',
 'Sugercane___mosaic',
 'Sugercane___red_rot',
 'Sugercane___rust',
 'Sugercane___yellow_leaf']
