help:
	@cat Makefile

build_eyeseg:
	poetry build

build_gpu: build_eyeseg
	DOCKER_BUILDKIT=1 docker build -t olcifer/eyeseg:1.0.2-gpu -f Dockerfile --target gpu ../dist
	# Needed only for distributing images without dockerhub
	#mkdir -p ./dist
	#docker save -o ./dist/docker_eyeseg-1.0.2-gpu.tar olcifer/eyeseg:1.0.2-gpu
	#gzip ./dist/docker_eyeseg-1.0.2-gpu.tar

build_cpu: build_eyeseg
	DOCKER_BUILDKIT=1 docker build --no-cache -t olcifer/eyeseg:1.0.2-cpu -f Dockerfile --target cpu ../dist
	# Needed only for distributing images without dockerhub
	#mkdir -p ./dist
	#docker save -o ./dist/docker_eyeseg-1.0.2-cpu.tar olcifer/eyeseg:1.0.2-cpu
	#gzip ./dist/docker_eyeseg-1.0.2-cpu.tar

build_all: build_gpu build_cpu
