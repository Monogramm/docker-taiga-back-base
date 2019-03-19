
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

:construction: **This container is still in development!**

This image was inspired by [ajira86/docker-taiga](https://github.com/ajira86/docker-taiga) which is a fork of [benhutchins/docker-taiga](https://github.com/benhutchins/docker-taiga).

## What is Taiga?

Taiga is a project management platform for startups and agile developers & designers who want a simple, beautiful tool that makes work truly enjoyable.

> [taiga.io](https://taiga.io)

## Build Docker image

To generate docker images from the template, execute `update.sh` script.

Install Docker and then run `docker build -t docker-taiga-back-base images/VARIANT/VERSION` to build the image for the variant and version you need.

You can also build all images by running `update.sh build`.

## Auto configuration via environment variables

The Taiga image supports auto configuration via environment variables. You can preconfigure nearly everything that is available in `local.py`.

See [local.py.example](https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example) and [docker-settings.py](https://github.com/Monogramm/docker-taiga-back-base/blob/master/docker-settings.py) for more details on configuration.


### TAIGA_DB_NAME

*Default value*: `taiga`

Your database name (REQUIRED)

Examples:
```
TAIGA_DB_NAME=taiga
TAIGA_DB_NAME=taigadb
```

### TAIGA_DB_HOST

*Default value*: `taigadb`

Your database hostname (REQUIRED)

Examples:
```
TAIGA_DB_HOST=taigadb
TAIGA_DB_HOST=taigadb.company.com
```

### TAIGA_DB_USER

*Default value*: `taiga`

Your database user (REQUIRED)

Examples:
```
TAIGA_DB_USER=taiga
TAIGA_DB_USER=taigadb
```

### TAIGA_DB_PASSWORD

*Default value*: `''`

Your database user passsword (REQUIRED)

Examples:
```
TAIGA_DB_PASSWORD=somethingsecure
```

### TAIGA_HOSTNAME

*Default value*: `localhost`

Your service hostname (REQUIRED)

Examples:
```
TAIGA_HOSTNAME=localhost
TAIGA_HOSTNAME=taiga.company.com
```

### TAIGA_ENABLE_EMAIL

*Default value*: `False`

Enable email server configuration

Examples:
```
TAIGA_ENABLE_EMAIL=False
TAIGA_ENABLE_EMAIL=True
```

### TAIGA_EMAIL_FROM

*Default value*: ``

The default 'From' email

Examples:
```
TAIGA_EMAIL_FROM=no-reply@company.com
```

### TAIGA_EMAIL_USE_TLS

*Default value*: `False`

Use STARTTLS to connect email server

Examples:
```
TAIGA_EMAIL_USE_TLS=False
TAIGA_EMAIL_USE_TLS=True
```

### TAIGA_EMAIL_HOST

*Default value*: `''`

The email server hostname

Examples:
```
TAIGA_EMAIL_HOST=mail.company.com
TAIGA_EMAIL_HOST=smtp.gmail.com
```

### TAIGA_EMAIL_PORT

*Default value*: `''`

The email server port

Examples:
```
TAIGA_EMAIL_PORT=25
TAIGA_EMAIL_PORT=465
TAIGA_EMAIL_PORT=587
```

### TAIGA_EMAIL_USER

*Default value*: `''`

The email server user

Examples:
```
TAIGA_EMAIL_USER=taiga@company.com
```

### TAIGA_EMAIL_PASS

*Default value*: `''`

The email server user passsword

Examples:
```
TAIGA_EMAIL_PASS=somethingsecure
```

### TAIGA_ADMIN_PASSWORD

*Default value*: `123123`

The default administrator password

Examples:
```
TAIGA_ADMIN_PASSWORD=somethingverysecure
```

### TAIGA_SSL

*Default value*: `False`

Activate SSL.

Examples:
```
TAIGA_SSL=False
TAIGA_SSL=True
```

### TAIGA_SSL_BY_REVERSE_PROXY

*Default value*: `False`

Activate SSL through a reverse proxy.

Examples:
```
TAIGA_SSL_BY_REVERSE_PROXY=False
TAIGA_SSL_BY_REVERSE_PROXY=True
```

### TAIGA_SECRET_KEY

*Default value*: `'!!!REPLACE-ME-j1598u1J^U*(y251u98u51u5981urf98u2o5uvoiiuzhlit3)!!!'`

Secret key used for encryption.

Examples:
```
TAIGA_SECRET_KEY=somethingreallysecureandrandom
```

### TAIGA_DEBUG

*Default value*: `False`

Enable Taiga backend debug mode.

Examples:
```
TAIGA_DEBUG=false
TAIGA_DEBUG=true
```

### TAIGA_TEMPLATE_DEBUG

*Default value*: `False`

Enable Taiga backend template debug mode.

Examples:
```
TAIGA_TEMPLATE_DEBUG=false
TAIGA_TEMPLATE_DEBUG=true
TAIGA_TEMPLATE_DEBUG=''
```

### TAIGA_PUBLIC_REGISTER_ENABLED

*Default value*: `False`

Enable Taiga backend registration.

Examples:
```
TAIGA_PUBLIC_REGISTER_ENABLED=False
TAIGA_PUBLIC_REGISTER_ENABLED=True
```
