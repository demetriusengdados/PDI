az login
az group create --name MineraGroup --location eastus
az iot hub create --name MineraIoTHub --resource-group MineraGroup --sku F1
az iot hub device-identity create --hub-name MineraIoTHub --device-id ExcavatorDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id ExcavatorDevice --output table
