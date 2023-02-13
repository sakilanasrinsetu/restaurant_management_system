#!/bin/bash
ssh root@178.128.121.166 "
cd restaurant_management_system-backend/
git pull
sudo service daphane restart
sudo service sheduler restart
echo "sheduler and daphane restarted on restaurant_management_system production"
exit
"

ssh root@178.128.214.106 "
cd restaurant_management_system-backend/
git pull
sudo service daphane restart
sudo service sheduler restart
echo "sheduler and daphane restarted on restaurant_management_system dev"
exit
"

# momos cafe
ssh root@139.59.114.34 "
cd restaurant_management_system-backend/
git pull
sudo service daphane restart
sudo service sheduler restart
echo "sheduler and daphane restarted on momos cafe"
exit
"