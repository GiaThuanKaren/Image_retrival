import os
import io
from flask import Flask,request,Response,send_from_directory
from flask_cors import cross_origin,CORS
from PIL import Image
from search_image import get_extract_model,extract_vector
import pickle
from pathlib import Path
import numpy as np
import math
import matplotlib.pyplot as plt
from flask import jsonify,json
script_location = Path(__file__).absolute().parent

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})

@app.route('/images/<path:filename>')
def serve_image(filename):
    # Specify the directory where your images are located
    directory = 'datasets/images_original'
   #  "./datasets/images_original\\708af227-43ba-4e2b-b35b-652a13cd1c77.jpg"
    # Use the send_from_directory function to serve the image
    return send_from_directory(directory, filename)

@cross_origin
@app.route('/upload', methods = ['GET', 'POST'])

def upload_file():
   image_file = request.files['image']
   image = Image.open(image_file)
   # image.show();
   file_location = script_location / 'vectors.pkl'
   file = file_location.open()
   model = get_extract_model()
   search_vector = extract_vector(model, image_file)  
   vectors = pickle.load(open("vectors.pkl","rb"))
   paths = pickle.load(open("paths.pkl","rb"))
   distance = np.linalg.norm(vectors - search_vector, axis=1)
   K = 16
   ids = np.argsort(distance)[:K]
   nearest_image = [(paths[id], distance[id]) for id in ids]
   axes = []
   grid_size = int(math.sqrt(K))
   fig = plt.figure(figsize=(10,5))
   

   for id in range(K):
       draw_image = nearest_image[id]
       axes.append(fig.add_subplot(grid_size, grid_size, id+1))
      
       axes[-1].set_title(draw_image[1])
       plt.imshow(Image.open(draw_image[0]))

   fig.tight_layout()
   # plt.show()

   serialized_list = [(path, float(value)) for path, value in nearest_image]
   return jsonify(serialized_list)

if __name__ == "__main__":
    app.config['DEBUG'] = True
    app.run()