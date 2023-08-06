FROM ubuntu:latest

ARG TAG=alpha

ADD https://github.com/BerentM/zakupy_backend/releases/download/${TAG}/zakupyBackend /pb/zakupyBackend
RUN chmod +x /pb/zakupyBackend

EXPOSE 8000
