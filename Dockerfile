FROM python:3.8.13-slim-buster

RUN mkdir -p /app
COPY . fast_api.py /app/
WORKDIR /app
RUN pip install -r Requirements.txt
EXPOSE 8080
CMD [ "fast_api.py" ]
ENTRYPOINT [ "python" ]