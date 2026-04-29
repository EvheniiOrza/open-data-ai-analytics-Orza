# Покрокова інструкція: Розгортання через Argo CD (GitOps)

Цей гайд допоможе вам розгорнути Kubernetes кластер k3s на вашій Azure VM та налаштувати автоматичний деплой через Argo CD.

## 1. Встановлення k3s
У терміналі вашої Azure VM виконайте:
```bash
# Встановлення легкого Kubernetes (k3s)
curl -sfL https://get.k3s.io | sh -

# Перевірка статусу ноди (може знадобитися sudo)
sudo k3s kubectl get nodes
```

## 2. Встановлення Argo CD
```bash
# Створення namespace для Argo CD
sudo k3s kubectl create namespace argocd

# Встановлення Argo CD через офіційний маніфест
sudo k3s kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

## 3. Доступ до Argo CD UI
Щоб відкрити веб-інтерфейс Argo CD:
```bash
# Зміна типу сервісу на NodePort (відкриє доступ на порту сервера)
sudo k3s kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'

# Дізнайтеся порт (шукайте 443:XXXXX/TCP)
sudo k3s kubectl get svc -n argocd argocd-server

# Дістаньте пароль адміністратора (логін: admin)
sudo k3s kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```
Відкрийте у браузері: `https://<YOUR_VM_IP>:<NODE_PORT>` (ігноруйте попередження про сертифікат).

## 4. Підключення вашого проекту
Застосуйте маніфест Application, який ви створили:
```bash
sudo k3s kubectl apply -f gitops/argocd/application.yaml
```

## 5. Тестування GitOps (Автоматизація)
1. Відкрийте файл `gitops/app/deployment.yaml` у вашому репозиторії на GitHub.
2. Змініть `replicas: 2` на `replicas: 3`.
3. Зробіть коміт та пуш.
4. Спостерігайте в UI Argo CD, як кількість подів автоматично змінюється на 3 без вашого втручання.

## 6. Відкат (Rollback)
Якщо щось пішло не так, просто зробіть `git revert <commit_hash>` у своєму репозиторії, і Argo CD миттєво поверне попередню робочу версію додатку.
