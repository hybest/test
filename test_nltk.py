#-*- coding:utf-8 -*-

# NLTK⾃带语料库
# from nltk.corpus import brown
# print brown.categories()
# print len(brown.sents())
# print len(brown.words())


# Tokenize 分词
import nltk
sentence = "hello, world"
tokens = nltk.word_tokenize(sentence)
print tokens


from nltk.tokenize import word_tokenize
tweet = 'RT @angelababy: love you baby! :D http://ah.love #168cm'
print(word_tokenize(tweet))

# 社交网络语言的tokenize
import re
emoticons_str = r"""
(?:
[:=;] # 泊氟
[oO\-]? # .惑.
[D\)\]\(\]/\\OpP] # 糒
)"""
regex_str = [
emoticons_str,
r'<[^>]+>', # HTML tags
r'(?:@[\w_]+)', # @琘.
r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # ....
r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
# URLs
r'(?:(?:\d+,?)+(?:\.?\d+)?)', # .
r"(?:[a-z][a-z'\-_]+[a-z])", # Τ - ㎝ ˉ ..
r'(?:[\w_]+)', # ㄤ
r'(?:\S)' # ㄤ
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
def tokenize(s):
    return tokens_re.findall(s)
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
tweet = 'RT @angelababy: love you baby! :D http://ah.love #168cm'
print(preprocess(tweet))


# Stemming
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
print porter_stemmer.stem('maximum')
print porter_stemmer.stem('presumably')
print porter_stemmer.stem('multiply')
print porter_stemmer.stem('provision')

print "implete lemma..."
# NLTK实现Lemma
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
print wordnet_lemmatizer.lemmatize('dogs')
print wordnet_lemmatizer.lemmatize('churches')
print wordnet_lemmatizer.lemmatize('aardwolves')
print wordnet_lemmatizer.lemmatize('abaci')
print wordnet_lemmatizer.lemmatize('hardrock')

# NLTK更好地实现Lemma
# ⽊木有POS Tag，默认是NN 名词
print wordnet_lemmatizer.lemmatize('are')
print wordnet_lemmatizer.lemmatize('is')
# 加上POS Tag
print wordnet_lemmatizer.lemmatize('is', pos='v')
print wordnet_lemmatizer.lemmatize('are', pos='v')


# NLTK标注POS Tag
import nltk
text = nltk.word_tokenize('what does the fox say')
print text
print nltk.pos_tag(text)

