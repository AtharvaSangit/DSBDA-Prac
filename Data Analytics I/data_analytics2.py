# -*- coding: utf-8 -*-
"""Data_Analytics2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10ymvRASBXAzv0URsBh30XDn7fE5Tkhud
"""

# Commented out IPython magic to ensure Python compatibility.
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt                      # Importing the required libraries
import seaborn as sns
# %matplotlib inline

df=pd.read_csv('/content/Social_Adv-changed - Social_Adv-changed.csv')
df
df.head()
df.columns
df.shape
df.info()
df.dtypes
df.describe()    
df.isnull().sum()
df

df.corr()  
sns.heatmap(df.corr())

#To check if the data is equally balanced between the target classes
df['Purchased'].value_counts()

#Defining features and target variable
y = df['Purchased'] #target variable we want to predict 
X = df.drop(columns = ['Purchased']) #set of required features, in this case all

from sklearn.model_selection import train_test_split
#Splitting the data into train and test set 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

#Predicting using Logistic Regression for Binary classification 
from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(X_train,y_train) #fitting the model 
y_pred = LR.predict(X_test) #prediction

#Evaluation of Model - Confusion Matrix Plot
import itertools
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

from sklearn.metrics import confusion_matrix
# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)
# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=['Age','EstimatedSalary'],
                      title='Confusion matrix, without normalization')

#extracting true_positives, false_positives, true_negatives, false_negatives
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print("True Negatives: ",tn)
print("False Positives: ",fp)
print("False Negatives: ",fn)
print("True Positives: ",tp)

#Accuracy
Accuracy = (tn+tp)*100/(tp+tn+fp+fn) 
print("Accuracy {:0.2f}%:", format(Accuracy))

#Precision 
Precision = tp/(tp+fp) 
print("Precision {:0.2f}",format(Precision))

#Recall 
Recall = tp/(tp+fn) 
print("Recall {:0.2f}",format(Recall))

#F1 Score
f1 = (2*Precision*Recall)/(Precision + Recall)
print("F1 Score {:0.2f}",format(f1))

#F-beta score calculation
def fbeta(precision, recall, beta):
    return ((1+pow(beta,2))*precision*recall)/(pow(beta,2)*precision + recall)
            
f2 = fbeta(Precision, Recall, 2)
f0_5 = fbeta(Precision, Recall, 0.5)

print("F2 {:0.2f}",format(f2))
print("\nF0.5 {:0.2f}",format(f0_5))

#Specificity 
Specificity = tn/(tn+fp)
print("Specificity {:0.2f}",format(Specificity))