
FROM ubuntu:latest


WORKDIR /app


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    unzip && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get install make

RUN python3 -m venv /app/pyenv


RUN /app/pyenv/bin/pip install --upgrade pip


COPY requirements.txt /app/requirements.txt


RUN /app/pyenv/bin/pip install -r /app/requirements.txt


COPY . /app/

RUN unzip model.pkl.zip -d temp_dir && mkdir -p artifacts && cp -r temp_dir/* artifacts/ && rm -rf temp_dir

RUN cd artifacts && ls

RUN export STREAMLIT_BROWSER_GATHERUSAGESTATS=false

CMD ["sh", "-c", "tail -f /dev/null"]