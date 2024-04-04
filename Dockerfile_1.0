FROM ubuntu:20.04
LABEL maintainer="magno alexandre"
WORKDIR /app
COPY . /app
RUN \
apt update && \
apt install -y pip && \
pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV REDIS_HOST redis-server
ENTRYPOINT ["flask"]
CMD ["run","--host=0.0.0.0"]
