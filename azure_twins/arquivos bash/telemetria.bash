pip install azure-iot-device
az iot hub device-identity create --hub-name MineraIoTHub --device-id BulldozerDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id BulldozerDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id DumpTruckDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id DumpTruckDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id   LoaderDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id LoaderDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id GraderDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id GraderDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id CraneDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id CraneDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id BulldozerDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id BulldozerDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id DumpTruckDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id DumpTruckDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id LoaderDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id LoaderDevice --output table
python telemetria.py
az iot hub device-identity create --hub-name MineraIoTHub --device-id GraderDevice
az iot hub device-identity show-connection-string --hub-name MineraIoTHub --device-id GraderDevice --output table
python telemetria.py