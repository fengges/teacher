
from sklearn.model_selection import  train_test_split as test
X_train, X_test, y_train, y_test=test(tfidf,label, test_size = 0.7,random_state = 42)
from sklearn.svm import SVC,LinearSVC
# svclf = SVC(kernel = 'linear')
svclf=LinearSVC()
svclf.fit(X_train,y_train)
preds = svclf.predict(X_test)
num = 0
preds = preds.tolist()
for i,pred in enumerate(preds):
    if int(pred) == int(y_test[i]):
        num += 1
print ('precision_score:' + str(float(num) / len(preds)))


