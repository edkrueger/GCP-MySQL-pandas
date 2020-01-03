# Loading a GCP Database with Pandas and SQLAlchemy

## Create the Database Instance
https://cloud.google.com/sql/docs/mysql/quickstart
Follow the instructions under "Before you begin" and "Create an instance".
We'll connect to it later.

## Download MySQL Workbench
https://dev.mysql.com/downloads/workbench/

## Install the Google Could SDK
https://cloud.google.com/sdk/docs/#install_the_latest_cloud_sdk_version

## Install and Start the Proxy
https://cloud.google.com/sql/docs/mysql/quickstart-proxy-test

## Connect with MySQLWorkbench
Hostname: 127.0.0.1
Port: 3306
Username: Root
Password: ?

## Load the Database
Install with `pipenv install`. Run a shell with `pipenv shell`. Run the script with `python load_mysql.py`.