from sklearn import tree

# x = [height , weight, shoe size], (features)

X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],
     [175,64,39],[177,70,40],[159,55,37],[177,75,42],[181,85,43]]

#y = output 
Y = ['male','female','female','female','male','male','male','female','male',
     'female','male']

#decision tree clasifier
clf = tree.DecisionTreeClassifier()

#train on the data set by fitting the data set- Two arguments
clf = clf.fit(X,Y)

#Testing time 
prediction = clf.predict([[190,70,43]])

print(prediction)
