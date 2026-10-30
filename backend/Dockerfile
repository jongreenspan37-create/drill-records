FROM python:3.14-slim

# Match the host user so files created through the bind mount stay editable
ARG APP_UID=1000
ARG APP_GID=1000

RUN groupadd --gid "$APP_GID" app \
    && useradd --uid "$APP_UID" --gid app --no-create-home app

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
