from sklearn import datasets #importing toy datasets available in scikit learn into this python code

dataset=datasets.load_iris() #iris flower dataset will be loaded into dataset

data=dataset.data
target=dataset.target

from sklearn.model_selection import train_test_split #to split a dataset into training & testing

train_data,test_data,train_target,test_target=train_test_split(data,target,test_size=0.1)

from sklearn.neighbors import KNeighborsClassifier #import KNN Algorithm into the code

clsfr=KNeighborsClassifier() #loading a KNN algorithm into clsfr

clsfr.fit(train_data,train_target) #training the KNN model

results=clsfr.predict(test_data)

print('Predictes Results:',results)
print('Actual Results:',test_target)

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(test_target,results)

print('accuracy:',accuracy)

