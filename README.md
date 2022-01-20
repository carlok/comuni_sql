# SQL per la memorizzazione dei Comuni, delle Province e delle Regioni d’Italia

Partendo dal `CSV` ufficiale ISTAT, si ottengono gli `SQL` necessari.

```
docker build -t carlok/pandas .
docker run -v $PWD:/app -it carlok/pandas wget --no-check-certificate -O comuni.csv https://www.istat.it/storage/codici-unita-amministrative/Elenco-comuni-italiani.csv
docker run -v $PWD:/app -it carlok/pandas python istat.py > insert.sql
```