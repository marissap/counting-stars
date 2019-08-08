import os
import json
import urllib
import requests
from datetime import datetime

from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

url = "https://api.nasa.gov/planetary/apod?api_key=NZcTgk6A0Z9LROxcyFPlFICzr7V9oa7mEIkU9j7a"

r = requests.get(url)

if r:
    img_data = json.loads(r.text)
    img_url = img_data['url']
    img_hd_url = img_data['hdurl']
    img_name = datetime.today().strftime('%y%m%d%H%M%S') + '.jpg'  
    print(img_name)
    img_name = img_name.replace(" ", "")  
    file_path = os.environ['HOME'] + '/Projects/nasa/img/' + img_name
    if (os.path.exists(file_path)) is False:
        try:
            urllib.request.urlretrieve(img_hd_url, filename=file_path)
            img_desc = img_hd_url
        except urllib.error.HTTPError:
            urllib.request.urlretrieve(img_url, filename=file_path)
            img_desc = img_url
        
        # file = glob.glob(file_path[1:])[0]
        # im = imread(file, as_grey=True)
        # plt.imshow(im, cmap='gray')
        # plt.show()