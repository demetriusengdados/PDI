from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import DefaultAzureCredential
import json

client = DigitalTwinsClient("https://<your-instance>.api.<region>.digitaltwins.azure.net", DefaultAzureCredential())

def main(event: dict):
    data = json.loads(event['body'])
    twin_id = "excavator1"
    patch = [
        {"op": "replace", "path": "/temperature", "value": data["temperature"]},
        {"op": "replace", "path": "/vibration", "value": data["vibration"]}
    ]
    client.update_digital_twin(twin_id, patch)
    print(f"Updated twin {twin_id} with data: {data}")  
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Twin updated successfully"})
    }
