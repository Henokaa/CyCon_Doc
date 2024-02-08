KNN
=====

.. _installation:

Introduction
------------
This file is a comparative analysis on Cycon’s ability to perform KNN classification. This serves as proof that the Cycon page is able to perform KNN. 
The following shows KNN results for various datasets.

.. note::
   * Name: Iris CSV
   * Path: Tests/sampleCSV_MLA_Classification/iris.csv
   * Kaggle: https://www.kaggle.com/code/skalskip/iris-data-visualization-and-knn-classification
   * Shape: (150, 5)
   * Classes:   Iris-setosa, Iris-versicolor, Iris-virginica
   * Purpose: Identify class of iris flowers given petal information.


Settings
----------------

.. figure:: /Images/KNN(1).png
   :width: 700


Preprocessing using CyCon 
----------------
.. image:: ./Images/KNN(2).png
   :width: 700

.. .. code-block:: python

..    from sklearn.model_selection import train_test_split
..    X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income',
..        'Daily Internet Usage','Male']]
..    ad_data.columns
..    y = ad_data['Clicked on Ad']
..    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4)

KNN parameters in CyCon 
----------------
.. image:: ./Images/KNN(3).png
   :width: 700

.. code-block:: python
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
   KNN = KNeighborsClassifier(n_neighbors=3)
   KNN.fit(X_train,y_train) 

CyCon Score 
----------------
.. image:: ./Images/KNN(4).png
   :width: 500

Kaggle Score 
----------------

.. image:: ./Images/KNN(5).png
   :width: 500

