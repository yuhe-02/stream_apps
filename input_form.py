import streamlit as st
import time
import os

# 環境変数の設定設定
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = '自身のAPIキーを追加'


import io
import os
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


# APIインタフェースの準備
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], 
    verbose=True,
)

#title
st.title('画像生成アプリ')

#input words
keywords = st.text_input("キーワード")
print(keywords)

#button
submit_btn = st.button("request")
cancel_btn = st.button("cancel")
print(f'submit_btn:{submit_btn}')
print(f'cancel_btn:{cancel_btn}')

if keywords == "" and submit_btn :
    st.info(f'入力がありません。文字を入力してください')

elif keywords == "":
    st.info(f'入力してください')
    


if submit_btn and keywords != "" :
    st.text(f'"{keywords}"の内容で画像を生成します')
    with st.spinner():
        time.sleep(5)
    
    st.success("success!!")
    answers = stability_api.generate(
    prompt=keywords,)

# 結果の出力
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                print("NSFW")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                st.image(img, caption=keywords,use_column_width=True)