FROM python:3.8

RUN apt-get update && apt -y install openssh-server

RUN useradd pwned && mkdir -p /home/pwned/app && mkdir -p /var/run/sshd
WORKDIR /home/pwned/app

COPY ./src ./
RUN mv run.sh /usr/bin/run.sh && chmod +x /usr/bin/run.sh
RUN ssh-keygen -A && mkdir /home/pwned/.ssh/
RUN pip install -r requirements.txt

RUN cat /dev/urandom | head | sha1sum | cut -d " " -f 1 > jwt.secret

RUN PASSWD=$(cat /dev/urandom | head | sha1sum | cut -d " " -f 1) && echo "$PASSWD" > pass.txt && echo "pwned:$PASSWD" | chpasswd

EXPOSE 5000
EXPOSE 22

ENTRYPOINT ["/bin/bash", "-c", "/usr/sbin/sshd && /usr/bin/run.sh"]
