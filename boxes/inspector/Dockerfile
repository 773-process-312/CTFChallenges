FROM node:8

WORKDIR /usr/src/app

COPY ./app/package*.json ./

RUN apt-get update
RUN apt-get install -y netcat
# For ifconfig, to make life easier for players who are used to that command
RUN apt-get install net-tools

RUN npm install

RUN echo "ctf{my_first_reverse_shell_super1337}" > /root/root.txt

# Bundle app source
COPY ./app/ .

EXPOSE 80

CMD [ "node", "index.js" ]
