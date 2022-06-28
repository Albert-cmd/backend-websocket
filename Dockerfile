FROM continuumio/miniconda:latest

WORKDIR ./

COPY ./ ./

RUN chmod +x boot.sh

RUN Conda env create -f environment.yml

RUN echo "source activate backend-websocket" &gt; ~/.bashrc
ENV PATH /opt/conda/envs/backend-websocket/bin:$PATH

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]