WORKSPACE=$1
sudo rm -rf /var/opt/rdbms/relationalDBManagementSystem
sudo mkdir -p /var/opt/rdbms/relationalDBManagementSystem

sudo cp $WORKSPACE/relationalDBManagementSystem/**/*.* /var/opt/rdbms/relationalDBManagementSystem/
cd /usr/lib/python3.7/site-packages
echo "/var/opt/rdbms/relationalDBManagementSystem" > addProjectPath.pth

cd /var/opt/rdbms/relationalDBManagementSystem/rdbms/
echo "Starting Server..."
python manage.py runserver
