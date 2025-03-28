FROM python:3.13-alpine
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

EXPOSE 5000
COPY . .
# TODO: migrations?
CMD ["flask", "run"]

