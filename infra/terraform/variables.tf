variable "resource_group_location" {
  type        = string
  default     = "eastus"
  description = "Локація для всіх ресурсів у Azure."
}

variable "resource_prefix" {
  type        = string
  default     = "orza-lab"
  description = "Префікс для назв ресурсів."
}

variable "vm_size" {
  type        = string
  default     = "Standard_B1s"
  description = "Розмір віртуальної машини."
}

variable "admin_username" {
  type        = string
  default     = "azureuser"
  description = "Ім'я адміністратора для VM."
}
