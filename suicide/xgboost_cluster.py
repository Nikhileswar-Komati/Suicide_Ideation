import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import xgboost
from xgboost import XGBClassifier
from joblib import dump

data = pd.read_csv('Cleaned_Depression_Vs_Suicide.csv', lineterminator = '\n')
X = data.iloc[:, 0].values
y = data.iloc[:, 1].values

le = LabelEncoder()

y = le.fit_transform(y)

train_X, test_X, train_y, test_y = train_test_split(X, y, train_size = 0.9)
print(train_X.shape, test_y.shape)



clf = Pipeline([('cv', CountVectorizer()), ('xgb', XGBClassifier())])

clf.fit(train_X, train_y)
print("------------Training Done ----------")
predictions = clf.predict(test_X)

import numpy as np
test_acc_sklearn = np.sum(predictions == test_y) / float(len(test_y)) 


print ("Test Set Examples: ", len(test_y)) 
print ("Test Set Accuracy: ", test_acc_sklearn * 100, "%")



# dump the pipeline model
dump(clf, filename = "suicide.joblib")
