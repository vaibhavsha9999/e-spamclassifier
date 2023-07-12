# Email/SMS Spamclassifier

This project aims to build a spam detection model using machine learning techniques and data used in this project looks like - ![Screenshot (52)](https://github.com/vaibhavsha9999/e-spamclassifier/assets/92802512/fe83a0b9-61d6-4031-bdd3-2c25dd9a56e9)

# Project Structure
The project is structured as follows:

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Text Preprocessing
4. Model Building
5. Evaluation
6. Improvement
7. Website
8. Deployment
   
1. Data Cleaning
In this step, we analyze the dataset, handle missing values, and remove unnecessary columns.

2. Exploratory Data Analysis (EDA)
EDA is performed to gain insights into the dataset. The target variable distribution is examined, and visualizations such as pie charts and histograms are created to understand the data.

3. Text Preprocessing
Text preprocessing is crucial to prepare the text data for modeling. The following steps are performed:

- Lowercasing the text
- Tokenization
- Removing special characters
- Removing stop words and punctuation
- Stemming

4. Model Building
Multiple classification models are trained and evaluated to determine the most effective algorithm for spam detection. The models used include Gaussian Naive Bayes, Multinomial Naive Bayes, and Bernoulli Naive Bayes.

5. Evaluation
The performance of each trained model is evaluated using metrics such as accuracy, precision, and confusion matrix. The Multinomial Naive Bayes model with TF-IDF vectorization is selected as the best performing model.

6. Improvement
Further improvements and optimizations can be made to enhance the model's performance, such as fine-tuning hyperparameters or exploring different feature engineering techniques.

7. Website
The project includes a web interface where users can input text messages and receive predictions on whether the message is spam or not. The website provides a user-friendly interface for real-time spam detection.

8. Deployment
The final model is deployed, and the website is hosted to make it accessible to users. The deployed model and vectorizer are saved as pickle files for future use.
