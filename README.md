# Hackathon in Athens 2025 for OSTrails

## Introduction
This repository is the hackathon day of OSTrails 2025. 

The purpose is to demonstrate the possibility of building a pipeline to fetch records from Solr, 
transform them according to a given template, and assess the transformed json files 
using [SKG-IF OpenAPI YAML](https://docs.google.com/document/d/1t7b7h28UTtM56Sda4NGJIp0hnQfGbcVVGn12fny9wfI/edit?tab=t.0#heading=h.snl8q52175g). 

## How to run 
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