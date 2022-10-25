FROM python:3.10.7

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git  

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "streamlit.py", "--server.port=8501" "--server.adress=0.0.0.0" ]

CMD streamlit run streamlit.py