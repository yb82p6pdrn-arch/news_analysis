import pandas as pd
import jieba
from collections import Counter
import matplotlib.pyplot as plt

# 1. 读取数据
df = pd.read_csv("data.csv")

# 2. 拼接文本
text = "".join(df['content'].astype(str))

# 3. 分词
words = jieba.lcut(text)

# 4. 读取停用词
with open("stopwords.txt", encoding="utf-8") as f:
    stopwords = set(f.read().splitlines())

# 5. 过滤
words = [w for w in words if w not in stopwords and len(w) > 1]

# 6. 统计
word_count = Counter(words)

# 7. 取前10
top_words = word_count.most_common(10)

words = [w[0] for w in top_words]
counts = [w[1] for w in top_words]

# 8. 画图
plt.bar(words, counts)
plt.title("关键词统计")
plt.xticks(rotation=45)
plt.show()