from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request
import torch
from tqdm import tqdm
import os 
from datetime import datetime

MODEL_PATH = "D:\\Long\\teiki\\sentiment_analysis\\cardiffnlp\\twitter-roberta-base-sentiment"
labels = ['negative', 'neutral', 'positive']
# result = {
#     "negative" : "",
#     "neutral" : "",
#     "positive" : ""
# }
class SentimentAnalysis:
    def __init__(self):
        self.model_path = MODEL_PATH
        self.loadModel()
        for i in range(10):
            self.inference(" i love you")

    def loadModel(self) :
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path)
        
    def inference(self, input_text) :
        encoded_input = self.tokenizer(input_text, return_tensors='pt')
        output = self.model(**encoded_input)

        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        max_score = np.amax(scores)
        for i in range(scores.shape[0]):
            if scores[ranking[i]] == max_score:
                max_index = ranking[i]
            
        if max_index == 0:
            result = {"negative" : str(max_score) }
        if max_index == 1:
            result = {"neutral" : str(max_score) }
        if max_index == 2:
            result = {"positive" : str(max_score) }
        # import ipdb; ipdb.set_trace()
        return result

    def convertToDerisedOutput(self, labels, scores, ranking):
        
        for i in range(3):
            if ranking[i] == 0:
                negative_ = scores[ranking[i]]
            if ranking[i] == 1:
                neutral_ = scores[ranking[i]]
            if ranking[i] == 2:
                positive_ = scores[ranking[i]]
        return negative_, neutral_, positive_

