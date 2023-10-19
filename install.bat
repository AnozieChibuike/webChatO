@echo off
echo Installation of required packages...

pip install -r requirements.txt

set migrationsPath=migrations

if exist %migrationsPath% (
    echo Migrations already exist, trying to migrate and upgrade ...
    set /p decide=Create new database? (yes/no): 
    if "%decide%"=="yes" (
        python -m flask db migrate
        if errorlevel 1 (
            echo status - 1, could not migrate database, creating new migrations ...
            rmdir /s /q %migrationsPath%
            python -m flask db init
            python -m flask db migrate
            echo Database set up successful
        ) else (
            python -m flask db upgrade
            echo Database set up successful
        )
    ) elseif "%decide%"=="no" (
        set /p decide=Start Server on development? (yes/no): 
        if "%decide%"=="yes" (
            python -m flask run
        ) elseif "%decide%"=="no" (
            echo Exiting...
            exit /b 0
        ) else (
            echo Invalid input. Please enter 'yes' or 'no'.
        )
    ) else (
        echo Invalid input. Please enter 'yes' or 'no'.
    )
) else (
    echo Migrations do not exist, creating new one
    python -m flask db init
    python -m flask db migrate
    python -m flask db upgrade
)
set /p decide=Start Server on development? (yes/no): 

if "%decide%"=="yes" (
    python -m flask run
) elseif "%decide%"=="no" (
    echo Exiting...
    exit /b 0
) else (
    echo Invalid input. Please enter 'yes' or 'no'.
)
