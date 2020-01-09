# Local Setup
## (optional/reccomended) Uninstall Any Old MySQL Install
This site provides a good guide: https://community.jaspersoft.com/wiki/uninstall-mysql-mac-os-x
I would recommend checking if the directories exist before removing them.

## Download MySQL
Here is a link to MySQL's instructions: https://dev.mysql.com/doc/mysql-osx-excerpt/5.7/en/
Be sure to download the install for 5.7! It is located here https://dev.mysql.com/downloads/mysql/
Click the link "Looking for previous GA versions?" to see 5.7.

## Install MySQL
The defaults should be fine for installation, but be sure to copy and save the password!

### Alias the MySQL Client

After installing, take the two lines in the snippet below and add them to either `~/.zshrc` or `~/.bash_profile` depending on if you are running zsh or bash as your terminal. This will allow you to execute the mysql client without typing its full path. Restart your terminal so that the changes take effect.

```
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin
```

### Change the Root Password
In your terminal run `mysql -u root -p`, it will prompt you for the password given in the install, enter it. This will pull up the MySQL client.

In the mysql client run `SET PASSWORD = PASSWORD('password');`. This will set your password to "password". Its fine (and probably better) to use annother one, but remember your password!

Exit back to your terminal with `exit`.

## Download and Install MySQL Workbench
https://dev.mysql.com/downloads/workbench/

## Connect with MySQLWorkbench
Hostname: 127.0.0.1
Port: 3306
Username: root
Password: ?

## Load the Database
Install with `pipenv install`. Run a shell with `pipenv shell`. Run the script with `python load_mysql.py`.

# GCP Setup

## Uninstall Cloud SDK (optional)
https://cloud.google.com/sdk/docs/uninstall-cloud-sdk
If you have any issues with the SDK, you can uninstall, but if it needs to update, it will prompt you.

## Install the Google Could SDK
https://cloud.google.com/sdk/docs/#install_the_latest_cloud_sdk_version
Follow the instructions.

## Create the Database Instance
https://cloud.google.com/sql/docs/mysql/quickstart
Follow the instructions under "Before you begin" and "Create an instance".
We'll connect to it later.

## Install and Start the Proxy
https://cloud.google.com/sql/docs/mysql/quickstart-proxy-test

## Connect with MySQLWorkbench
Hostname: 127.0.0.1
Port: 3306
Username: root
Password: ?

## Load the Database
Install with `pipenv install`. Run a shell with `pipenv shell`. Run the script with `python load_mysql.py`.
