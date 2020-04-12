#!/usr/bin/env python
    # coding: utf-8
    
    # # Naive Bayes, K-nearest, DecisionTree Classifiers
    
    import pandas as pd
    import numpy as np
    
    ds=pd.read_csv('iris.csv')
    ds.shape
    
    X=ds.values[:,:-1]
    Y=ds.values[:,-1]
    print(X.shape)
    print(Y.shape)
        
    # # Data Split
    
    from sklearn.model_selection import train_test_split
        
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=3)
    
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score, confusion_matrix
        
    DTclassifer = DecisionTreeClassifier()
    
    DTclassifer.fit(X_train,Y_train)
    
    predictions=DTclassifer.predict(X_test)
    predictions
        
    # # Accuracy Score
    
    accuracy_score(Y_test,predictions)
        
    # # Confusion Matrix
    
    confusion_matrix(Y_test,predictions)
    
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.preprocessing import MinMaxScaler
    
    dataset = "wine_dataset.txt"
    label=['class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
    dt= pd.read_csv(dataset,names=label)
    
    print(dt.shape)
    
    dt.groupby('class').size()
    
    data=dt.values##in csv file 1st column is classlabel
    x=data[:,1:]##contains all info other than class label
    y=data[:,0]##class label 
    ##print(x)
    print(y)
    
    ### 5.1a) case1 :test is 25%
    
    Val_size=0.33 #test size is how much rest is training
    random_seed=3 #randomly chosing
    X_train,X_test,Y_train,Y_test=model_selection.train_test_split(x,y,test_size = Val_size,random_state=random_seed)
    deciTree = DecisionTreeClassifier()
    deciTree.fit(X_train, Y_train)
    predictions = deciTree.predict(X_test)
    print("Accuracy on the Test Data ")
    print(accuracy_score(Y_test, predictions))
    
    ### 5.1b case2 :testset is 2/3rd 
    
    Val_size=0.33 #test size is how much rest is training
    random_seed=3 #randomly chosing
    X_train,X_test,Y_train,Y_test=model_selection.train_test_split(x,y,test_size = Val_size,random_state=random_seed)
    deciTree = DecisionTreeClassifier()
    deciTree.fit(X_train, Y_train)
    predictions = deciTree.predict(X_test)
    print("Accuracy on the Test Data ")
    print(accuracy_score(Y_test, predictions))
    
    ###5.3 scaling of data using minmaxscaler()
    
    scaler=MinMaxScaler()
    print(scaler.fit(dt))
    
    ##5.2(b)choosing dataset using holdout method
    
    ##assume test data as 10% and rest as training data

    Val_size=0.33 #test size is how much rest is training
    random_seed=3 #randomly chosing
    X_train,X_test,Y_train,Y_test=model_selection.train_test_split(x,y,test_size = Val_size,random_state=random_seed)
    deciTree = DecisionTreeClassifier()
    deciTree.fit(X_train, Y_train)
    predictions = deciTree.predict(X_test)
    print("Accuracy on the Test Data ")
    print(accuracy_score(Y_test, predictions))
    
    ##knearest neighbour
    
    neigh = KNeighborsClassifier(n_neighbors=3)
    neigh.fit(X_train,Y_train) 
    
    ## print(neigh.predict([Y_test]))
    