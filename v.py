import requests
import json
import warnings

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

url = "https://172.30.0.103/api/v1/attendance/check-in-out"

headers = {
    "Content-Type": "application/json"
}

def send_rfid_request(rfid):
    data = {
        "rfid": rfid
    }

    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)

    if response.status_code == 200:
        response_json = response.json()
        print(f"RFID {rfid}: {response_json['message']}")
    else:
        print(f"RFID {rfid}: Request failed with status code {response.status_code}")

with open('rfid.txt', 'r') as file:
    for line in file:
        rfid = line.strip()
        send_rfid_request(rfid)
