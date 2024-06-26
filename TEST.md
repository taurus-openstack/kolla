# Example

- kolla build on localhost (required, registry login)

```sh
python ./kolla/cmd/build.py octavia \
    --config-file=./kolla-build.conf --base=ubuntu \
    --registry=public.ecr.aws/p6g9k8e4 \
    --namespace=taurus-kolla \
    --base-arch=x86_64 --platform=linux/amd64 \
    --tag=2024.1-taurus \
    --push
```

- build spec example

```yaml
version: 0.2

phases:
  install:
    commands:
      - echo "Install kolla packages"
      - python3 --version
      - pip3 install -r requirements.txt
      - pip3 install docker packaging
  pre_build:
    commands:
      - echo "Check versions and ecr login"
      - echo "Target project is, $OS_PROJECT"
      - docker --version
      - jq --version
      - aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin $OS_REGISTRY_URL
      - OS_REGISTRY_NAMESPACE=taurus-kolla
      - PUSH_TAG=$OS_RELEASE-$OS_CUSTOM_TAG
  build:
    commands:
      - >
        python3 ./kolla/cmd/build.py $OS_PROJECT \
            --config-file=./kolla-build.conf --base=ubuntu \
            --base-image=$OS_REGISTRY_URL/ubuntu \
            --base-tag=22.04 \
            --base-arch=x86_64 --platform=linux/amd64 \
            --registry="" \
            --namespace=$OS_REGISTRY_NAMESPACE \
            --tag=$PUSH_TAG \
            --skip-existing
  post_build:
    commands:
      - echo "Push and remove untagged images"
      - >
        docker images --format '{{.Repository}}:{{.Tag}}' | grep $PUSH_TAG | grep -v $OS_REGISTRY_URL | while read -r image; do
            
            repo_name="${image%:*}"  # Extract repository name
            if ! aws ecr-public describe-repositories --repository-names "$repo_name" --region us-east-1 > /dev/null 2>&1; then
                echo "Repository $repo_name does not exist. Creating..."
                aws ecr-public create-repository --repository-name "$repo_name" --region us-east-1
            else
                echo "Repository $repo_name already exists."
            fi
            
            image_version="$OS_REGISTRY_URL/$image"
            docker tag "$image" "$image_version"
            docker push "$image_version"
            
            image_latest="$OS_REGISTRY_URL/$repo_name:latest"
            docker tag "$image" "$image_latest"
            docker push "$image_latest"
            
            image_list=$(aws ecr-public describe-images \
              --repository-name $repo_name \
              --region us-east-1 | jq -c .imageDetails)
            
            untagged_images=$(echo "$image_list" | jq -c 'map(select(has("imageTags") | not))')

            target_digests=$(echo "$untagged_images" | jq -r '[.[] | {imageDigest}] | .[] | @text "imageDigest=\(.imageDigest)"')
            
            if [ -n "$target_digests" ]; then
                aws ecr-public batch-delete-image --repository-name "$repo_name" --image-ids $target_digests --region us-east-1
            fi
        done
      - echo "Confirm kolla images"
      - docker images
```
