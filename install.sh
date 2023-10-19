#!/bin/bash
echo "Installation of required packages..."

pip install -r requirements.txt

migrations_path="migrations/"

if [ -d $migrations_path ]; then
    echo "Migrations already exist, trying to migrate and upgrade ..."
    read -p "Create new database? (yes/no): " decide
    if [ $decide == "yes" ]; then
        python3 -m flask db migrate
        if [ $? -eq 1 ]; then
            echo "status - 1,could not migrate database,creating new migrations ..."
            rm -r $migrations_path
            python3 -m flask db init
            python3 -m flask db migrate
            echo "Database set up successful"
        else
            python3 -m flask db upgrade
            echo "Database set up successful"
        fi
    elif [ $decide == "no" ]; then
        echo "Exiting..."
        exit 0
    else 
        echo "Invalid input. Please enter 'yes' or 'no'."
    fi
else
    echo "Migrations does not exist, creating new one"
    python3 -m flask db init
    python3 -m flask db migrate
    python3 -m flask db upgrade
fi
read -p "Start Server on development? (yes/no): " decide
if [ $decide == "yes" ]; then
    python3 -m flask run
elif [ $decide == "no" ]; then
    echo "Exiting..."
    exit 0
else 
    echo "Invalid input. Please enter 'yes' or 'no'."
fi