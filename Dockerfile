FROM python:3.13-alpine

ARG UID=10001
RUN adduser \
    -D \
    -H \
    -s "/sbin/nologin" \
    -u "${UID}" \
    appuser

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir -p /data && chown -R appuser:appuser /data /app

COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:35050", "--workers", "2", "--worker-tmp-dir", "/tmp", "app:app"]
