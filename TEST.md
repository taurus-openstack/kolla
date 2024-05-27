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
