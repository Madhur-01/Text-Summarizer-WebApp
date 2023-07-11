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

model_pegasus = AutoModelForSeq2SeqLM.from_pretrained("Madhur-01/text-summarization-model")

pipe = pipeline('summarization', model = "Madhur-01/text-summarization-model" )

text_input = st.text_area("Input your text in English")


if st.button("Summarize"):
    if text_input:
        pred = pipe(text_input)
        st.write("Summarized Text")
        st.write(pred[0].get("summary_text"))
