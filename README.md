#                                 Image Retrival ( Python - Flask - NextJs )


![Screenshot 2023-04-25 211939](https://user-images.githubusercontent.com/86192249/234307338-03a511c9-b6ef-4a45-a019-8bc75842f51d.png)



## Description
  - Use VGG16 pretrained model as a extractor feature to convert and extract features on images and save them in .pkl files .
  
![image](https://user-images.githubusercontent.com/86192249/234316915-b9ab14a9-a289-462c-a5b3-0cba68fa2eca.png)

## Installations
  1) Download this repo or clone it 
  2) In terminal run command : pip install -r setup.txt 
  3) Use command ``` cd [REPO]/server ``` and ``` npm run dev ``` to run the server. 
  4) Create a new directories : ``` [REPO]/server/datasets ``` and download clothes dataset on kaggle which has about 5200 images ``` https://www.kaggle.com/datasets/agrigorev/clothing-dataset-full ```
  5) 
  6) Notice , this repo was trained by clothes dataset which has about 5200 images 
      - link to above dataset  ( 
      If you want to train with others datasets , just follow these steps below
        - Download your dataset and save them into folder -> /datasets
        - In store_vectors.py change directory into the paths to your datasets
        ![image](https://user-images.githubusercontent.com/86192249/234317334-5ff06210-6614-4cb6-80f5-3a8f10adae4b.png)
        - In this file , it has a variables , " numpic "  which is the number of image in the dataset , you can comment this line , if you want to pass all image in your dataset into the model..
         
  4) Now you run this file in your terminal : ``` python store_vectors.py ``` to extract vectors from these images .
  5) You can run the demo on browser on ``` client ``` folder .
  6) To run this demo on your browser . Please follow these steps belows:
       1) Make sure you have installed the lastest version of NodeJs .
       2) On your terminal , use ``` cd [REPO]/client ``` to change current directory to client folder , and run ``` npm run dev ``` . If the browser won't open automaitcally , please enter this link : ```http://localhost:3000```.
       3) Pick an image from your laptop and enjoy 💐💐💐💐
       
   
        
        

        
        
      
      
  
