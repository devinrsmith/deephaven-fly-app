FROM ghcr.io/devinrsmith/fly-jetty:latest
#FROM deephaven/server:local-build

COPY app.d/ /app.d
