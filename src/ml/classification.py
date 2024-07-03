from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import io
import matplotlib.pyplot as plt



# Overfiting :(
def knn(k, X, y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Scale the features using StandardScaler
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Encode the labels to numeric values
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)
    y_test_encoded = label_encoder.transform(y_test)

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train_encoded)

    y_pred_encoded = knn.predict(X_test)
    accuracy = accuracy_score(y_test_encoded, y_pred_encoded)

    # Visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(X_test[:, 0], X_test[:, 1], c=y_pred_encoded, cmap='viridis', marker='o', edgecolor='k', s=50, alpha=0.7)
    ax.set_title(f'KNN Classification (k={k})\nAccuracy: {accuracy:.2f}')
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    fig.colorbar(scatter, ax=ax, label='Predicted Label')
    plt.grid(True)
    
    return fig, accuracy

def random_forest(X, y):
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 

    # Create Random Forest classifier object
    clf = RandomForestClassifier(n_estimators=100, random_state=1)

    # Train Random Forest classifier
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Visualize one of the trees in the random forest
    fig, ax = plt.subplots(figsize=(20, 10))
    plot_tree(clf.estimators_[0], filled=True, feature_names=X.columns, class_names=[str(i) for i in clf.classes_], ax=ax)
    plt.title("Random Forest Visualization (Single Tree)")
    
    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return accuracy, buf

def decision_tree(X, y, max_depth=None):
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 

    # Create Decision Tree classifier object with the given max_depth
    clf = DecisionTreeClassifier(max_depth=max_depth)

    # Train Decision Tree classifier
    clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Visualize the decision tree
    fig, ax = plt.subplots(figsize=(20, 10))
    plot_tree(clf, filled=True, feature_names=X.columns, class_names=[str(i) for i in clf.classes_], ax=ax)
    plt.title("Decision Tree Visualization")
    
    # Save plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return accuracy, buf