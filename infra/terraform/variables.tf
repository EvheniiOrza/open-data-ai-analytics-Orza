variable "resource_group_location" {
  type        = string
  default     = "uksouth"
  description = "Локація для всіх ресурсу у Azure."
}

variable "resource_prefix" {
  type        = string
  default     = "orza-lab-v4"
  description = "Префікс для назв ресурсів."
}

variable "vm_size" {
  type        = string
  default     = "Standard_D2s_v3"
  description = "Розмір віртуальної машини."
}

variable "admin_username" {
  type        = string
  default     = "azureuser"
  description = "Ім'я адміністратора для VM."
}
