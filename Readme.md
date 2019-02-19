Ikamai Deployer v1.1

di versi iki, runner ning gitlab

name='deployer-v1.1-2'
git init
git remote add kopet https://ikamai:kopet1234@gitlab.com/ikamai/tmp.git
git fetch
git branch $name
git checkout $name
git add .
git commit -m "push:$name"
git push -u kopet $name
echo 'success'


docker run -it --rm \
  --name swarmpit-installer \
  -p 8080:888 \
  --volume /var/run/docker.sock:/var/run/docker.sock \
swarmpit/install:1.6

docker run \
    -v $PWD/:/home/foo/upload \
    -p 2222:22 atmoz/sftp \
    foo:pass:1001

docker run -d -p 2222:22 -v /secrets/id_rsa.pub:/root/.ssh/authorized_keys -v /home:/data/ docker.io/panubo/sshd


docker run --rm \
--publish=2222:22 \
--env ROOT_PASSWORD=kopet1234 \
hermsi/alpine-sshd

docker swarm init
docker swarm leave
docker swarm join --token SWMTKN-1-3bd36kollej2z5ub6iw4pl6zezmv2paz1egiu9w10pe53lnztb-8iqnpfh8j01g7e09bpuilize6 live.koo.pet:2377

docker node ls
docker swarm join --token SWMTKN-1-31kxy4kas4el30una4xvmq9c5g1azvz7zjatfw1clf0elixps3-9nfrjhmr6il1ni90mqivhmwky 0.tcp.ngrok.io:15368

docker login --username rizoa --password kopet1234
docker pull rizoa/ikamai:kautsarbot.v1.posting

docker service create --replicas 50 --name posting rizoa/ikamai:kautsarbot.v1.posting
docker service rm botkeeper
docker service rm domainmon
docker service rm pinger
docker service rm ngapi
docker service ls

docker service create --replicas 1 --name pinger rizoa/ikamai:kautsarbot.v1.pinger
docker service create --replicas 1 --name domainmon rizoa/ikamai:kautsarbot.v1.domainmon
docker service create --replicas 4 --name botkeeper rizoa/ikamai:kautsarbot.v1.botkeeper
docker service create --replicas 20 --name ngapi rizoa/ikamai:kautsarbot.v1.ngapi

docker pull rizoa/ikamai:kautsarbot.v1.pinger
docker pull rizoa/ikamai:kautsarbot.v1.botkeeper
docker pull rizoa/ikamai:kautsarbot.v1.domainmon
docker pull rizoa/ikamai:kautsarbot.v1.ngapi


