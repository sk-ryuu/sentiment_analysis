# Teiki-ai

## Setup

Install Nix:
```bash
bash <(curl -L https://nixos.org/nix/install)
```

## Run

```bash
nix-shell
```

# Teiki-ai

## Open dev environment

1. Run docker image

```bash
docker run -it --net=host --runtime nvidia --name teiki-dev -p 8000:8000 --gpus all -v $(pwd):/root/teiki-ai -v /tmp/.X11-unix/:/tmp/.X11-unix -e DISPLAY=$DISPLAY teiki-ai:0.0.1

or

docker start teiki-dev
docker exec -it teiki-dev bash

or

nix-shell
```

2. Run API server

```bash
gunicorn main:app --certfile cert.pem --workers 1 --keyfile key.pem --bind 0.0.0.0:8000
```

3. `curl` command

```bash
curl -X POST -k \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode text="Shinka Network builds self-optimising & self-governing networks for diverse agents to co-evolve. Each agent focuses on their fields of expertise and leaves the rest for network collaboration." \
    https://10.10.2.150:8001/keyword-extraction
curl -X POST -k -F file=@CardanoCatalyst-Nunet.raw https://10.10.2.150:8001/keyword-extraction

curl -X POST -k \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode text="Shinka Network builds self-optimising & self-governing networks for diverse agents to co-evolve. Each agent focuses on their fields of expertise and leaves the rest for network collaboration." \
    https://10.10.2.150:8001/sentiment-analysis
curl -X POST -k -F file=@CardanoCatalyst-Nunet.raw https://10.10.2.150:8001/sentiment-analysis

curl -X POST -k \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode text="Shinka Network builds self-optimising & self-governing networks for diverse agents to co-evolve. Each agent focuses on their fields of expertise and leaves the rest for network collaboration." \
    https://10.10.2.150:8001/text-summarization
curl -X POST -k -F file=@CardanoCatalyst-Nunet.raw https://10.10.2.150:8001/text-summarization

curl -X POST -k \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode text="Shinka Network builds self-optimising & self-governing networks for diverse agents to co-evolve. Each agent focuses on their fields of expertise and leaves the rest for network collaboration." \
    https://10.10.2.150:8001/logo-generation \
    --output logo.jpg
curl -X POST -k -F file=@CardanoCatalyst-Nunet.raw https://10.10.2.150:8001/logo-generation

curl -X POST -k \
    --header "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode text="Shinka Network builds self-optimising & self-governing networks for diverse agents to co-evolve. Each agent focuses on their fields of expertise and leaves the rest for network collaboration." \
    https://10.10.2.150:8001/name-generation
curl -X POST -k -F file=@CardanoCatalyst-Nunet.raw https://10.10.2.150:8001/name-generation
```

## Build docker

```bash
docker compose build
```
