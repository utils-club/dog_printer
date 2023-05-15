# create folder
sudo mkdir /opt/dog_printer
sudo chmod 777 dog_printer
# populate files
cp dog.py /opt/dog_printer
cp requirements.txt /opt/dog_printer
# setup env
cd /opt/dog_printer
python3 -m venv nv
source nv/bin/activate
pip install -r requirements.txt
# show how to setup init task
echo "el comando para que el programa inicie solo desde el encencido del sistema operativo es:"
echo "/opt/dog_printer/nb/bin/python -OO /opt/dog_printer/dog.py"