import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from peft import PeftModel
import torch

st.set_page_config(page_title="AI Dịch Thuật Anh - Việt")
st.title("Ứng dụng Dịch Anh - Việt (Sử dụng LoRA)")

@st.cache_resource
def load_model():
    model_checkpoint = "Helsinki-NLP/opus-mt-en-vi"
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    
    base_model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
    model = PeftModel.from_pretrained(base_model, "./my-lora-adapter")
    
    return tokenizer, model

with st.spinner('Đang tải...'):
    tokenizer, model = load_model()

text_input = st.text_area("Nhập văn bản tiếng Anh:", height=150, placeholder="Ví dụ: Machine learning is fascinating.")

if st.button("Dịch thuật", type="primary"):
    if text_input.strip() == "":
        st.warning("Vui lòng nhập văn bản.")
    else:
        inputs = tokenizer(text_input, return_tensors="pt")
        
        with st.spinner('AI đang dịch...'):
            outputs = model.generate(**inputs, max_length=128)
            translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
        st.success("Kết quả: ")
        st.write(translation)