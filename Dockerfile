FROM H1M4N5HU0P/MAFIA-USERBOT:latest

#clonning repo 
RUN git clone https://github.com/H1M4N5HU0P/L/MAFIA-USERBOT.git/root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["bash","startup.sh"]
