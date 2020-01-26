FROM tensorflow/tensorflow:latest-gpu-py3-jupyter
LABEL Description="Tensorflow 2.0 + Jupyter notebook with additonal packages" Version="1.0"

COPY ./requirements.txt .
COPY ./setup.py .
COPY ./src .
RUN pip3 install -r requirements.txt
