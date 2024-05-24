python ./tools/build.py --config-file=./etc/kolla/kolla-build.conf --base ubuntu --tag 2024.1-custom octavia

docker tag kolla/octavia-api:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-api:20240524.1
docker tag kolla/octavia-driver-agent:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-driver-agent:20240524.1
docker tag kolla/octavia-health-manager:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-health-manager:20240524.1
docker tag kolla/octavia-worker:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-worker:20240524.1
docker tag kolla/octavia-housekeeping:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-housekeeping:20240524.1
docker tag kolla/octavia-base:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-base:20240524.1
docker tag kolla/openstack-base:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/openstack-base:20240524.1
docker tag kolla/base:2024.1-custom public.ecr.aws/p6g9k8e4/taurus-kolla/base:20240524.1

docker push public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-api:20240524.1
docker push public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-driver-agent:20240524.1
docker push public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-health-manager:20240524.1
docker push public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-worker:20240524.1
docker push public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-housekeeping:20240524.1
docker push public.ecr.aws/p6g9k8e4/taurus-kolla/octavia-base:20240524.1
docker push public.ecr.aws/p6g9k8e4/taurus-kolla/openstack-base:20240524.1
docker push public.ecr.aws/p6g9k8e4/taurus-kolla/base:20240524.1
