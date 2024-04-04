###### ESTAGIO 1 #####
FROM cgr.dev/chainguard/python:latest-dev as building
LABEL maintainer="Magno Alexandre"
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

###### ESTAGIO 2 #####
FROM cgr.dev/chainguard/python:latest
ENV REDIS_HOST redis-server
WORKDIR /app
COPY --from=building /home/nonroot/.local/lib/python3.12/site-packages /home/nonroot/.local/lib/python3.12/site-packages
COPY --from=building /home/nonroot/.local/bin  /home/nonroot/.local/bin
COPY --from=building /app/ .
ENV PATH=$PATH:/home/nonroot/.local/bin
EXPOSE 5000
ENTRYPOINT ["flask"]
CMD [ "run","--host=0.0.0.0" ]
