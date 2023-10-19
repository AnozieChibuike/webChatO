Write-Host "Installation of required packages..."
# pip install -r requirements.txt
# pip install --upgrade -r requirements.txt

$migrationsPath = "migrations"

if (Test-Path -Path $migrationsPath -PathType Container) {
    Write-Host "Migrations already exist, trying to migrate and upgrade ..."
    $decide = Read-Host "Create new database? (yes/no)"
    if ($decide -eq "yes") {
        python -m flask db migrate
        if ($LASTEXITCODE -ne 0) {
            Write-Host "status - 1, could not migrate database, creating new migrations ..."
            Remove-Item -Path $migrationsPath -Recurse -Force
            python -m flask db init
            python -m flask db migrate
            Write-Host "Database set up successful"
        } else {
            python -m flask db upgrade
            Write-Host "Database set up successful"
        }
    } elseif ($decide -eq "no") {
        $decide = Read-Host "Start Server on development? (yes/no)"

        if ($decide -eq "yes") {
            python -m flask run
        }
        elseif ($decide -eq "no") {
            Write-Host "Exiting..."
            exit 0
        }
        else {
            Write-Host "Invalid input. Please enter 'yes' or 'no'."
        }

            } else {
                Write-Host "Invalid input. Please enter 'yes' or 'no'."
            }
} else {
    Write-Host "Migrations does not exist, creating new one"
    python -m flask db init
    python -m flask db migrate
    python -m flask db upgrade
}
$decide = Read-Host "Start Server on development? (yes/no)"

if ($decide -eq "yes") {
    python -m flask run
}
elseif ($decide -eq "no") {
    Write-Host "Exiting..."
    exit 0
}
else {
    Write-Host "Invalid input. Please enter 'yes' or 'no'."
}
