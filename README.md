# FastAPI-Faust-POC

Building a system of Kafka event consumers using FastAPI and Faust.

## Introduction

fastapi-faust-poc is created to check how FastAPI works with Faust stream processor. I'll be using confluent-kafka and zookeeper for event consumption purposes.

## Installation

I'm using Poetry for package dependency management.

Run `poetry install --no-dev`

If there is an error with the installation of confluent-kafka, then follow [this](https://github.com/confluentinc/confluent-kafka-python/blob/master/INSTALL.md).