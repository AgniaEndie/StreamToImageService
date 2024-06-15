FROM python:3.12-slim
LABEL authors="agniaendie"

COPY /src /tmp
WORKDIR /src
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "StreamToImageService.py"]