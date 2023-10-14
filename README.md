Build the dummy image:

`docker build -t dummy --file dummy.Dockerfile .`

run the dummy container:
`docker run --name dummy42 --env REDIS_HOST=${REDIS_HOST} --env REDIS_PORT=${REDIS_PORT} --env REDIS_QUEUE_NAME=${REDIS_QUEUE_NAME} -- dummy`

Minikube cannot see the local Docker daemon.  Any image sbuilt locally will not be available inside of Minikube.   
instead you need to lift Minikube's daemon into your current shell and build the image so that it exists in the Minikube VM.
https://stackoverflow.com/questions/40144138/pull-a-local-image-to-run-a-pod-in-kubernetes
`eval $(minikube docker-env)`


When creating a configmap from yaml do not use the --fromfile flg, this is for Java style properties files, instead:
`https://stackoverflow.com/questions/60821970/why-k8s-pod-cant-find-key-in-configmap`