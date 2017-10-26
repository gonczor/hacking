#!/bin/bash

sudo openssl req -new > new.ssl.csr
sudo openssl rsa -in privkey.pem -out new.cert.key
sudo openssl x509 -in new.ssl.csr -out new.cert.cert -req -signkey new.cert.key -days 999
if [ ! -d cert ]; then
    mkdir cert
fi
sudo cp new.cert.cert cert/server.crt
sudo cp new.cert.key cert/server.key
sudo rm new.ssl.csr
sudo rm new.cert.cert
sudo rm new.cert.key
sudo rm privkey.pem
