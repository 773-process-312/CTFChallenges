FROM ubuntu:latest

RUN apt-get -y update && \
    apt-get -y install python bash perl nmap socat netcat openssh-server openssh-client whois sudo


COPY ./init.sh /init.sh

RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN useradd -m -p `echo "ReallySecurePassword" | mkpasswd -m sha-512 -s` -s /bin/bash ctf 

COPY ./.bash_history /home/ctf/.bash_history

RUN chown root /home/ctf/.bash_history && \
    chmod 444 /home/ctf/.bash_history

EXPOSE 22

CMD ["sh", "/init.sh"]
