# pip install influxdb
from influxdb import InfluxDBClient
from datetime import datetime


# Setup database
client = InfluxDBClient('localhost', 8086, 'admin', 'passwd', 'influxdb-01')
client.create_database('influxdb-01')
client.get_list_database()
client.switch_database('influxdb-01')


# Setup Payload
json_payload = []
data = {
    "measurement": "stocks",
    "tags": {
        "ticker": "TSLA"
    },
    "time": datetime.now(),
    "fields": {
        "open": 688.37,
        "close": 667.93
    }
}
json_payload.append(data)


# Send our payload
client.write_points(json_payload)


# Select statement



#  