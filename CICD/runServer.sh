WORKSPACE=$1
DESTINATION="/var/opt/rdbms/relationalDBManagementSystem/"
sudo rm -rf $DESTINATION
sudo mkdir -p $DESTINATION

sudo cp -rvf $WORKSPACE/* $DESTINATION
sudo chown -R $USER:$USER /usr/lib/python3.7/site-packages
echo "/var/opt/rdbms/relationalDBManagementSystem" > /usr/lib/python3.7/site-packages/addProjectPath.pth
ls -lrt /usr/lib/python3.7/site-packages/
cd $DESTINATION/rdbms/
echo "Starting Server..."
python manage.py runserver
