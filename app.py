import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def transform_text(text):
    text = text.lower()                # Lower Case
    text = nltk.word_tokenize(text)    # Tokenization
    y = []                             # Removing Special Character
    for i in text:
        if i.isalnum():
            y.append(i) 
            
    text = y[:]
    y.clear()
    
    for i in text:                                                                 # Removing Stop words and punctuation
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)           
    text = y[:]
    y.clear()
    for i in text:                    # Stemming
        y.append(ps.stem(i))
    
    return ' '.join(y)
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
st.title("Email/Sms Spam Classifier")
input_sms = st.text_area("Enter the message")
if st.button('Predict'):
    #1. Preprocess
    transformed_sms = transform_text(input_sms)
    #2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    #3. predict
    result = model.predict(vector_input)[0]
    #4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
    



