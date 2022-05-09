import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image


#######################

import json
import urllib.parse
import urllib.request
import requests
##公開URLへ変更
url = "http://0be0-104-199-160-154.ngrok.io"


##戻り値例 shapeの前が比較値
##{'class_id': 'tf.Tensor(758865800.0, shape=(), dtype=float32)', 'class_name': 'interlab_style2'}



#####################

#image = Image.open('cat.jpg')

#st.image(image, caption='Sunrise by the mountains')

import streamlit as st
#import matplotlib.pyplot as plt
from PIL import Image
import json
import urllib.parse
import urllib.request
import requests


st.set_option("deprecation.showfileUploaderEncoding", True)

st.sidebar.title("画像比較")
st.sidebar.write("スタイルとコンテンツの類似度を出力")

st.sidebar.write("")

images = {}

img_file = st.sidebar.file_uploader("対象画像Aを選択して", type=["jpg"])

img_file2 = st.sidebar.file_uploader("対象画像Bを選択して", type=["jpg"],key="1")

if img_file is not None:
    if img_file2 is not None:
        with st.spinner("推定中..."):
            img = Image.open(img_file)
            st.image(img, caption="対象Aの画像", width=480)
            st.write("")
            from io import BytesIO
            buf = BytesIO()
            img.save(buf, 'jpeg')
            buf.seek(0)
            images[str(0)] = buf.read()
            buf.close()

            img = Image.open(img_file2)
            st.image(img, caption="対象Bの画像", width=480)
            st.write("")
            from io import BytesIO
            buf = BytesIO()
            img.save(buf, 'jpeg')
            buf.seek(0)
            images[str(1)] = buf.read()               
            buf.close()


            
            ##スタイル比較値API（2枚で比較）
            #res = requests.post(url+"/style2", files=images)

            res = requests.post(url+"/content2", files=images)
            #print(res.json())

            #reqbody = images
            #print(res.json())
            st.sidebar.write(res.json())
            
            res = requests.post(url+"/style2", files=images)
            #print(res.json())

            #reqbody = images
            #print(res.json())
            st.sidebar.write(res.json())




