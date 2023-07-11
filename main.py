# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:58:32 2023

@author: madhu
"""

import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import pipeline, set_seed
import torch

st.write("Text Summarizer WebApp")

 

tokenizer = AutoTokenizer.from_pretrained("Madhur-01/tokenizer")

model = AutoModelForSeq2SeqLM.from_pretrained("Madhur-01/text-summarization-model")

pipe = pipeline('summarization', model = mode,tokenizer=tokenizer )

text_input = st.text_area("Input your text in English")
# Set max and min length inputs
max_length = st.number_input("Max Summary Length", min_value=10, max_value=500, value=150)
min_length = st.number_input("Min Summary Length", min_value=10, max_value=500, value=40)

# Summarize the input text on button click
if st.button("Summarize"):
    if text_input:
        # Generate summary using the pipeline with custom length settings
        summaries = pipe(text_input, max_length=max_length, min_length=min_length, do_sample=False)
        st.write("Summarized Text")
        st.write(pred[0].get("summary_text"))
