import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from joblib import dump

print("All packages imported successfully")

data = pd.read_csv('Cleaned_Depression_Vs_Suicide.csv', lineterminator = '\n')
print("Data loaded successfully")
X = data.iloc[:, 0].values
y = data.iloc[:, 1].values
le = LabelEncoder()
y = le.fit_transform(y)

train_X, test_X, train_y, test_y = train_test_split(X, y, train_size = 0.9)
print("Training X shape", train_X.shape, "Testing Y shape", test_y.shape)

clf = Pipeline([('cv', CountVectorizer()), ('xgb', XGBClassifier())])

clf.fit(train_X, train_y)
print("------------Training Done ----------")

predictions = clf.predict(test_X)
acc = accuracy_score(predictions, test_y)
print ("Test Set Accuracy: ", acc * 100, "%")



# dump the pipeline model
dump(clf, filename = "suicide.joblib")
print("Successfully completed --- joblib file created")