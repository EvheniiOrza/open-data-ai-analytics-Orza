# Open Data AI Analytics - Infrastructure & Deployment

Цей репозиторій містить Docker-проект для аналітики даних та інфраструктурний код Terraform для автоматичного розгортання в Azure.

## Структура репозиторію
- `/web`, `/data_load`, `/visualization` — сервіси Docker-проекту.
- `/infra/terraform/` — конфігураційні файли Terraform.
- `compose.yaml` — файл для оркестрації контейнерів.

## Інструкція для розгортання через Azure Cloud Shell

### 1. Підготовка
1. Увійдіть у [Azure Portal](https://portal.azure.com).
2. Відкрийте **Cloud Shell** (іконка `>_` вгорі), оберіть **Bash**.
3. Клонуйте цей репозиторій:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/open-data-ai-analytics-Orza.git
   cd open-data-ai-analytics-Orza/infra/terraform/
   ```

### 2. Розгортання інфраструктури
Виконайте наступні команди:
```bash
# Ініціалізація провайдерів
terraform init

# Перевірка плану розгортання
terraform plan

# Застосування (створення ресурсів)
terraform apply -auto-approve
```

### 3. Перевірка результату
- Після завершення (3-5 хв) Terraform виведе `public_ip_address`.
- Перейдіть за адресою: `http://<PUBLIC_IP>:8501` (для Streamlit) або `http://<PUBLIC_IP>` (якщо налаштований Nginx).
- Для перевірки через термінал: `curl http://<PUBLIC_IP>:8501`.

### 4. Видалення ресурсів
Щоб уникнути зайвих витрат, видаліть інфраструктуру після перевірки:
```bash
terraform destroy -auto-approve
```

---
**Розробив:** Орза Євгеній Сергійович, студент групи ШІ-33.
