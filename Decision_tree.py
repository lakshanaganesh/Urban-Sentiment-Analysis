#import libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, train_test_split, ShuffleSplit,cross_val_score
from sklearn.metrics import classification_report


#reading input files
df = pd.read_csv('data_train_clean_scores.csv')
y = df['sentiment'].values
X = df.drop(columns=['sentiment','text'])

#spilting test and train datasets
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.25, random_state=84)

#classifier-> decision tree
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

#report
y_true, y_pred = y_test , clf.predict(X_test)
print('Results on the test set:')
print(classification_report(y_true, y_pred))

#cv score
cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=20)
print(np.mean(cross_val_score(clf, X, y, cv=cv)  ))