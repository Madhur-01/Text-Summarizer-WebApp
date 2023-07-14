# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:58:32 2023

@author: madhu
"""

import streamlit as st
from transformers import  AutoTokenizer
from transformers import pipeline
import torch
import fitz

st.write("Text Summarizer WebApp")


model_ckpt = "t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)


pipe = pipeline('summarization', model = model_ckpt, tokenizer=tokenizer)

text_input = st.text_area("Input your text in English")

pdf_file = st.file_uploader("Upload a PDF file", type="pdf")

if st.button("Summarize"):
    if text_input:
        pred = pipe(text_input)
        summarized_text = pred[0]["summary_text"]
        st.write("Summarized Text:")
        st.write(summarized_text)
    elif pdf_file is not None:
        pdf_data = pdf_file.read()
        doc = fitz.open(stream=pdf_data, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        pred = pipe(text)
        summarized_text = pred[0]["summary_text"]
        st.write("Summarized Text:")
        st.write(summarized_text)
