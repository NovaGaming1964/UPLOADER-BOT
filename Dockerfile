FROM debian:11
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-pip wget
    
RUN wget https://raw.githubusercontent.com/NovaGaming1964/UPLOADER-BOT/main/bot.py
RUN wget https://raw.githubusercontent.com/NovaGaming1964/UPLOADER-BOT/main/requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python3","bot.py"]
