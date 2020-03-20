print("\t\t\tAssignment\n\t\t\tShubhangi Goyal\n\t\t\tRoll No.: 17/1430\n\n")

# Reading data from CSV
# Removing unnecessary columns
# Renaming column-names to something meaningful
import pandas as pd
data = pd.read_csv("../input/spam.csv",encoding = "latin")
data = data.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1)
data = data.rename(columns = {'v1':'Spam/Ham','v2':'message'})
data.head()

# Preprocessing
# Removing punctuation and stop words
import string
import nltk
from nltk.corpus import stopwords
def text_preprocess(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    return " ".join(text)

data_2 = data['message'].copy()
data_2 = data_2.apply(text_preprocess)

# Vectorizing the data
# Collecting each word and its frequency in each email.
# The vectorization will produce a matrix.
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer("english")
data_matrix = vectorizer.fit_transform(data_2)

# Test/Train Split
# Dividing data into test-train sets, 25% and 75%
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(data_matrix, data['Spam/Ham'], test_size=0.25)

# Logistic Regression
# Fit the model according to "data" variable obtained from CSV.
from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression()
logistic.fit(X_train, Y_train)

# Checking accuracy score metrics
predictions = logistic.predict(X_test)

# Accuracy score metrics
from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test, predictions)
print("Accuracy score : ",acc,"\nAccuracy %ge = ",acc*100,"%")

# Scatter Plot
import matplotlib.pyplot as plt
plt.scatter(Y_test, predictions)
plt.xlabel("True Values",color='red')
plt.ylabel("Predictions",color='blue')
plt.title("Predicted vs Actual value")
plt.grid(True)
plt.show()
