#Major Project
#Web Application
This web application consists of several HTML pages, CSS styles, and images. Below is an overview of the project structure and how to set up the application.

Project Structure
land.html: Landing page for the application.
login.html: Login page where users can sign in.
index.html: Main page of the application.
style.css: Stylesheet to style the pages.
bg.jpg: Background image used in the application.
bg.png: Additional background image option.
Getting Started
Prerequisites
To run this project, you need a web browser. No additional installation is required.

Running the Application
Clone or download this repository.
Open index.html in a web browser to access the main page.
You can navigate between land.html and login.html using links provided within the pages (if implemented).
File Descriptions
land.html: The starting page with basic information and links to other parts of the application.
login.html: A login form where users enter their credentials to access restricted sections of the application.
index.html: The core page users see after logging in.
style.css: Contains the styles for various elements on each page.
Sets background images, adjusts padding, and defines responsive behaviors.
Custom animations and font styles are also configured for an enhanced user experience.
bg.jpg and bg.png: Background images referenced in style.css for a visually engaging interface.
CSS Highlights
The stylesheet style.css customizes the layout and appearance:

Sets responsive behavior for various screen sizes.
Includes animations for headings, color transitions, and media query adjustments for mobile views.
Notes
Ensure all files are in the same directory for proper linking.
Customize images or styles in style.css as needed.
Machine Learning for Spam Message and Call Detection using MLP and Logistic Regression
Introduction
Spam message detection and call checks are crucial for improving user experience and protecting against unwanted communication in modern digital systems. Machine learning (ML) can be leveraged to automate the identification of spam messages and phone calls by classifying incoming data into two categories: spam and non-spam (ham), or legitimate calls and fraudulent ones.

Two common ML models used for these tasks are:

Multi-Layer Perceptron (MLP): A type of neural network that works well for learning complex patterns in data.
Logistic Regression: A simpler but effective linear model that is widely used for binary classification tasks.
Data Collection and Preprocessing
Before applying MLP or Logistic Regression, it's necessary to gather data and preprocess it:

Spam Message Dataset: This might consist of text messages labeled as 'spam' or 'ham'. Features could include the text content (e.g., length of message, presence of specific words or phrases, etc.).
Call Dataset: This might include records of phone calls, labeled as 'spam' or 'ham'. Features could involve call duration, origin of the call (e.g., known spam number), or other patterns from past calls.
Preprocessing Steps:
Text Cleaning: Removing punctuation, numbers, and stop words.
Tokenization: Converting text into tokens (words or characters).
Vectorization: Converting textual data into numeric form (e.g., using TF-IDF or word embeddings).
Feature Engineering: Creating new features such as message length, frequency of certain keywords, etc.
Normalization: Scaling features to ensure the model performs optimally.
Model 1: Multi-Layer Perceptron (MLP)
MLP is a type of artificial neural network that can model complex relationships between inputs and outputs. In the case of spam message or call classification, the model would typically consist of an input layer, one or more hidden layers, and an output layer.

Input Layer: Takes in the features (such as message content, phone number history, etc.).
Hidden Layers: Perform computations based on learned weights and activation functions (such as ReLU).
Output Layer: Outputs a binary classification result (spam or ham).
Steps for Training MLP:
Initialization: Set up the architecture with an appropriate number of neurons in hidden layers.
Training: Use the backpropagation algorithm to minimize the loss function (commonly cross-entropy) and update weights based on gradients.
Evaluation: Evaluate the model on test data using metrics like accuracy, precision, recall, and F1-score.
Strengths of MLP:
Capable of handling highly non-linear data relationships.
Can adapt and learn from large, complex datasets.
Challenges:
Requires a large amount of data to perform well.
More computationally expensive compared to simpler models like logistic regression.
Model 2: Logistic Regression
Logistic Regression is a simpler, probabilistic model used for binary classification tasks. Despite its simplicity, it is highly effective, especially for linearly separable data.

In the context of spam message detection or call checks:

The input features could be the presence or absence of specific words or characteristics of the message/call.
The output would be a probability of the message being spam or the call being fraudulent.
Steps for Training Logistic Regression:

Training: Use an optimization algorithm (such as Gradient Descent) to minimize the logistic loss function.
Evaluation: Measure the model’s performance using accuracy, precision, recall, and AUC (Area Under Curve).
Strengths of Logistic Regression:
Simple and computationally efficient.
Works well for linearly separable data.
Easy to interpret model parameters.
Challenges:
Not ideal for highly non-linear relationships.
May underperform with complex patterns, especially in text-based data.

### Author
Developed by [Pratham Pathak].

