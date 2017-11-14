
name=plot3dsurfaces

docker build . -t $name && \
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /mnt/scratch/kitchell/sigularitytest:/output \
    --privileged -t --rm \
    singularityware/docker2singularity \
    $name
