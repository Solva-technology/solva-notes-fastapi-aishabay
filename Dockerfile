FROM python:3.12-slim

RUN useradd --create-home --home-dir /app --shell /bin/bash app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements ./requirements

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements/base.txt

COPY . .
USER app

#COPY entrypoint.sh /code/entrypoint.sh
#RUN chmod +x /code/entrypoint.sh

#EXPOSE 8000

#ENTRYPOINT ["/code/entrypoint.sh"]
