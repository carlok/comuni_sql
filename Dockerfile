FROM python:3.10.2-bullseye
WORKDIR /app

RUN apt-get install wget
RUN pip install pandas

# docker build -t carlok/pandas .
# docker run -v $PWD:/app -it carlok/pandas wget --no-check-certificate -O comuni.csv https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv
# docker run -v $PWD:/app -it carlok/pandas python istat.py > insert.sql