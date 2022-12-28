import nltk
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')
with open("/content/drive/MyDrive/savetags.savtag","rb") as f:
  tagger = pickle.load(f)
tagger.get_tags(tagger.get_cluster("sort moi les doigts du fiak stp"))
