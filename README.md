# MLOPS MAJOR ASSIGNMENT  
**Author:** Aastha Singh  
**Roll No:** G24AI2079  

---

## 🧠 Project Overview
This project demonstrates the complete **MLOps pipeline** for a simple machine learning model — a **Decision Tree Classifier** trained on the **Olivetti Faces dataset** from `sklearn`.  
It includes:
- Model training and testing automation using **GitHub Actions (CI/CD)**  
- Containerization using **Docker**  
- Deployment on **Kubernetes (minikube)** with **3 replicas**

---

## ⚙️ Setup Instructions

### 🐍 Local Development
```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model
python train.py

# 4. Test the model
python test.py

# 5. Run Flask app locally
python app.py

docker build -t aasthasingh20/olivetti-face:1.0 .

docker run -p 5000:5000 aasthasingh20/olivetti-face:1.0

docker push aasthasingh20/olivetti-face:1.0


🔗 **Docker Hub Repository:**  
[https://hub.docker.com/r/aasthasingh20/olivetti-face](https://hub.docker.com/r/aasthasingh20/olivetti-face)

---

## ☸️ Kubernetes Deployment (Minikube)
Make sure Docker Desktop is running, then start minikube:
```bash
minikube start --driver=docker
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml


kubectl get pods -o wide
kubectl get svc

minikube service olivetti-service --url

✅ You should see your Flask web app served by **3 Kubernetes pods**.

---

## 🤖 CI/CD Workflows
- **Branch:** `dev` → runs `train.py` and `test.py` automatically via GitHub Actions (`ci.yml`).
- **Branch:** `docker_cicd` → containerization, Docker build, and deployment setup.
- **Branch:** `main` → final stable version.

All tests pass automatically on push to `dev` branch.

---

## 📸 Screenshots (for submission)
Include the following in your report:
1. ✅ GitHub Actions “Passed” status (CI run).  
2. 🐳 Docker Hub repository showing tag `1.0`.  
3. ☸️ `kubectl get pods -o wide` (3 pods running).  
4. ☸️ `kubectl get svc` (LoadBalancer).  
5. 🌐 Flask app in browser via `minikube service … --url`.

---

## 🧾 Results
- **Model Used:** DecisionTreeClassifier (sklearn)  
- **Dataset:** Olivetti Faces (64×64 grayscale)  
- **Test Accuracy:** ~0.37  
- **Replicas in Kubernetes:** 3  
- **Container Size:** ~610MB  
- **Image Registry:** Docker Hub (Public)

---

## 🚀 Future Improvements
- Use a CNN-based model for higher accuracy  
- Add persistent volume for model storage  
- Integrate model retraining in CI/CD  
- Deploy on a managed Kubernetes cluster (e.g., EKS / GKE)

---

## 🧑‍💻 Author
**Aastha Singh**  
Roll No: G24AI2079  
GitHub: [github.com/AasthaSingh6124](https://github.com/AasthaSingh6124)

---

