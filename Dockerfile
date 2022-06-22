FROM ghcr.io/devinrsmith/fly-jetty:latest
#FROM deephaven/server:local-build

ADD https://github.com/chrislusf/seaweedfs/releases/download/3.12/linux_amd64.tar.gz .

RUN set -eux; \
    tar xzvf linux_amd64.tar.gz; \
    rm linux_amd64.tar.gz; \
    mv weed /sbin/mount.weed; \
    mkdir /mnt/deephaven; \
    echo "fuse /mnt/deephaven weed filer=deepseaweed.internal:8888,filer.path=/,readOnly=true 0 0" > /etc/fstab

# TODO: the amove /etf/fstab doesn't seem to auto-run in fly.io
# In the meantime, we've customized the entrypoint script to call `mount -a`, but we should prefer to have a better way to do it.
# https://github.com/deephaven/deephaven-core/discussions/1105

COPY app.d/ /app.d
