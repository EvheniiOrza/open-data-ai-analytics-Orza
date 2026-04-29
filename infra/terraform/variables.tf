variable "resource_group_location" {
  type        = string
  default     = "northeurope"
  description = "Локація для всіх ресурсів у Azure."
}

variable "resource_prefix" {
  type        = string
  default     = "orza-lab-v2"
  description = "Префікс для назв ресурсів."
}

variable "vm_size" {
  type        = string
  default     = "Standard_B1ms"
  description = "Розмір віртуальної машини."
}

variable "admin_username" {
  type        = string
  default     = "azureuser"
  description = "Ім'я адміністратора для VM."
}
