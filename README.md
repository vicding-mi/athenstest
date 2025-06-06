# Hackathon in Athens 2025 for OSTrails

## Introduction
This repository is the hackathon day of OSTrails 2025. 

The purpose is to demonstrate the possibility of building a pipeline to fetch records from Solr, 
transform them according to a given template, and assess the transformed json files 
using [SKG-IF OpenAPI YAML](https://gitlab.esrf.fr/smis/ostrails/-/raw/main/skg-if-api/skg-if-api.yaml). 
And workshop description is [Hackathon doc](https://docs.google.com/document/d/1t7b7h28UTtM56Sda4NGJIp0hnQfGbcVVGn12fny9wfI/edit?tab=t.0#heading=h.snl8q52175g). 

## How to run 

Special note: there are now 2 ways to use this repository.

1. Run as a service - which means you setup a stack and keep it running. In this case, you have to comment out line 837 ~ 850 in 
   `app.py` and rebuild the docker image and uncomment line 853 ~ 868.
2. Run in github actions - which means you run the pipeline in a github action. In this case, `app.py` is ready, as well as the docker image.

### First way - run as a service
```shell
docker compose up
```
1. From browser visit http://url/38000/fetchall to fetch all records from Solr.
2. From browser visit http://url/38000/initdb to initialize the database.
3. From browser visit http://url/38000/transform to transform the fetched records.

Link to all the products: http://url:38000/products
Link to single product: http://url:38000/products/{id} or http://url:38000/products/random to get a random product.

## How to validate
Go to http://url:34010/products or http://url:34010/products/{id} to see the results.


## 
url to dataset http://n-10-27-6-240.diginfra.net:38000/products/https_58__47__47_archief.nl_47_id_47_dataset_47_toegang_47_2.16.131
url to test http://n-10-27-6-240.diginfra.net:34010/products/https_58__47__47_archief.nl_47_id_47_dataset_47_toegang_47_2.16.131

### Second way - run in github actions
The json files should be put in the `sample_data` folder. Modify them, commit and push to the repository.
The action will only be fired when you push json files. 

