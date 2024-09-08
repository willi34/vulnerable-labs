FROM node:14

RUN apt-get update && apt-get install -y openssh-server supervisor

RUN useradd pwned && mkdir -p /home/pwned/app && mkdir -p /var/run/sshd
WORKDIR /home/pwned/app

COPY ./src ./ 
RUN ssh-keygen -A && mkdir /home/pwned/.ssh/
RUN PASSPHRASE=$(tr -dc '0-9' < /dev/urandom | head -c 3) && ssh-keygen -t rsa -f ../.ssh/id_rsa -N $PASSPHRASE
RUN PASSWD=$(cat /dev/urandom | head | sha1sum | cut -d " " -f 1) && echo "pwned:$PASSWD" | chpasswd
RUN cp /home/pwned/.ssh/id_rsa.pub /home/pwned/.ssh/authorized_keys
RUN npm install

COPY supervisor.conf /etc/supervisor/conf.d/supervisor.conf
EXPOSE 3000 22


ENTRYPOINT ["/usr/bin/supervisord"]
