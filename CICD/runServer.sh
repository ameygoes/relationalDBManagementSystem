WORKSPACE=$1
DESTINATION="/var/opt/rdbms/relationalDBManagementSystem/"
sudo rm -rf $DESTINATION
sudo mkdir -p $DESTINATION

sudo cp -rvf $WORKSPACE/* $DESTINATION
cd /usr/lib/python3.7/
sudo chown -R $USER:$USER site-packages
echo "/var/opt/rdbms/relationalDBManagementSystem" > addProjectPath.pth

cd $DESTINATION/rdbms/
echo "Starting Server..."
python manage.py runserver
