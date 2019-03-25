
[uri_license]: http://www.gnu.org/licenses/agpl.html
[uri_license_image]: https://img.shields.io/badge/License-AGPL%20v3-blue.svg

[![License: AGPL v3][uri_license_image]][uri_license]
[![Build Status](https://travis-ci.org/Monogramm/docker-taiga-back-base.svg)](https://travis-ci.org/Monogramm/docker-taiga-back-base)
[![Docker Automated buid](https://img.shields.io/docker/cloud/build/monogramm/docker-taiga-back-base.svg)](https://hub.docker.com/r/monogramm/docker-taiga-back-base/)
[![Docker Pulls](https://img.shields.io/docker/pulls/monogramm/docker-taiga-back-base.svg)](https://hub.docker.com/r/monogramm/docker-taiga-back-base/)
[![](https://images.microbadger.com/badges/version/monogramm/docker-taiga-back-base.svg)](https://microbadger.com/images/monogramm/docker-taiga-back-base)
[![](https://images.microbadger.com/badges/image/monogramm/docker-taiga-back-base.svg)](https://microbadger.com/images/monogramm/docker-taiga-back-base)


# Docker image for taiga-back

This Docker repository provides the [taiga-back](https://github.com/taigaio/taiga-back) server with a configuration suitable to use with [taiga-front](https://github.com/taigaio/taiga-front).

This image was inspired by [ajira86/docker-taiga](https://github.com/ajira86/docker-taiga) which is a fork of [benhutchins/docker-taiga](https://github.com/benhutchins/docker-taiga).

For a more advanced image and full docker-compose example, checkout [Monogramm/docker-taiga](https://github.com/Monogramm/docker-taiga).


## What is Taiga?

Taiga is a project management platform for startups and agile developers & designers who want a simple, beautiful tool that makes work truly enjoyable.

> [taiga.io](https://taiga.io)


## Supported tags

https://hub.docker.com/r/monogramm/docker-taiga-back-base/

-	`3.3`, `3.3-alpine` (*3.3/alpine/Dockerfile*)
-	`3.4`, `3.4-alpine`, `3`, `3-alpine` (*3.4/alpine/Dockerfile*)
-	`4.0`, `4.0-alpine` (*4.0/alpine/Dockerfile*)
-	`4.1`, `4.1-alpine` (*4.1/alpine/Dockerfile*)
-	`4.2-alpine`, `4.2`, `4-alpine`, `4`, `alpine`, `latest` (*4.2/alpine/Dockerfile*)


## Build Docker image

To generate docker images from the template, execute `update.sh` script.

Install Docker and then run `docker build -t docker-taiga-back-base images/VARIANT/VERSION` to build the image for the variant and version you need.

You can also build all images by running `update.sh build`.


# Adding Features
If the image does not include the packages you need, you can easily build your own image on top of it.
Start your derived image with the `FROM` statement and add whatever you like.

```Dockerfile
FROM monogramm/docker-taiga-back-base:alpine

RUN ...

```

You can also clone this repository and use the [update.sh](update.sh) shell script to generate a new Dockerfile based on your own needs.

For instance, you could build a container based on Dolibarr develop branch by setting the `update.sh` versions like this:
```bash
latests=( "master" )
```
Then simply call [update.sh](update.sh) script.

```console
bash update.sh
```
Your Dockerfile(s) will be generated in the `images/` folder.


## Auto configuration via environment variables

The Taiga image supports auto configuration via environment variables. You can preconfigure nearly everything that is available in `local.py`.

See [local.py.example](https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example) and [docker-settings.py](https://github.com/Monogramm/docker-taiga-back-base/blob/master/docker-docker.py) for more details on configuration.


### TAIGA_DB_NAME

*Default value*: `taiga`

Your database name (REQUIRED)

Examples:
```yml
TAIGA_DB_NAME=taiga
TAIGA_DB_NAME=taigadb
```

### TAIGA_DB_HOST

*Default value*: `taigadb`

Your database hostname (REQUIRED)

Examples:
```yml
TAIGA_DB_HOST=taigadb
TAIGA_DB_HOST=taigadb.company.com
```

### TAIGA_DB_USER

*Default value*: `taiga`

Your database user (REQUIRED)

Examples:
```yml
TAIGA_DB_USER=taiga
TAIGA_DB_USER=taigadb
```

### TAIGA_DB_PASSWORD

*Default value*:

Your database user passsword (REQUIRED)

Examples:
```yml
TAIGA_DB_PASSWORD=somethingsecure
```

### TAIGA_HOSTNAME

*Default value*: `localhost`

Your service hostname (REQUIRED). Remember to set it in the front client too.

Examples:
```yml
TAIGA_HOSTNAME=localhost
TAIGA_HOSTNAME=taiga.company.com
```

### TAIGA_ENABLE_EMAIL

*Default value*: `False`

Enable email server configuration

Examples:
```yml
TAIGA_ENABLE_EMAIL=False
```
```yml
TAIGA_ENABLE_EMAIL=True
TAIGA_EMAIL_FROM=no-reply@gmail.com
TAIGA_EMAIL_USE_TLS=False
TAIGA_EMAIL_HOST=smtp.gmail.com
TAIGA_EMAIL_PORT=465
TAIGA_EMAIL_USER=user.taiga@gmail.com
TAIGA_EMAIL_PASS=usertaigagmailappsecret
```
```yml
TAIGA_ENABLE_EMAIL=True
TAIGA_EMAIL_FROM=no-reply@company.com
TAIGA_EMAIL_USE_TLS=True
TAIGA_EMAIL_HOST=mail.company.com
TAIGA_EMAIL_PORT=587
TAIGA_EMAIL_USER=taiga@company.com
TAIGA_EMAIL_PASS=somethingsecure
```
```yml
TAIGA_ENABLE_EMAIL=True
TAIGA_EMAIL_FROM=no-reply@company.com
TAIGA_EMAIL_USE_TLS=False
TAIGA_EMAIL_HOST=mail.company.com
TAIGA_EMAIL_PORT=25
TAIGA_EMAIL_USER=taiga@company.com
TAIGA_EMAIL_PASS=somethingsecure
```

### TAIGA_ADMIN_PASSWORD

*Default value*: `123123`

The default administrator password

Examples:
```yml
TAIGA_ADMIN_PASSWORD=somethingverysecure
```

### TAIGA_SSL

*Default value*: `False`

Activate SSL. Remember to enable it in the front client too.

Examples:
```yml
TAIGA_SSL=False
TAIGA_SSL=True
```

### TAIGA_SSL_BY_REVERSE_PROXY

*Default value*: `False`

Activate SSL through a reverse proxy. Remember to enable it in the front client too.

Examples:
```yml
TAIGA_SSL_BY_REVERSE_PROXY=False
TAIGA_SSL_BY_REVERSE_PROXY=True
```

### TAIGA_SECRET_KEY

*Default value*: `'!!!REPLACE-ME-j1598u1J^U*(y251u98u51u5981urf98u2o5uvoiiuzhlit3)!!!'`

Secret key used for encryption.

Examples:
```yml
TAIGA_SECRET_KEY=somethingreallysecureandrandom
```

### TAIGA_DEBUG

*Default value*: `False`

Enable Taiga debug mode.

Examples:
```yml
TAIGA_DEBUG=False
TAIGA_DEBUG=True
```

### TAIGA_TEMPLATE_DEBUG

*Default value*: `False`

Enable Taiga template debug mode.

Examples:
```yml
TAIGA_TEMPLATE_DEBUG=False
TAIGA_TEMPLATE_DEBUG=True
```

### TAIGA_PUBLIC_REGISTER_ENABLED

*Default value*: `False`

Enable Taiga registration.

Examples:
```yml
TAIGA_PUBLIC_REGISTER_ENABLED=False
TAIGA_PUBLIC_REGISTER_ENABLED=True
```

### TAIGA_SITEMAP_ENABLED

*Default value*: `False`

Enable Taiga sitemap.

Examples:
```yml
TAIGA_SITEMAP_ENABLED=False
TAIGA_SITEMAP_ENABLED=True
```

### TAIGA_FEEDBACK_ENABLED

*Default value*: `False`

Enable Taiga feedback. Remember to enable it in the front client too.

Examples:
```yml
TAIGA_FEEDBACK_ENABLED=False
```
```yml
TAIGA_FEEDBACK_ENABLED=True
TAIGA_FEEDBACK_EMAIL=support@taiga.io
```
```
TAIGA_FEEDBACK_ENABLED=True
TAIGA_FEEDBACK_EMAIL=taiga@company.com
```
```yml
TAIGA_FEEDBACK_ENABLED=True
TAIGA_FEEDBACK_EMAIL=contact@company.com
```

### TAIGA_STATS_ENABLED

*Default value*: `False`

Enable Taiga statistics.

Examples:
```yml
TAIGA_STATS_ENABLED=False
TAIGA_STATS_ENABLED=True
```

### TAIGA_IMPORTER_GITHUB_ENABLED

*Default value*: `False`

Enable Taiga [GitHub](https://github.com) importer. Remember to enable it in the front client too. Requires GitHub client ID and secret.

Examples:
```yml
TAIGA_IMPORTER_GITHUB_ENABLED=False
```
```yml
TAIGA_IMPORTER_GITHUB_ENABLED=True
TAIGA_IMPORTER_GITHUB_CLIENT_ID=XXXXXX_get_a_valid_client_id_from_github_XXXXXX
TAIGA_IMPORTER_GITHUB_CLIENT_SECRET=XXXXXX_get_a_valid_client_secret_from_github_XXXXXX
```

### TAIGA_IMPORTER_TRELLO_ENABLED

*Default value*: `False`

Enable Taiga [Trello](https://trello.com/) importer. Remember to enable it in the front client too. Requires Trello API key and secret.

Examples:
```yml
TAIGA_IMPORTER_TRELLO_ENABLED=False
```
```yml
TAIGA_IMPORTER_TRELLO_ENABLED=True
TAIGA_IMPORTER_TRELLO_API_KEY=XXXXXX_get_a_valid_api_key_from_trello_XXXXXX
TAIGA_IMPORTER_TRELLO_API_SECRET=XXXXXX_get_a_valid_secret_key_from_trello_XXXXXX
```

### TAIGA_IMPORTER_JIRA_ENABLED

*Default value*: `False`

Enable Taiga [JIRA](https://www.atlassian.com/software/jira) importer. Remember to enable it in the front client too. Requires JIRA consumer key and valid certificate.

Examples:
```yml
TAIGA_IMPORTER_JIRA_ENABLED=False
```
```yml
TAIGA_IMPORTER_JIRA_ENABLED=True
TAIGA_IMPORTER_JIRA_CONSUMER_KEY=XXXXXX_get_a_valid_consumer_key_from_jira_XXXXXX
TAIGA_IMPORTER_JIRA_CERT=XXXXXX_get_a_valid_cert_from_jira_XXXXXX
TAIGA_IMPORTER_JIRA_PUB_CERT=XXXXXX_get_a_valid_pub_cert_from_jira_XXXXXX
```

### TAIGA_IMPORTER_ASANA_ENABLED

*Default value*: `False`

Enable Taiga [Asana](https://asana.com) importer. Remember to enable it in the front client too. Requires Asana App ID and secret.

Examples:
```yml
TAIGA_IMPORTER_ASANA_ENABLED=False
```
```yml
TAIGA_IMPORTER_ASANA_ENABLED=True
TAIGA_IMPORTER_ASANA_APP_ID=XXXXXX_get_a_valid_app_id_from_asana_XXXXXX
TAIGA_IMPORTER_ASANA_APP_SECRET=XXXXXX_get_a_valid_app_secret_from_asana_XXXXXX
```

### TAIGA_EVENTS_ENABLED

*Default value*: `False`

Enable [Taiga Events](https://github.com/Monogramm/docker-taiga-events). Requires RabbitMQ.

Examples:
```yml
TAIGA_EVENTS_ENABLED=False
```
```yml
TAIGA_EVENTS_ENABLED=True
RABBIT_USER=guest
RABBIT_PASSWORD=guest
RABBIT_HOST=rabbitmq
RABBIT_PORT=5672
```
```
TAIGA_EVENTS_ENABLED=True
RABBIT_USER=taiga
RABBIT_PASSWORD=somethingverysecure
RABBIT_HOST=taiga_rabbitmq
RABBIT_PORT=5672
```

### TAIGA_ASYNC_ENABLED

*Default value*: `False`

Enable Taiga asynchronous mode. Requires Redis, Celery and RabbitMQ.

Examples:
```yml
TAIGA_ASYNC_ENABLED=False
```
```yml
TAIGA_ASYNC_ENABLED=True
RABBIT_USER=guest
RABBIT_PASSWORD=guest
RABBIT_HOST=rabbitmq
RABBIT_PORT=5672
REDIS_HOST=redis
REDIS_PORT=6379
```
```yml
TAIGA_ASYNC_ENABLED=True
RABBIT_USER=taiga
RABBIT_PASSWORD=somethingverysecure
RABBIT_HOST=taiga_rabbitmq
RABBIT_PORT=5672
REDIS_HOST=taiga_redis
REDIS_PORT=6379
```
