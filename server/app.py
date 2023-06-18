import os
import io
from flask import Flask,request
from PIL import Image
from search_image import get_extract_model,extract_vector
import pickle
from pathlib import Path
import numpy as np
import math
import matplotlib.pyplot as plt
script_location = Path(__file__).absolute().parent

app = Flask(__name__)

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   image_file = request.files['image']
   image = Image.open(image_file)
   # file_location = script_location / 'vectors.pkl'
   # file = file_location.open()
   model = get_extract_model()
   search_vector = extract_vector(model, image_file)  
   vectors = pickle.load(open("vectors.pkl","rb"))
   paths = pickle.load(open("paths.pkl","rb"))
   distance = np.linalg.norm(vectors - search_vector, axis=1)
   K = 16
   ids = np.argsort(distance)[:K]
   nearest_image = [(paths[id], distance[id]) for id in ids]
   # axes = []
   grid_size = int(math.sqrt(K))
   fig = plt.figure(figsize=(10,5))
   print(nearest_image)
   axes = []
   for id in range(K):
      draw_image = nearest_image[id]
      axes.append(fig.add_subplot(grid_size, grid_size, id+1))
      
      axes[-1].set_title(draw_image[1])
      plt.imshow(Image.open(draw_image[0]))

   fig.tight_layout()
   plt.show()

    # Example: Resize the image
   resized_image = image.resize((800, 600))
   
    # Example: Save the processed image
   resized_image.save('output.jpg')
    
   return {'message': 'Image processed and saved.'}

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()