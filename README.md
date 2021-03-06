# DATA606Project
DATA 606 Capstone Project repository 

**Real Time Courier boxes detection System using CNNs**

**Presentations**: https://github.com/ShrimanthAM/DATA606Project/tree/main/PPT

**Overview**

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


**Conclusion:**

Object detection is the core component for most of the computer vision systems, the current advancements have been used in many real time applications. 
As we know training the model is computer intensive, but attaining the inference on low compute devices not requires much of resources. Hence the future is towards predicting inference on edge devices which have limited or no access to cloud or  high compute resources. Deploying the trained model's weights on edge devices and detecting the images captured on the go by running a forward pass along with the pre-trained weights will surely lead to many more applications.


**References**

1. Becoming Blind Is a Top 4 Fear – Smart Vision Labs. “Why Vision Is the Most Important Sense Organ.” Smart Vision Labs, 29 Jan. 2017, www.smartvisionlabs.com/blog/why-vision-is-the-most-important-sense-organ/.
2. Brownlee, Jason. “A Gentle Introduction to Computer Vision.” Machine Learning Mastery, 5 July 2019, machinelearningmastery.com/what-is-computer-vision/.
3. Redmon, Joseph, and Ali Farhadi. “YOLO9000: Better, Faster, Stronger.” 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, doi:10.1109/cvpr.2017.690.
4. Redmon, Joseph, et al. “You Only Look Once: Unified, Real-Time Object Detection.” 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, doi:10.1109/cvpr.2016.91.
5. Redmon, J. (n.d.). Darknet: Open Source Neural Networks in C. https://pjreddie.com/darknet/.
