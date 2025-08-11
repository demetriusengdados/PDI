output "iot_hub_name" {
  value = azurerm_iothub.iot_hub.name
}

output "digital_twins_url" {
  value = azurerm_digital_twins_instance.adt.host_name
}

output "eventhub_namespace" {
  value = azurerm_eventhub_namespace.eh_ns.name
}
output "eventhub_name" {
  value = azurerm_eventhub.eh.name
}