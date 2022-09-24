echo [$(date)]:"START"
echo [$(date)]:"Creating Conda environment with Python 3.9"
conda create --prefix ./env python=3.9 -y
echo [$(date)]:"Activating Environment"
source activate ./env
echo [$(date)]:"Installing Dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]:"END"