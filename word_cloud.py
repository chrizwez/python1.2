







frequencies = {"Hand": 5, "Motor": 10}





cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")