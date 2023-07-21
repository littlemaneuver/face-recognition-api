FROM animcogn/face_recognition:cpu AS app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

ARG FLASK_DEBUG="false"
ENV FLASK_DEBUG="${FLASK_DEBUG}" \
    FLASK_APP="app.main" \
    FLASK_SKIP_DOTENV="true" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="." \
    PATH="${PATH}:/home/python/.local/bin"

COPY . /app
WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "-c", "python:config.gunicorn", "app.main:create_app()"]
