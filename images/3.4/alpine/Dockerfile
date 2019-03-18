FROM python:alpine

LABEL maintainer="Mathieu BRUNOT <mathieu.brunot at monogramm dot io>"

# Taiga database, front, events, email and security properties
ENV TAIGA_VERSION=3.4.5 \
    TAIGA_DB_NAME='' \
    TAIGA_DB_HOST='' \
    TAIGA_DB_USER='' \
    TAIGA_DB_PASSWORD='' \
    TAIGA_HOSTNAME=localhost \
	TAIGA_SSL=False \
    TAIGA_SSL_BY_REVERSE_PROXY=False \
    RABBIT_HOST=rabbit \
    RABBIT_PORT='' \
    REDIS_HOST=redis \
    REDIS_PORT='' \
    TAIGA_ENABLE_EMAIL=False \
    TAIGA_EMAIL_FROM='' \
    TAIGA_EMAIL_USE_TLS=False \
    TAIGA_EMAIL_HOST='' \
    TAIGA_EMAIL_PORT='' \
    TAIGA_EMAIL_USER='' \
    TAIGA_EMAIL_PASS='' \
    TAIGA_SECRET_KEY="!!!REPLACE-ME-j1598u1J^U*(y251u98u51u5981urf98u2o5uvoiiuzhlit3)!!!" \
    TAIGA_ADMIN_PASSWORD=

EXPOSE 8000

VOLUME /taiga /usr/src/taiga-back/media

COPY checkdb.py entrypoint.sh /
COPY settings.py /usr/src/taiga-back/settings/docker.py
COPY conf/locale.gen /etc/locale.gen
COPY conf/taiga/local.py /taiga/local.py

# Get Taiga
ADD https://github.com/taigaio/taiga-back/archive/${TAIGA_VERSION}.tar.gz /tmp/taiga-back-${TAIGA_VERSION}.tar.gz

WORKDIR /usr/src/taiga-back

# specify LANG to ensure python installs locals properly
# fixes benhutchins/docker-taiga-example#4
# ref benhutchins/docker-taiga#15
ENV LANG=C

# Install the packages we need
# Set locale
#    echo "LANG=en_US.UTF-8" >> /etc/default/locale; \
#    echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale; \
#    echo "LC_TYPE=en_US.UTF-8" >> /etc/default/locale; \
#    echo "LC_MESSAGES=POSIX" >> /etc/default/locale; \
#    echo "LANGUAGE=en" >> /etc/default/locale; \
# Assure main scripts are executable
# Install Taiga from tag archive
# Setup symbolic links for configuration files
RUN set -ex; \
    apk add --no-cache \
        ca-certificates \
        gettext \
        git \
        libgcrypt-dev \
        libxml2-dev \
        libxslt-dev \
        postgresql-libs \
        python-dev \
        tar \
    ; \
	apk add --no-cache --virtual .build-deps \
        libffi-dev \
		gcc \
        musl-dev \
        openssl-dev \
        postgresql-dev \
	; \
    chmod 755 /entrypoint.sh /checkdb.py; \
    mkdir -p /tmp/taiga-back; \
	tar xzf /tmp/taiga-back-${TAIGA_VERSION}.tar.gz -C /tmp/taiga-back; \
	rm /tmp/taiga-back-${TAIGA_VERSION}.tar.gz; \
	mkdir -p /usr/src/taiga-back; \
	cp -r /tmp/taiga-back/taiga-back-${TAIGA_VERSION}/* /usr/src/taiga-back; \
	rm -rf /tmp/taiga-back; \
	ln -s /taiga/local.py /usr/src/taiga-back/settings/local.py; \
    pip install --no-cache-dir -r requirements.txt; \
	apk --purge del .build-deps

#ENV LANG=en_US.UTF-8 \
#    LC_TYPE=en_US.UTF-8
#RUN set -ex; \
#    locale-gen en_US.UTF-8 && locale -a

RUN set -ex; \
    python manage.py collectstatic --noinput

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "-w 3", "-t 60", "--pythonpath=.", "-b 127.0.0.1:8000", "taiga.wsgi"]
