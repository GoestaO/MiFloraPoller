# MiFloraPoller
A poller to fetch the sensordata from a Xiaomi Mi Flora plant sensor

## How to use it

* cd into poller folder and install the requirements: `sudo pip3 install -r requirements.txt`
* create a config.yaml file in the folder "poller"
* add a configuration and fill with the values you need, you can use this reference:

`
#required: at least one sensor
sensors:
  - name: Sensor 1
    bluetooth_mac_address: 'MAC_ADDRESS'
  - name: Sensor 2
    bluetooth_mac_address: 'MAC_ADDRESS'
database:
  host: HOST
  username: USERNAME
  password: PASSWORD
  db_name: DB_NAME`
  
  * `python3`
