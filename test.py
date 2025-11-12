import joblib
from sklearn.metrics import accuracy_score

def main():
    data = joblib.load('savedmodel.pth')
    model = data['model']
    X_test = data['X_test']
    y_test = data['y_test']

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"✅ Test accuracy: {acc:.4f}")

if __name__ == "__main__":
    main()
