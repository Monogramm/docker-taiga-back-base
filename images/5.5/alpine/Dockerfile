FROM python:3.6-alpine

## Build time environment variables
# specify LANG to ensure python installs locals properly
# fixes benhutchins/docker-taiga-example#4
# ref benhutchins/docker-taiga#15
ENV LANG=C \
    LANG=en_US.UTF-8 \
    LC_TYPE=en_US.UTF-8 \
    SOURCE_DIR=/usr/src/taiga-back \
    WORK_DIR=/usr/src/taiga-back

WORKDIR ${WORK_DIR}

COPY changeadminpasswd.py checkdb.py entrypoint.sh /
COPY docker.py celery_local.py ${WORK_DIR}/settings/
COPY conf/locale.gen /etc/
COPY conf/taiga/local.py /taiga/

# Build version
ARG TAIGA_VERSION=5.5.5

# Get Taiga
ADD https://github.com/taigaio/taiga-back/archive/${TAIGA_VERSION}.tar.gz /tmp/taiga-back-${TAIGA_VERSION}.tar.gz

# Install the packages we need
# Set locale
#    echo "LANG=en_US.UTF-8" > /etc/default/locale; \
#    echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale; \
#    echo "LC_TYPE=en_US.UTF-8" >> /etc/default/locale; \
#    echo "LC_MESSAGES=POSIX" >> /etc/default/locale; \
#    echo "LANGUAGE=en" >> /etc/default/locale; \
# Assure main scripts are executable
# Install Taiga from tag archive
# Setup symbolic links for configuration files
RUN set -ex; \
    apk add --update --no-cache \
        ca-certificates \
        curl \
        gettext \
        gcc \
        g++ \
        git \
        libffi-dev \
        libgcrypt-dev \
        jpeg-dev \
        libxml2-dev \
        libxslt-dev \
        musl-dev \
        openssl-dev \
        postgresql-dev \
        postgresql-libs \
        py3-openssl \
        rsync \
        tar \
        zeromq-dev \
        zlib-dev \
    ; \
    rm -rf /var/cache/apk/*; \
    chmod 755 /entrypoint.sh /checkdb.py /changeadminpasswd.py; \
    mkdir -p "${SOURCE_DIR}"; \
    mkdir -p /tmp/taiga-back; \
    tar xzf "/tmp/taiga-back-${TAIGA_VERSION}.tar.gz" -C /tmp/taiga-back; \
    rm "/tmp/taiga-back-${TAIGA_VERSION}.tar.gz"; \
    cp -r /tmp/taiga-back/taiga-back-${TAIGA_VERSION}/* "${SOURCE_DIR}"; \
    rm -rf /tmp/taiga-back; \
    ln -s /taiga/local.py "${SOURCE_DIR}/settings/local.py"; \
    sed -i -e 's|cryptography==1.9|cryptography==2.3.1|g' "${SOURCE_DIR}/requirements.txt"; \
    pip install --no-cache-dir -r "${SOURCE_DIR}/requirements.txt"

## Runtime environment variables
# Taiga database, front, back, events, email and security properties
ENV BIND_ADDRESS=0.0.0.0 \
    PORT=8001 \
    TAIGA_DB_NAME=taiga \
    TAIGA_DB_HOST=taigadb \
    TAIGA_DB_USER=taiga \
    TAIGA_DB_PASSWORD= \
    TAIGA_HOSTNAME=localhost \
    TAIGA_ENABLE_EMAIL=False \
    TAIGA_EMAIL_FROM= \
    TAIGA_NOTIFICATIONS_INTERVAL=0 \
    TAIGA_EMAIL_USE_TLS=False \
    TAIGA_EMAIL_HOST= \
    TAIGA_EMAIL_PORT= \
    TAIGA_EMAIL_USER= \
    TAIGA_EMAIL_PASS= \
    TAIGA_ADMIN_PASSWORD=123123 \
    TAIGA_SSL=False \
    TAIGA_SSL_BY_REVERSE_PROXY=False \
    TAIGA_SECRET_KEY="!!!REPLACE-ME-j1598u1J^U*(y251u98u51u5981urf98u2o5uvoiiuzhlit3)!!!" \
    TAIGA_DEBUG=False \
    TAIGA_TEMPLATE_DEBUG=False \
    TAIGA_PUBLIC_REGISTER_ENABLED=False \
    TAIGA_SITEMAP_ENABLED=False \
    TAIGA_FEEDBACK_ENABLED=False \
    TAIGA_FEEDBACK_EMAIL= \
    TAIGA_STATS_ENABLED=False \
    TAIGA_IMPORTER_GITHUB_ENABLED=False \
    TAIGA_IMPORTER_GITHUB_CLIENT_ID= \
    TAIGA_IMPORTER_GITHUB_CLIENT_SECRET= \
    TAIGA_IMPORTER_TRELLO_ENABLED=False \
    TAIGA_IMPORTER_TRELLO_API_KEY= \
    TAIGA_IMPORTER_TRELLO_API_SECRET= \
    TAIGA_IMPORTER_JIRA_ENABLED=False \
    TAIGA_IMPORTER_JIRA_CONSUMER_KEY= \
    TAIGA_IMPORTER_JIRA_CERT= \
    TAIGA_IMPORTER_JIRA_PUB_CERT= \
    TAIGA_IMPORTER_ASANA_ENABLED=False \
    TAIGA_IMPORTER_ASANA_APP_ID= \
    TAIGA_IMPORTER_ASANA_APP_SECRET= \
    TAIGA_EVENTS_ENABLED=False \
    RABBIT_VHOST=/ \
    RABBIT_USER=guest \
    RABBIT_PASSWORD=guest \
    RABBIT_HOST=rabbitmq \
    RABBIT_PORT=5672 \
    TAIGA_ASYNC_ENABLED=False \
    REDIS_HOST=redis \
    REDIS_PORT=6379

# TODO Setup Taiga user
# RUN set -ex; \
#     addgroup -S taiga; \
#     adduser -S -D -G taiga taiga; \
#     chown -R taiga:taiga "${SOURCE_DIR}/"* "${WORK_DIR}/"*
# 
# USER taiga

VOLUME /taiga ${WORK_DIR}

ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "taiga.wsgi"]

ARG VCS_REF
ARG BUILD_DATE

# Container labels (http://label-schema.org/)
# Container annotations (https://github.com/opencontainers/image-spec)
LABEL maintainer="Monogramm Maintainers <opensource at monogramm dot io>" \
      product="Taiga Backend" \
      version=$TAIGA_VERSION \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/Monogramm/docker-taiga-back-base" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Taiga Backend" \
      org.label-schema.description="Agile project management platform." \
      org.label-schema.url="http://taiga.io/" \
      org.label-schema.vendor="Taiga Agile, LLC" \
      org.label-schema.version=$TAIGA_VERSION \
      org.label-schema.schema-version="1.0" \
      org.opencontainers.image.revision=$VCS_REF \
      org.opencontainers.image.source="https://github.com/Monogramm/docker-taiga-back-base" \
      org.opencontainers.image.created=$BUILD_DATE \
      org.opencontainers.image.title="Taiga Backend" \
      org.opencontainers.image.description="Agile project management platform." \
      org.opencontainers.image.url="http://taiga.io/" \
      org.opencontainers.image.vendor="Taiga Agile, LLC" \
      org.opencontainers.image.version=$TAIGA_VERSION \
      org.opencontainers.image.authors="Kaleidos <https://kaleidos.net/>"
