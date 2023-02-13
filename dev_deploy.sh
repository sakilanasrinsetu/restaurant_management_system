ssh root@178.128.214.106 "
cd restaurant_management_system-backend/
git pull
sudo service daphane restart
sudo service sheduler restart
echo "sheduler and daphane restarted on restaurant_management_system dev"
exit
"