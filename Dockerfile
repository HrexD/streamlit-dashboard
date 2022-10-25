FROM python:3.10.7

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/* 

RUN git clone https://github.com/HrexD/DataAnalyse/tree/main/StreamlitProject

EXPOSE 8501

RUN pip3 install -r requirement.txt

ENTRYPOINT [ "streamlit", "run", "streamlit.py" ]

CMD streamlit run streamlit.py