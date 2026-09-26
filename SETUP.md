# StockSense — Local Setup Guide

Follow these steps to run this project on your own machine.

## 1. Clone this repo
mkdir -p ~/odoo-projects/odoo19
cd ~/odoo-projects/odoo19
git clone https://github.com/Alexrosariyo319/stocksense.git .

## 2. Create your Python virtual environment
Requires Python 3.12.
python3.12 -m venv .venv
source .venv/bin/activate
(Windows: python -m venv .venv then .venv\Scripts\activate)

## 3. Clone Odoo 19 source (not included in this repo, it's huge)
git clone https://github.com/odoo/odoo --depth 1 --branch 19.0 --single-branch odoo-src
cd odoo-src
pip install -r requirements.txt
If psycopg2 fails to build, run pip install psycopg2-binary instead.

## 4. Install and start PostgreSQL
brew install postgresql@17
brew services start postgresql@17
Create your own database user:
psql postgres
CREATE USER odoo WITH SUPERUSER PASSWORD yourpassword;
then type backslash q to quit psql

## 5. Create your own config file
This file is not in git, it holds your local DB password. Create it yourself:
cd ..
mkdir -p config
nano config/odoo.conf
Paste this in, using your own absolute paths and password:

options section:
admin_passwd = admin
db_host = localhost
db_port = 5432
db_user = odoo
db_password = yourpassword
addons_path = path to odoo-src/addons, path to custom_addons, path to odoo-training
http_port = 8019

## 6. Run the server and install all modules
cd odoo-src
python odoo-bin -c ../config/odoo.conf -i all -d stocksense
Use -i all the first time to install every module in custom_addons. After that, use -u module_name when you update your own module's code.

## 7. Open it
Visit http://localhost:8019 and create your database when prompted, first run only.

## Team workflow
Pull before you start: git pull
Push when you are done: git add . then git commit then git push
Work inside your own subfolder in custom_addons to avoid conflicts with teammates
