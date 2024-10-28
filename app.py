from flask import Flask, render_template, request, redirect, url_for
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load model and vectorizer
model = LogisticRegression()
feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)

# Load and train model with dataset
raw_mail_data = pd.read_csv('mail_data (1).csv')
mail_data = raw_mail_data.fillna('')
mail_data['Category'] = mail_data['Category'].map({'spam': 0, 'ham': 1})

X = mail_data['Message']
Y = mail_data['Category']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)
X_train_features = feature_extraction.fit_transform(X_train)
model.fit(X_train_features, Y_train)

# Route to the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to the landing page after login
@app.route('/land')
def land():
    return render_template('land.html')

# Redirect after login form submission to the landing page
@app.route('/login', methods=['POST'])
def handle_login():
    # Optional: Add login credential checks here
    return redirect(url_for('land'))

# Route for prediction on the index page
@app.route('/predict', methods=['POST'])
def predict():
    input_mail = [request.form['message']]
    input_data_features = feature_extraction.transform(input_mail)
    prediction = model.predict(input_data_features)
    
    return render_template('index.html', prediction=prediction[0])

# Route to display index.html directly
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
