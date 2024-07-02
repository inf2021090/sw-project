from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

# Overfiting after 6
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