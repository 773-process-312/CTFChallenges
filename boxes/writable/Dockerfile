FROM ubuntu:latest

RUN apt-get -y update && \
    apt-get -y install python bash perl nmap socat netcat openssh-server openssh-client whois sudo redis python-pip


RUN pip install bottle glances

COPY ./init.sh /init.sh

RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config

# Configure the user
RUN useradd -m -p `echo "tompassword" | mkpasswd -m sha-512 -s` -s /bin/rbash -d /home/tom/ tom

RUN mkdir -p /home/tom/.ssh/; chown tom /home/tom/.ssh/; chmod 755 /home/tom/.ssh/
COPY ./rbash/.bash_profile /home/tom/.bash_profile
RUN chmod 444 /home/tom/.bash_profile & \
    mkdir -p /home/tom/bin/; \
    ln -s /bin/ls /home/tom/bin/; \
    ln -s /bin/sed /home/tom/bin/sed 

# Add the root script
COPY ./pyexec/pyexec.py /opt/pyexec.py
COPY ./pyexec/requirements.txt /opt/requirements.txt
COPY ./pyexec/etc/jobs.json /etc/jobs.json
RUN pip install -r /opt/requirements.txt; \
    chown root /etc/jobs.json /opt/pyexec.py; \
    chmod 744 /opt/pyexec.py; \
    chmod 444 /etc/jobs.json

# Add the flags
RUN echo "CTF{wait_ssh_can_still_read_that}" > /home/tom/user.txt; \
    chown root /home/tom/user.txt; \
    chmod 444 /home/tom/user.txt; \
    echo "CTF{pysandbox_is_still_broken}" > /root/root.txt; \
    chown root /root/root.txt; \
    chmod 400 /root/root.txt

EXPOSE 22
EXPOSE 6379
EXPOSE 8000

CMD ["sh", "/init.sh"]
