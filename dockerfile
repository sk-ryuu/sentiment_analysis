FROM nvidia/cuda:11.6.0-cudnn8-devel-ubuntu20.04
ENV DEBIAN_FRONTEND noninteractive

RUN echo "export PATH=/usr/local/cuda/bin:\$PATH" >> ~/.bashrc
RUN echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/TensorRT/lib:/usr/local/cuda/extras/CUPTI/lib64:\$LD_LIBRARY_PATH" >> ~/.bashrc

COPY ./requirements.txt /root/

WORKDIR /root
RUN apt update && \
    # apt upgrade -y && \
    apt install --assume-yes software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update && apt install --assume-yes python3.9 python3.9-dev python3-pip && \
    ln -sf /usr/bin/python3.9 /usr/bin/python3 && \
    ln -sf /usr/bin/python3 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip && \
    apt install --assume-yes git tree wget unzip htop unzip nano python-dev vim

RUN python3 -m pip install -U setuptools && \
    python3 -m pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu116 && \
    python3 -c "from transformers import AutoModelForSequenceClassification, AutoTokenizer; MODEL = 'cardiffnlp/twitter-roberta-base-sentiment'; tokenizer = AutoTokenizer.from_pretrained(MODEL); model = AutoModelForSequenceClassification.from_pretrained(MODEL)"
COPY . /root/teiki-ai

WORKDIR /root/teiki-ai
# CMD ["gunicorn", "main:app", "--workers", "4", "--certfile", "cert.pem", "--keyfile", "key.pem", "--bind", "0.0.0.0:8000"]
