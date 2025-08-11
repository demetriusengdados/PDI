provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "iot_rg" {
  name     = "iot-rg"
  location = "Brazil South"
}

resource "azurerm_iothub" "iot_hub" {
  name                = "iotHubDemo"
  location            = azurerm_resource_group.iot_rg.location
  resource_group_name = azurerm_resource_group.iot_rg.name
  sku {
    name     = "S1"
    capacity = 1
  }
}

resource "azurerm_eventhub_namespace" "eh_ns" {
  name                = "ehNamespaceDemo"
  location            = azurerm_resource_group.iot_rg.location
  resource_group_name = azurerm_resource_group.iot_rg.name
  sku                 = "Standard"
  capacity            = 1
}

resource "azurerm_eventhub" "eh" {
  name                = "ehDigitalTwins"
  namespace_name      = azurerm_eventhub_namespace.eh_ns.name
  resource_group_name = azurerm_resource_group.iot_rg.name
  partition_count     = 2
  message_retention   = 1
}

resource "azurerm_digital_twins_instance" "adt" {
  name                = "digitalTwinsDemo"
  location            = azurerm_resource_group.iot_rg.location
  resource_group_name = azurerm_resource_group.iot_rg.name
}

resource "azurerm_digital_twins_endpoint_eventhub" "adt_endpoint" {
  name                                   = "eventHubEndpoint"
  digital_twins_id                       = azurerm_digital_twins_instance.adt.id
  eventhub_primary_connection_string      = azurerm_eventhub_namespace.eh_ns.default_primary_connection_string
  eventhub_secondary_connection_string    = azurerm_eventhub_namespace.eh_ns.default_secondary_connection_string
}

resource "azurerm_digital_twins_endpoint_route" "adt_route" {
  name                      = "routeToEventHub"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  endpoint_name             = azurerm_digital_twins_endpoint_eventhub.adt_endpoint.name
  filter                   = "true"
}
resource "azurerm_digital_twins_model" "water_pump" {
  name                      = "dtmi:mining:WaterPump;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("water_pump2.json")
}
resource "azurerm_digital_twins_model" "power_generator" {
  name                      = "dtmi:mining:PowerGenerator;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("power_generator2.json")
}
resource "azurerm_digital_twins_model" "worker_badge" {
  name                      = "dtmi:mining:WorkerBadge;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("worker_badge2.json")
}
resource "azurerm_digital_twins_model" "excavator" {
  name                      = "dtmi:mining:Excavator;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("excavator2.json")
}
resource "azurerm_digital_twins_model" "excavator2" {
  name                      = "dtmi:mining:Excavator;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("excavator2.json")
}
resource "azurerm_digital_twins_model" "water_pump2" {
  name                      = "dtmi:mining:WaterPump;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("water_pump2.json")
}
resource "azurerm_digital_twins_model" "power_generator2" {
  name                      = "dtmi:mining:PowerGenerator;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("power_generator2.json")
}
resource "azurerm_digital_twins_model" "worker_badge2" {
  name                      = "dtmi:mining:WorkerBadge;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("worker_badge2.json")
}
resource "azurerm_digital_twins_model" "water_pump2" {
  name                      = "dtmi:mining:WaterPump;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("water_pump2.json")
}
resource "azurerm_digital_twins_model" "excavator2" {
  name                      = "dtmi:mining:Excavator;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("excavator2.json")
}
resource "azurerm_digital_twins_model" "water_pump2" {
  name                      = "dtmi:mining:WaterPump;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("water_pump2.json")
}
resource "azurerm_digital_twins_model" "power_generator2" {
  name                      = "dtmi:mining:PowerGenerator;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("power_generator2.json")
}
resource "azurerm_digital_twins_model" "worker_badge2" {
  name                      = "dtmi:mining:WorkerBadge;2"
  digital_twins_instance_id = azurerm_digital_twins_instance.adt.id
  model                     = file("worker_badge2.json")
}
