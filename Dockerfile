FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

LABEL Description="Tensorflow 2.0 + Jupyter notebook with additonal packages" Version="1.0"

COPY ./requirements.txt
RUN pip install -r requrements.txt .