from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

def main():
    data = fetch_olivetti_faces()
    X = data.images
    y = data.target

    n_samples = X.shape[0]
    X_flat = X.reshape((n_samples, -1))

    X_train, X_test, y_train, y_test = train_test_split(
        X_flat, y, train_size=0.7, random_state=42, stratify=y)

    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)

    joblib.dump({'model': clf, 'X_test': X_test, 'y_test': y_test}, 'savedmodel.pth')
    print("✅ Training completed. Model saved as savedmodel.pth")

if __name__ == "__main__":
    main()
