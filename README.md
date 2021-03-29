# DATA606Project
DATA 606 Capstone Project repository 

Real Time Courier boxes detection System using CNNs


Overview

The aim of this project is to detect various courier packages that arrive at your doorstep by the images or videos captured by the Raspberry Pi camera. This falls under the category of Computer vision tasks and is a subset of object detection. The generic process of object detection is brought down to detect the various courier service providers like FedEx, UPS, USPS, Amazon by identifying the logos on the packages along with the bounding boxes. I will be using the YOLO framework for object detection. 



Detection of objects involves all the steps of a machine learning pipeline. So will discuss them in detail in the below sections

1. Data Source and collection: 
In order to implement the project, we have to train the model to detect these specific logos in the given image or video. As the data is scenario-specific, I will be creating custom images set for each of these companies that have the target logos in them. 
* Data collection: Scrapping of images with these logos from Google images using selenium.
* Data augmentation: Augmenting the real data to produce new fake images that can be used for training. (Neural networks perform better when trained on huge data) 
* Data labeling: Annotations are vital in object detection, so I'm planning of using an open-source tool to label the images. 
Once the training data is ready it has to be converted in the format how the YOLO framework accepts
2. Training the model using the YOLO framework 
3. Testing the model 


Data Annotation steps - LabelImg open source tool
  1. intsall LabelImg tool as per the https://github.com/tzutalin/labelImg#labelimg
  2. execute tha application(labelImg.py)
  3. Open the directory of the images to be labelled 
  4. change the format to Yolo in left side bar 
  5. select create rec box and draw the bounding box around the object 
  6. add the class name in the label list and select it
  7. save the label.txt file created in the labels directory


