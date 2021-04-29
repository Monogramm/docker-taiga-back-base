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
ARG TAIGA_VERSION=5.5.9

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
        cargo \
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
    ln -s /taiga/local.py "${SOURCE_DIR}/settings/config.py"; \
    sed -i -e 's|cryptography==1.9|cryptography==2.3.1|g' "${SOURCE_DIR}/requirements.txt"; \
    pip install --no-cache-dir -r "${SOURCE_DIR}/requirements.txt"; \
    [ ! -f "${SOURCE_DIR}/requirements-contribs.txt" ] || pip install --no-cache-dir -r "${SOURCE_DIR}/requirements-contribs.txt"

## Runtime environment variables
# Taiga database, front, back, events, email and security properties
ENV BIND_ADDRESS=0.0.0.0 \
    PORT=8001 \
    POSTGRES_DB=taiga \
    POSTGRES_HOST=taigadb \
    POSTGRES_PORT=5432 \
    POSTGRES_USER=taiga \
    POSTGRES_PASSWORD= \
    TAIGA_HOSTNAME=localhost \
    ENABLE_EMAIL=False \
    DEFAULT_FROM_EMAIL= \
    TAIGA_NOTIFICATIONS_INTERVAL=0 \
    EMAIL_USE_TLS=False \
    EMAIL_USE_SSL=False \
    EMAIL_HOST= \
    EMAIL_PORT=587 \
    EMAIL_HOST_USER= \
    EMAIL_HOST_PASSWORD= \
    TAIGA_ADMIN_PASSWORD=123123 \
    TAIGA_SSL=False \
    TAIGA_SSL_BY_REVERSE_PROXY=False \
    TAIGA_SECRET_KEY="!!!REPLACE-ME-j1598u1J^U*(y251u98u51u5981urf98u2o5uvoiiuzhlit3)!!!" \
    TAIGA_DEBUG=False \
    TAIGA_TEMPLATE_DEBUG=False \
    PUBLIC_REGISTER_ENABLED=False \
    FRONT_SITEMAP_ENABLED=False \
    FEEDBACK_ENABLED=False \
    FEEDBACK_EMAIL= \
    STATS_ENABLED=False \
    ENABLE_TELEMETRY=False \
    ENABLE_GITHUB_IMPORTER=False \
    GITHUB_IMPORTER_CLIENT_ID= \
    GITHUB_IMPORTER_CLIENT_SECRET= \
    ENABLE_TRELLO_IMPORTER=False \
    TRELLO_IMPORTER_API_KEY= \
    TRELLO_IMPORTER_SECRET_KEY= \
    ENABLE_JIRA_IMPORTER=False \
    JIRA_IMPORTER_CONSUMER_KEY= \
    JIRA_IMPORTER_CERT= \
    JIRA_IMPORTER_PUB_CERT= \
    ENABLE_ASANA_IMPORTER=False \
    ASANA_IMPORTER_APP_ID= \
    ASANA_IMPORTER_APP_SECRET= \
    EVENTS_ENABLED=False \
    RABBITMQ_VHOST=/taiga \
    RABBITMQ_USER=guest \
    RABBITMQ_PASS=guest \
    RABBITMQ_HOST=rabbitmq \
    RABBITMQ_PORT=5672 \
    CELERY_ENABLED=False \
    REDIS_HOST=redis \
    REDIS_PORT=6379



# TODO Setup Taiga user
# RUN set -ex; \
#     addgroup --gid 999 -S taiga; \
#     adduser --uid 999 -S -D -G taiga taiga; \
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
