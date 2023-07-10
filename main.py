# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 14:58:32 2023

@author: madhu
"""

import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import pipeline, set_seed

st.write("Text Summarizer WebApp")


model_ckpt = "google/pegasus-cnn_dailymail"

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)

pipe = pipeline('summarization', model = model_ckpt )

text_input = st.text_area("Input your text in English")

if text_input:
    pred = pipe(text_input)
    st.write("##Summarized Text")
    st.write(" ".join(pred))