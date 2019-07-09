#!/bin/sh
set -e

log() {
  echo "[$(date +%Y-%m-%dT%H:%M:%S%:z)] $@"
}

# Sleep when asked to, to allow the database time to start
# before Taiga tries to run /checkdb.py below.
: ${TAIGA_SLEEP:=0}
sleep $TAIGA_SLEEP

# Setup and check database automatically if needed
if [ -z "$TAIGA_SKIP_DB_CHECK" ]; then
  log "Running database check"
  set +e
  python /checkdb.py
  DB_CHECK_STATUS=$?
  set -e

  if [ $DB_CHECK_STATUS -eq 1 ]; then
    log "Failed to connect to database server or database does not exist."
    exit 1
  fi

  # Database migration check should be done in all startup in case of backend upgrade
  log "Execute database migrations..."
  python manage.py migrate --noinput

  if [ $DB_CHECK_STATUS -eq 2 ]; then
    log "Configuring initial user"
    python manage.py loaddata initial_user
    log "Configuring initial project templates"
    python manage.py loaddata initial_project_templates

    if [ -n $TAIGA_ADMIN_PASSWORD ]; then
      log "Changing initial admin password"
      python manage.py shell < /changeadminpasswd.py
    fi
  fi

  # TODO This works... but requires to persist the backend to keep track of already executed migrations
  # BREAKING CHANGES INCOMING
  #if python manage.py migrate --noinput | grep 'Your models have changes that are not yet reflected in a migration'; then
  #  log "Generate database migrations..."
  #  python manage.py makemigrations
  #  log "Execute database migrations..."
  #  python manage.py migrate --noinput
  #fi

fi

# In case of frontend upgrade, locales and statics should be regenerated
log "Compiling messages and collecting static"
python manage.py compilemessages > /dev/null
python manage.py collectstatic --noinput > /dev/null

log "Start gunicorn server"
exec "$@"
