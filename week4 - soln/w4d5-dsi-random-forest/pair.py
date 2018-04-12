# You can run this script and see the results. Example output is also included
# for each question. Note that there is randomness involved (both in how the
# data is split and also in the Random Forest), so you will not always get
# exactly the same results.


from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from roc import plot_roc


# 1. Load the dataset in with pandas
df = pd.read_csv('./data/churn.csv')

# 2. Convert the "no", "yes" values to booleans (True/False)
df["Int'l Plan"] = df["Int'l Plan"] == 'yes'
df["VMail Plan"] = df["VMail Plan"] == 'yes'
df['Churn?'] = df['Churn?'] == 'True.'

# 3. Remove the features which aren't continuous or boolean
df.pop('State')
df.pop('Area Code')
df.pop('Phone')

# 4. Make a numpy array called y containing the churn values
y = df.pop('Churn?').values

# 5. Make a 2 dimensional numpy array containing the feature data (everything except the labels)
X = df.values

# 6. Use sklearn's train_test_split to split into train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 7. Use sklearn's RandomForestClassifier to build a model of your data
rf = RandomForestClassifier()
rf.fit(X_train, y_train)

# 8. What is the accuracy score on the test data?
print("\n8. score:", rf.score(X_test, y_test))
## answer: 0.9448441247

# 9. Draw a confusion matrix for the results
y_predict = rf.predict(X_test)
print("\n9. confusion matrix:")
print(confusion_matrix(y_test, y_predict))
## answer:  716   6
##           40  72

# 10. What is the precision? Recall?
print("\n10. precision:", precision_score(y_test, y_predict))
print("    recall:", recall_score(y_test, y_predict))
## precision: 0.923076923077
##    recall: 0.642857142857

# 11. Build the RandomForestClassifier again setting the out of bag parameter to be true
rf = RandomForestClassifier(n_estimators=30, oob_score=True)
rf.fit(X_train, y_train)
print("\n11: accuracy score:", rf.score(X_test, y_test))
print("    out of bag score:", rf.oob_score_)
##   accuracy score: 0.953237410072
## out of bag score: 0.946778711485   (out-of-bag error is slightly worse)

# 12. Use sklearn's model to get the feature importances
feature_importances = np.argsort(rf.feature_importances_)
print("\n12: top five:", list(df.columns[feature_importances[-1:-6:-1]]))
## top five: ['Day Mins', 'CustServ Calls', 'Day Charge', "Int'l Plan", 'Eve Mins']
## (will vary a little)

# 13. Calculate the standard deviation for feature importances across all trees

n = 10 # top 10 features

#importances = forest_fit.feature_importances_[:n]
importances = rf.feature_importances_[:n]
std = np.std([tree.feature_importances_ for tree in rf.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]
features = list(df.columns[indices])

# Print the feature ranking
print("\n13. Feature ranking:")

for f in range(n):
    print("%d. %s (%f)" % (f + 1, features[f], importances[indices[f]]))

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(10), importances[indices], yerr=std[indices], color="r", align="center")
plt.xticks(range(10), indices)
plt.xlim([-1, 10])
plt.savefig('13_Feature_ranking.png')
plt.close()
print('\nPlotted 13) feature importances')

# 14. Try modifying the number of trees
num_trees = range(5, 50, 5)
accuracies = []
for n in num_trees:
    tot = 0
    for i in range(5):
        rf = RandomForestClassifier(n_estimators=n)
        rf.fit(X_train, y_train)
        tot += rf.score(X_test, y_test)
    accuracies.append(tot / 5)
plt.plot(num_trees, accuracies)
plt.savefig('14_Accuracy_vs_num_trees.png')
plt.close()
print('\nPlotted 14) accuracy vs num_trees')
## Levels off around 20-25

# 15. Try modifying the max features parameter
num_features = range(1, len(df.columns) + 1)
accuracies = []
for n in num_features:
    tot = 0
    for i in range(5):
        rf = RandomForestClassifier(max_features=n)
        rf.fit(X_train, y_train)
        tot += rf.score(X_test, y_test)
    accuracies.append(tot / 5)
plt.plot(num_features, accuracies)
plt.savefig('15_accuracy_vs_num_features.png')
plt.close()
print('\nPlotted 15) accuracy vs num_features')
## Levels off around 5-6

# 16. Run all the other classifiers that we have learned so far in class
def get_scores(classifier, X_train, X_test, y_train, y_test, **kwargs):
    model = classifier(**kwargs)
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    return model.score(X_test, y_test), \
           precision_score(y_test, y_predict), \
           recall_score(y_test, y_predict)

print("\n16. Model, Accuracy, Precision, Recall")
print("    Random Forest:", get_scores(RandomForestClassifier, X_train, X_test, y_train, y_test, n_estimators=25, max_features=5))
print("    Logistic Regression:", get_scores(LogisticRegression, X_train, X_test, y_train, y_test))
print("    Decision Tree:", get_scores(DecisionTreeClassifier, X_train, X_test, y_train, y_test))
print("    Naive Bayes:", get_scores(MultinomialNB, X_train, X_test, y_train, y_test))
## MODEL               ACCURACY PRECISION    RECALL
## Random Forest         0.9508    0.8817    0.7321
## Logistic Regression   0.8741    0.6129    0.1696
## Decision Tree         0.9209    0.6949    0.7321

print("17. Use the included `plot_roc` function to visualize the roc curve of each model")
plot_roc(X, y, RandomForestClassifier, 'Random_Forest', n_estimators=25, max_features=5)
plot_roc(X, y, LogisticRegression, 'Logistic_Regrssion')
plot_roc(X, y, DecisionTreeClassifier, 'Decision_Tree')
#plot_roc(X, y, MultinomialNB, 'Naive_Bayes') error
print('\nPlotting completed.')
