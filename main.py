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


model_ckpt = "t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_ckpt)

model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(model_ckpt)

pipe = pipeline('summarization', model = model_ckpt )

text_input = st.text_area("Input your text in English")

if st.button("Summarize"):
    if text_input:
        inputs = tokenizer.encode(text_input, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(inputs, max_length=150, min_length=40, num_beams=4)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        st.write("## Summarized Text")
        st.write(summary)
