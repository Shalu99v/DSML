import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import  tree
iris=load_iris() 
x,y=iris.data,iris.target
clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
tree.plot_tree(clf)
print(tree.plot_tree(clf))
plt.show()


