#!/bin/sh

. ../jenkins-common.sh

mkdir $VOL_BASE_DIR/bsc-tester
cp sccplite/BSC_Tests.cfg $VOL_BASE_DIR/bsc-tester/

mkdir $VOL_BASE_DIR/bsc
cp sccplite/osmo-bsc.cfg $VOL_BASE_DIR/bsc/

network_create 172.18.11.0/24

echo Starting container with BSC
docker run	--rm \
		--network $NET_NAME --ip 172.18.11.20 \
		-v $VOL_BASE_DIR/bsc:/data \
		--name ${BUILD_TAG}-bsc -d \
		$REPO_USER/osmo-bsc-master

for i in `seq 0 2`; do
	echo Starting container with OML for BTS$i
	docker run	--rm \
			--network $NET_NAME --ip 172.18.11.10$i \
			--name ${BUILD_TAG}-bts$i -d \
			$REPO_USER/osmo-bts-master /usr/local/bin/respawn.sh osmo-bts-omldummy 172.18.11.20 $((i + 1234)) 1
done

echo Starting container with BSC testsuite
docker run	--rm \
		--network $NET_NAME --ip 172.18.11.203 \
		-e "TTCN3_PCAP_PATH=/data" \
		-v $VOL_BASE_DIR/bsc-tester:/data \
		--name ${BUILD_TAG}-ttcn3-bsc-test \
		$REPO_USER/ttcn3-bsc-test

echo Stopping containers
for i in `seq 0 2`; do
	docker container kill ${BUILD_TAG}-bts$i
done
docker container kill ${BUILD_TAG}-bsc

network_remove
collect_logs