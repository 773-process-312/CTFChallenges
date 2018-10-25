FROM ubuntu:latest

RUN apt-get -y update && \
    apt-get -y install python bash perl nmap socat netcat openssh-server openssh-client whois sudo python-pip


COPY ./init.sh /init.sh
COPY ./app/ /app/

RUN pip install -r /app/requirements.txt

RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN useradd -m -p `echo "need_some_help" | mkpasswd -m sha-512 -s` -s /bin/bash clippy 

# Method to root the box is via find having the ablity to execute commands.
RUN echo "clippy ALL=(ALL) NOPASSWD: /usr/bin/find" >> /etc/sudoers

# Add the flags
RUN echo "CTF{quick_maths}" > /home/clippy/user.txt & \
    chown root /home/clippy/user.txt & \
    chmod 444 /home/clippy/user.txt & \
    echo "CTF{sudo_make_me_a_sandwich}" > /root/root.txt & \
    chown root /root/root.txt & \
    chmod 400 /root/root.txt

EXPOSE 22
EXPOSE 5000


CMD ["sh", "/init.sh"]
