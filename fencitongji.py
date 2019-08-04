
"""
本文用于统计文章中的频率较高的词，并且对一些无意义的词作了过滤
Based on Python3.6
"""

import sys
import pkuseg
from collections import Counter
import pprint
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from imageio import imread


YANJIANGFILE = 'yanjiang.txt'
STOPWORDFILE = 'stopword.txt'
MASKFILE = 'wechat_logo.jpg'
SAVEIMGFILE = 'ciyun.jpg'

# 加载待统计文章
content = []
with open(YANJIANGFILE, encoding='utf-8') as f:
    content = f.read()


# 加载过滤词
stopwords = []
with open(STOPWORDFILE, encoding='utf-8') as f:
    stopwords = f.read()

reserved_words = ['朋友圈', '小程序', '公众号']


# 执行分词 
seg = pkuseg.pkuseg(user_dict=reserved_words)
text = seg.cut(content)

new_text = []
for word in text:
    if word not in stopwords:
        new_text.append(word)

counter = Counter(new_text)
pprint.pprint(counter.most_common(50))

# 绘图
font_path = '/System/Library/fonts/PingFang.ttc'
mask = imread(MASKFILE)
img_color = ImageColorGenerator(mask)
other_stopwords = ['这是']

wordcloud = WordCloud(
    font_path = font_path,
    margin = 2, # 设置页面边缘
    mask = mask,
    scale = 2,
    max_words = 200, # 最多词个数
    min_font_size = 4, # 最小字体大小
    random_state = 42,
    background_color = 'white', # 背景颜色
    max_font_size = 150, # 最大字体大小
)
wordcloud.generate_from_frequencies(counter)
wordcloud.recolor(color_func=img_color)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
#plt.show()
plt.savefig(SAVEIMGFILE)
