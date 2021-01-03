from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
#% matplotlib inline
import pandas as pd
from os import path
from PIL import Image
#import pillow
import numpy as np

text = open("pythonquest.txt","r").read()

wordcloud = WordCloud().generate(text)

print("Hello WordCloud")

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


