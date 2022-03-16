# Sandbox-Fastapi

This project exists as a sandbox for me to experiment a service template built around fastapi

## Key Features
* Structed logging via loguru and hooks to have uvicorn use loguru
* Migrations via aerich
* Async ORM with Pydantic integration via Tortoise-orm
* Small multi stage docker builds
* Code Quality enforcement via flake8

## Requirements
* python 3.10+ 
* poetry
* postrgesql 
* docker

## Setup
1. poetry install
2. poetry shell
3. ./run_dev.sh