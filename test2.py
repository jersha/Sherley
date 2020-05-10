import pickle
from sklearn import cross_validation

character = ['love', 'life', 'death', 'girl', 'soul']

file_name1 = "D:\word_data.pkl"
file_name2 = "D:\email_authors.pkl"

file_object = open(file_name,'rb')

authors = pickle.load(file_object)
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(file_name1, file_name2, test_size=0.1, random_state=42)

print(features_train)

file_object.close()
