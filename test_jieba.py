#! -*- coding:utf-8 -*-
import jieba


seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print "Full Mode:", "/ ".join(seg_list)  # 全模式
seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print "Default Mode:", "/ ".join(seg_list)  # 精确模式
seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print ", ".join(seg_list)
seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造", cut_all=True)
print "Full Mode:", "/ ".join(seg_list)  # 全模式
seg_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 默认是精确模式
print ", ".join(seg_list)
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print ", ".join(seg_list)

# 使用自定义词典
test_sent = "李小福是创新办主任也是云计算方面的专家;"
test_sent += "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类型"
words = jieba.cut(test_sent)
for w in words:
    print w

jieba.load_userdict("selfdefine.txt")
import jieba.posseg as pseg

test_sent = "李小福是创新办主任也是云计算方面的专家;"
test_sent += "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类型"
words = jieba.cut(test_sent)
print "$$$$$$$$$$$$$$加入自定义词典后: "
for w in words:
    print w

print "\n================================="
result = pseg.cut(test_sent)
for w in result:
    print w.word, "/", w.flag, ", ",

# 关键词抽取
print "\n关键词抽取.............................."
import jieba.analyse
file_name = "news.txt"

topK = 10
content = open(file_name, 'rb').read()
tags = jieba.analyse.extract_tags(content, topK=topK)
print ",".join(tags)


# 词性标注
print "\n词性标注.............................."
words = pseg.cut("我爱北京天安门")
for w in words:
    print w.word, w.flag



