import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn import datasets
from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier
from pair_solns import *


def plot_data_basic(X, y):
    """Plots a scatter plot

    Parameters
    ----------
    X : a dataset with two columns
    y : a label in {0,1}

    Returns
    -------
    None
    """
    colors = ['red' if x else 'blue' for x in y]
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111)
    ax.scatter(X[:,0], X[:,1], color=colors, alpha=0.5)
    plt.xlabel('X1')
    plt.ylabel('X2')


def plot_svm_decision(model, X, y, label_sizes, name):
    """Plots the Support Vector Classifier decision boundary over a scatter plot of data_scientist.csv

    Parameters
    ----------
    model : a SVC model as returned by SVC().fit()
    X : a dataset with two columns
    y : a label in {0,1}
    label_sizes : an array corresponding to shape of y, indicating for each point its size on plot
    name : a name for the figure (for enhanced readibility)

    Returns
    -------
    None
    """
    # get the separating hyperplane
    w = model.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(min(X[:,0]), max(X[:,0]))
    yy = a * xx - (model.intercept_[0]) / w[1]

    # plot the parallels to the separating hyperplane that pass through the
    # support vectors
    margin = 1 / np.sqrt(np.sum(model.coef_ ** 2))
    yy_down = yy + a * margin
    yy_up = yy - a * margin

    # plot the line, the points, and the nearest vectors to the plane
    colors = ['red' if x else 'blue' for x in y]
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(111)

    ax.scatter(X[:,0], X[:,1], color=colors, s=label_sizes, alpha=0.5)
    ax.plot(xx, yy, 'k-')
    ax.plot(xx, yy_down, 'k--')
    ax.plot(xx, yy_up, 'k--')

    # applying a limit on the plot to focus on the point clouds
    plt.xlim(min(X[:,0]), max(X[:,0]))
    plt.ylim(min(X[:,1]), max(X[:,1]))

    plt.title('SVM Decision Boundary %s' % name)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


def decision_boundary(clf, X, Y, name, h=.02):
    """Plots non-linear decision boundaries by plotting decision for every pixel on the plot

    Parameters
    ----------
    clf : a classification model
    X : a dataset with two columns
    y : a label in {0,1}
    label_sizes : an array corresponding to shape of y, indicating for each point its size on plot
    name : a name for the figure (for enhanced readibility)
    h : the step for pixel plotting within the figure (homogeneous to scale of attributes in X)

    Returns
    -------
    None
    """
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1, figsize=(7,7))
    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title('%s' % name)
    plt.show()


# NOTE: function used in part 1
def calc_margin(sep_model, X):
   coefs = sep_model.coef_.squeeze()
   dist = abs(sep_model.intercept_ + np.dot(X, coefs)) / np.linalg.norm(coefs)
   return dist.ravel()

# NOTE: function used in part 1
def model_cv(clf, X, y, k=5):
    #np.mean(cross_val_score(p_scaled, X1, y1, scoring='accuracy', cv=5)
    return np.mean(cross_val_score(clf, X, y, scoring='accuracy', cv=5))


# NOTE: the functions below correspond to the main processes
# you'll find a notebook version of that process under pair_solns.ipynb

# Part 1
def part1_preprocess():
    data = np.genfromtxt('data/part1_unscaled.csv', delimiter=',')
    X1 = data[:,1:3]
    y1 = data[:,3]
    X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.3)

    print("X1 varies in range: [{},{}] with mean {}".format(min(X1[:,0]), max(X1[:,0]), np.mean(X1[:,0])))
    print("X2 varies in range: [{},{}] with mean {}".format(min(X1[:,1]), max(X1[:,1]), np.mean(X1[:,1])))

    plot_data_basic(X1,y1)

    # SVC on unscaled data, embedded within a Pipeline
    svm_unscaled = SVC(kernel="linear")
    p_unscaled = Pipeline([('svc', svm_unscaled)])
    p_unscaled.fit(X1_train, y1_train)

    print 'Score for unscaled data: ', p_unscaled.score(X1_test, y1_test)
    print 'Beta coefficients for unscaled data: ', svm_unscaled.coef_

    margin_unscaled = calc_margin(svm_unscaled, X1_train)
    plot_svm_decision(svm_unscaled, X1_train, y1_train, margin_unscaled*20, '-- UNSCALED --')

    # SVC on scaled data embedded within a Pipeline
    svm_scaled = SVC(kernel="linear")
    p_scaled = Pipeline([('scaler', StandardScaler()),
                        ('svc', svm_scaled)])

    p_scaled.fit(X1_train, y1_train)
    print 'Score for scaled data: ', p_scaled.score(X1_test, y1_test)
    print 'Beta coefficients for scaled data: ', svm_scaled.coef_

    margin = calc_margin(svm_scaled, p_scaled.steps[0][1].transform(X1_train))
    plot_svm_decision(svm_scaled, p_scaled.steps[0][1].transform(X1_train), y1_train, margin*40, '-- SCALED --')

    print('Cross validated score with 5 folds (scaled pipeline): {}'
          .format(np.mean(cross_val_score(p_scaled, X1, y1, scoring='accuracy', cv=5))))
    print('Cross validated score with 5 folds (unscaled pipeline): {}'
          .format(np.mean(cross_val_score(p_unscaled, X1, y1, scoring='accuracy', cv=5))))


# Part 2
def part2_hyperparameter():
    data = np.genfromtxt('data/part2_scaled.csv', delimiter=',')

    X2 = data[:,1:3]
    y2 = data[:,3]
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.3)

    print("X1 varies in range: [{},{}] with mean {}".format(min(X2[:,0]), max(X2[:,0]), np.mean(X2[:,0])))
    print("X2 varies in range: [{},{}] with mean {}".format(min(X2[:,1]), max(X2[:,1]), np.mean(X2[:,1])))

    plot_data_basic(X2,y2)

    plot_svm_decision(SVC(kernel='linear', C=0.01).fit(X2_train, y2_train), X2_train, y2_train, 20, 'C=0.01')
    plot_svm_decision(SVC(kernel='linear', C=0.1).fit(X2_train, y2_train), X2_train, y2_train, 20, 'C=0.1')
    plot_svm_decision(SVC(kernel='linear', C=1.0).fit(X2_train, y2_train), X2_train, y2_train, 20, 'C=1.0')
    plot_svm_decision(SVC(kernel='linear', C=10.0).fit(X2_train, y2_train), X2_train, y2_train, 20, 'C=10.0')
    plot_svm_decision(SVC(kernel='linear', C=100.0).fit(X2_train, y2_train), X2_train, y2_train, 20, 'C=100.0')



# Part 3
def part3_kerneltricks():
    data = np.genfromtxt('data/part3_nonseparable.csv', delimiter=',')
    X3 = data[:,1:3]
    y3 = data[:,3]

    X3_train, X3_test, y3_train, y3_test = train_test_split(X3, y3, test_size=0.3, random_state=300)

    plot_data_basic(X3,y3)

    print 'CV score with 5 folds (linear): ', np.mean(cross_val_score(SVC(kernel='linear'), X3, y3, scoring='accuracy', cv=5))
    print 'CV score with 5 folds (rbf): ', np.mean(cross_val_score(SVC(kernel='rbf'), X3, y3, scoring='accuracy', cv=5))
    print 'CV score with 5 folds (poly): ', np.mean(cross_val_score(SVC(kernel='poly'), X3, y3, scoring='accuracy', cv=5))

    s = SVC(kernel='poly')
    s.fit(X3_train, y3_train)
    decision_boundary(s, X3, y3, 'POLY KERNEL')

    s = SVC(kernel='rbf')
    s.fit(X3_train, y3_train)
    decision_boundary(s, X3, y3, 'POLY RBF')


# Part 4
def part4_gridsearch():
    s = SVC(kernel='poly')

    C_values = np.exp(np.linspace(np.log(0.01), np.log(100), 40))
    degree_values = [1,2,3,4,5]

    g = GridSearchCV(s, {'C':C_values, 'degree':degree_values}, cv=10).fit(X3_train,y3_train)

    print 'The best params with a POLY kernel are', g.best_params_
    print 'Score with POLY kernel is: ', g.score(X3_test, y3_test)

    decision_boundary(g.best_estimator_, X3_train, y3_train, 'POLY KERNEL')

    s = SVC(kernel='rbf')

    C_values = np.exp(np.linspace(np.log(0.1), np.log(10), 40))

    g = GridSearchCV(s, {'C':C_values, 'gamma':np.linspace(0,5,20)}, cv=10).fit(X3_train,y3_train)

    print 'The best params with a RBF kernel are', g.best_params_
    print 'Score with RBF kernel is: ', g.score(X3_test, y3_test)

    decision_boundary(g.best_estimator_, X3_train, y3_train, 'RBF KERNEL')


# Part 5
def part5_unbalanced():
    dfU = pd.read_csv('data/part5_unbalanced.csv', names=['x1','x2', 'y'], index_col=0, skiprows=1)
    yU = dfU.pop('y').values
    XU = dfU.values
    XU_train, XU_test, yU_train, yU_test = train_test_split(XU, yU, test_size=0.3, random_state=300)

    unweighted = LinearSVC()

    weighted = LinearSVC(class_weight='balanced')
    params = {'C':np.linspace(.001, 3, 100)}
    do_search = lambda x: GridSearchCV(x, params, cv=3, scoring='recall').fit(XU_train, yU_train)

    unw = do_search(unweighted)
    w = do_search(weighted)

    decision_boundary(unw, XU_train, yU_train, 'UNWEIGHTED')
    decision_boundary(w, XU_train, yU_train, 'WEIGHTED')

    print 'Weighted best score: ', w.best_score_
    print 'UNweighted best score: ', unw.best_score_


# Part 6
def part6_real_world():
    dfR = pd.read_csv('data/svmguide1.csv')
    yR = dfR.pop('y').values
    XR = dfR.values
    XR_train, XR_test, yR_train, yR_test = train_test_split(XR, yR, test_size=0.3, random_state=300)

    p = Pipeline([('scale', StandardScaler()),
                      ('svm', SVC())])

    params = {'svm__kernel':['linear', 'poly', 'rbf'],
                  'svm__C':[0.1, 1, 2],
                 'svm__gamma':[0.1, 1, 2],
                  'svm__degree':[2,3]}

    r = GridSearchCV(p, params, cv=10, n_jobs=5).fit(XR_train, yR_train)

    print 'The best params for this model are ', r.best_params_
    print 'This model gives a CV score of ', r.best_score_


# Part 7
def part7_wide():
    dfW = pd.read_csv('data/golub1999.csv')
    yW = dfW.pop('class').values
    XW = dfW.values
    XW_train, XW_test, yW_train, yW_test = train_test_split(XW, yW, test_size=0.3, random_state=300)

    make_p = lambda x: Pipeline([('scale', StandardScaler()),
                                  ('model', x)])

    lg = GridSearchCV(make_p(LinearSVC()),
                          {'model__C':[0.01, 0.1, 1.0, 10.0]}).fit(XW_train, yW_train)
    print 'The best params for this model are ', lg.best_params_
    print 'This model gives a CV score of ', lg.best_score_
    print '---------------------------'

    rg = GridSearchCV(make_p(SVC(kernel='rbf')),
                          {'model__C':[0.01, 0.1, 1.0, 10.0],
                          'model__gamma':[0.01, 0.1, 1.0, 10.0]}).fit(XW_train, yW_train)
    print 'The best params for this model are ', rg.best_params_
    print 'This model gives a CV score of ', rg.best_score_
    print '---------------------------'


# Part 7
def part7_tall():
    dfT = pd.read_csv('data/part7_tall.csv')
    yT = dfT.pop('class').values
    XT = dfT.iloc[:,0:-2]
    XT_train, XT_test, yT_train, yT_test = train_test_split(XT, yT, train_size=20000, test_size=10000)

    make_p = lambda x: Pipeline([('scale', StandardScaler()),
                  ('model', x)])

    lg = GridSearchCV(make_p(LinearSVC()),
                          {'model__C':np.linspace(.001, 1, 10)}).fit(XT_train, yT_train)
    print 'The best params for this model are ', lg.best_params_
    print 'This model gives a CV score of ', lg.best_score_
    print '---------------------------'

    rg = GridSearchCV(make_p(SVC(kernel='rbf')),
                          {'model__C':np.linspace(.001,1,3),
                           'model__gamma':(.01, 3, 3)}).fit(XT_train, yT_train)
    print 'The best params for this model are ', rg.best_params_
    print 'This model gives a CV score of ', rg.best_score_
    print '---------------------------'


# Part 8
def part8_multi_class():
    digits = datasets.load_digits()
    Xdigits = digits.data
    ydigits = digits.target
    Xdigits_train, Xdigits_test, ydigits_train, ydigits_test = \
        train_test_split(Xdigits, ydigits, test_size=0.3, random_state=300)

    svm = GridSearchCV(LinearSVC(), {'C':[0.01, 0.1, 1.0, 10.0]}, cv=10)

    svm_ovo = OneVsOneClassifier(svm).fit(Xdigits_train, ydigits_train)
    svm_ovr = OneVsRestClassifier(svm).fit(Xdigits_train, ydigits_train)

    logit = GridSearchCV(LogisticRegression(), {'C':[0.01, 0.1, 1.0, 10.0]}, cv=10)

    log_ovo = OneVsOneClassifier(logit).fit(Xdigits_train, ydigits_train)
    log_ovr = OneVsRestClassifier(logit).fit(Xdigits_train, ydigits_train)

    ydigits_pred = svm_ovo.predict(Xdigits_test)
    print("svm_ovo accuracy: {}".format(accuracy_score(ydigits_test, ydigits_pred)))

    ydigits_pred = log_ovo.predict(Xdigits_test)
    print("log_ovo accuracy: {}".format(accuracy_score(ydigits_test, ydigits_pred)))

    ydigits_pred = svm_ovr.predict(Xdigits_test)
    print("svm_ovr accuracy: {}".format(accuracy_score(ydigits_test, ydigits_pred)))

    ydigits_pred = log_ovr.predict(Xdigits_test)
    print("log_ovr accuracy: {}".format(accuracy_score(ydigits_test, ydigits_pred)))


# NOTE: you'll find a notebook version of that process under pair_solns.ipynb
if __name__ == '__main__':
    # Part 1
    part1_preprocess()

    # Part 2
    part2_hyperparameter()

    # Part 3
    part3_kerneltricks()

    # Part 4
    part4_gridsearch()

    # Part 5
    part5_unbalanced()

    # Part 6
    part6_real_world()

    # Part 7
    part7_wide()
    part7_tall()

    # Part 8
    part8_multi_class()
