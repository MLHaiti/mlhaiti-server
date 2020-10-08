#!/bin/bash

DKL_DIR=$(pwd)
WORK_DIR="$(cd "$(dirname "$0")" && pwd)"

source $WORK_DIR/_function.sh

################ ~ ENVIRONEMENT FILE
ENV_TEMPLATE=.env.template 

if [ ! -f .env ]; then
    echo ""
    print_info "- Creating environement file;"
    cp $ENV_TEMPLATE .env
fi

source .env

################ ~ SETTING UP POSTGRESQL 
sudo apt-get install postgresql postgresql-12-postgis-3 postgresql-contrib

function _psql {
    sudo -u postgres psql -c "$1"
}

# Grab database info from .env file
if [ -f .env ]; then
    source .env 
else
    print_error "!! Don't found environnement file: .env"
    exit 1;
fi

# Creating database if not already exists
# https://stackoverflow.com/questions/14549270/check-if-database-exists-in-postgresql-using-shell
if psql -lqt | cut -d \| -f 1 | grep -qw $DB_NAME; then
    # database exists
    # $? is 0
    print_info "DELETING OLD $DB_NAME DB"
    _psql "DROP DATABASE $DB_NAME;"
fi

print_info "CREATING A NEW $DB_NAME DB"

_psql "CREATE DATABASE $DB_NAME;"

# https://stackoverflow.com/questions/8546759/how-to-check-if-a-postgres-user-exists
if psql -t -c '\du' | cut -d \| -f 1 | grep -qw $DB_USER; then
    # user exists
    # $? is 0
    _psql "DROP USER $DB_USER;"
fi

_psql "CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASSWORD';"
_psql "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
_psql "\connect $DB_NAME;"
_psql "ALTER USER $DB_USER WITH SUPERUSER;" 


print_info "INSTALLATION RÉUSSIE"