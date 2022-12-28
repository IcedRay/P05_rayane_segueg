from sklearn.cluster import MiniBatchKMeans
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from io import StringIO
from html.parser import HTMLParser
import re
from joblib import dump, load
import umap

class MLStripper(HTMLParser):
  def __init__(self):
    super().__init__()
    self.reset()
    self.strict = False
    self.convert_charrefs= True
    self.text = StringIO()
  def handle_data(self, d):
    self.text.write(d)
  def get_data(self):
    return self.text.getvalue()

def strip_tags(html):
  noescape = re.sub('\n',' ',html)
  nocode = re.sub('<code*?.*?/code>','',noescape)# on retire le code
  explicit1 = re.sub('<pre class="lang-',' ',nocode)# on garde le tag de language
  explicit2 = re.sub('prettyprint-override">','',explicit1)# on garde le tag de language
  explicit3 = re.sub('</pre>','',explicit2)
  s = MLStripper()
  s.feed(explicit3)
  return s.get_data()

def preprocess(sentence):
  stemmer = WordNetLemmatizer()
  nopunc = [char for char in sentence if char not in string.punctuation]
  nopunc_nodigit = ''.join([i for i in nopunc if not i.isdigit()])
  stopworded = [word.lower() for word in nopunc_nodigit.split() if word not in stopwords.words('english')]
  return [stemmer.lemmatize(word) for word in stopworded]

def clean(txt):
  return " ".join(preprocess(strip_tags(txt)))

class Tagger:
  def __init__(self,avg,tag,mod,vec):
    self.average = avg
    self.tags = tag
    self.model = mod
    self.vectorizer = vec
    self.reducer = reducer
  def get_tags(self,i):
    return  [key for key,value in self.tags[i][:5]]
  def get_cluster(self,txt):
    buff = self.vectorizer.transform([clean(txt)])
    buff2 = self.reducer.transform(buff)
    return self.model.predict(buff2)[0]
tagger = load('savetags.joblib')
print("oui")
print(tagger.get_tags(tagger.get_cluster("data doesn't work , how do i make data work in sql please ")))
