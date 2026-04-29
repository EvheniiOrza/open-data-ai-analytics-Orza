output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "public_ip_address" {
  value       = azurerm_linux_virtual_machine.vm.public_ip_address
  description = "Публічна IP-адреса розгорнутої віртуальної машини."
}

output "ssh_command" {
  value       = "ssh ${var.admin_username}@${azurerm_linux_virtual_machine.vm.public_ip_address}"
  description = "Команда для підключення по SSH."
}
