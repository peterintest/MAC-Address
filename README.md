# MAC Address Client

Command-line tool to lookup company name associated with MAC address
using macaddress.io API

## Prerequisites
- Docker is installed
- Clone this repository locally and `cd` to the directory

## Build
- Add provided API key to the .env file
- Run `docker build -t mac_address .`

## Run
- `docker run -it mac_address <mac address>>`

e.g. 

- `docker run -it mac_address 44:38:39:ff:ef:57`

## TODO
- Write unit tests