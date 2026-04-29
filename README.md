# Розгортання Docker-інфраструктури в Azure за допомогою Terraform

Цей проєкт автоматизує створення віртуальної машини в Azure та розгортання веб-додатку (Nginx + Flask + MySQL) через Docker Compose.

## Попередня підготовка

Перед початком переконайтеся, що у вас згенеровано SSH-ключ:
```bash
ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
```

## Інструкція з розгортання

1.  **Відкрийте Azure Cloud Shell** (або термінал з встановленим Azure CLI та Terraform).
2.  **Клонуйте проєкт та перейдіть у робочу директорію**:
    ```bash
    git clone <url-вашого-репозиторію>
    cd project/infra/terraform/
    ```
3.  **Ініціалізуйте Terraform**:
    ```bash
    terraform init
    ```
4.  **Перевірте конфігурацію**:
    ```bash
    terraform fmt
    terraform validate
    terraform plan
    ```
5.  **Застосуйте зміни**:
    ```bash
    terraform apply -auto-approve
    ```
    *Зачекайте 3-5 хвилин, поки Azure створить ресурси, а cloud-init встановить Docker та запустить контейнери.*

## Перевірка результату

1.  Отримайте публічну IP-адресу з виводу Terraform:
    ```bash
    terraform output public_ip_address
    ```
2.  **Перевірка через браузер**: Відкрийте `http://<PUBLIC_IP>`.
3.  **Перевірка через термінал**:
    ```bash
    curl http://$(terraform output -raw public_ip_address)
    ```

## Видалення ресурсів

Щоб не витрачати кошти після завершення роботи:
```bash
terraform destroy -auto-approve
```
