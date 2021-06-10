FROM python:3.6-slim

COPY ./mazars.py /

WORKDIR ./

RUN pip install Flask==1.1.2 &&\
    pip install requests==2.24.0

EXPOSE 3000

CMD ["python", "mazars.py"]