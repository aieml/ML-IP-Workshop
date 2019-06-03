from sklearn import datasets #importing toy datasets available in scikit learn into this python code

dataset=datasets.load_iris() #iris flower dataset will be loaded into dataset

data=dataset.data
target=dataset.target


print(data)
