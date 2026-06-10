import os
import streamlit as st
import base64

from openai import OpenAI

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

st.title('🎁 제품 홍보 포스터 생성기')
keyword = st.text_input("키워드를 입력하세요.")

if st.button('생성하기🔥'):
    with st.spinner('생성 중🔥'):
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions="입력 받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 작성해줘.",
            input=keyword,
        )
        
        result = response.output_text
        
        get_images = client.images.generate(
            model="gpt-image-2",
            prompt=result
        )

    image_base64 = get_images.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    st.write(result)
    st.image(image_bytes)
