from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = open("pythonquest.txt", "r").read()

wordcloud = WordCloud().generate(text)

print("Hello WordCloud")

plt.imshow(wordcloud) #, interpolation='bilinear')
plt.axis("off")
plt.show()
