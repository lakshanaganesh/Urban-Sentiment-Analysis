#import libraries
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV, train_test_split, ShuffleSplit,cross_val_score

#reading input files
df = pd.read_csv('data_train_clean_scores.csv')
y = df['sentiment'].values
X = df.drop(columns=['sentiment','text'])


#spilting test and train datasets
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=20)

#classifier-> MLP
mlp = MLPClassifier(max_iter=2000,hidden_layer_sizes=(660,200,6),activation='tanh')


#Grid search
parameter_space = {
    'hidden_layer_sizes': [(660,100,3),(660,300,10),(660,200,6)],
    'activation': ['tanh', 'relu']
}
clf = GridSearchCV(mlp, parameter_space, n_jobs=-1, cv=4)

# Best parameter set
print('Best parameters found:\n', clf.best_params_)

clf = MLPClassifier(max_iter=2000,hidden_layer_sizes=(660,200,6),activation='tanh')
clf.fit(X_train, y_train)

# All results
means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
	print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))



y_true, y_pred = y_test , clf.predict(X_test)

from sklearn.metrics import classification_report

print('Results on the test set:')
print(classification_report(y_true, y_pred))

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=20)
print(np.mean(cross_val_score(clf, X, y, cv=cv)  ))