IMAGES = {
  'kolla-default': {
    'category': 'kolla infra default',
    'list': [
      'cron',
      'dnsmasq',
      'hacluster-corosync',
      'hacluster-pacemaker-remote',
      'hacluster-pacemaker',
      'kolla-toolbox',
      'tgtd',
    ],
  },
  'fluentd': {
    'category': 'fluentd for opensearch',
    'list': [
      'fluentd',
    ],
  },
  'grafana': {
    'category': 'grafana for metric visualization',
    'list': [
      'grafana',
    ],
  },
  'haproxy': {
    'category': 'haproxy for load balancing',
    'list': [
      'haproxy',
    ],
  },
  'influxdb': {
    'category': 'influxdb for metric storage',
    'list': [
      'influxdb',
    ],
  },
  'keepalived': {
    'category': 'keepalived for high availability',
    'list': [
      'keepalived',
    ],
  },
  'mariadb': {
    'category': 'mariadb for database',
    'list': [
      'mariadb',
      'mariadb-clustercheck',
    ],
  },
  'memcached': {
    'category': 'memcached for caching',
    'list': [
      'memcached',
    ],
  },
  'iscsid': {
    'category': 'iscsid for block storage',
    'list': [
      'iscsid',
    ],
  },
  'opensearch': {
    'category': 'opensearch for log storage',
    'list': [
      'opensearch',
      'opensearch-dashboards',
    ],
  },
  'openvswitch': {
    'category': 'openvswitch for networking',
    'list': [
      'openvswitch-vswitchd',
      'openvswitch-db-server',
    ],
  },
  'prometheus': {
    'category': 'prometheus for metric collection, and exporters',
    'list': [
      'prometheus-v2-server',
      'prometheus-alertmanager',
      'prometheus-cadvisor',
      'prometheus-blackbox-exporter',
      'prometheus-elasticsearch-exporter',
      'prometheus-haproxy-exporter',
      'prometheus-memcached-exporter',
      'prometheus-mysqld-exporter',
      'prometheus-node-exporter',
      'prometheus-libvirt-exporter',
      'prometheus-openstack-exporter',
    ],
  },
  'rabbitmq': {
    'category': 'rabbitmq for messaging',
    'list': [
      'rabbitmq',
    ],
  },
  'redis': {
    'category': 'redis for caching',
    'list': [
      'redis',
      'redis-sentinel',
    ],
  },
}

import argparse

parser = argparse.ArgumentParser(description='Get the list of images for a given key or describe them.')
parser.add_argument('command', type=str, help="Command to execute ('desc' or 'get-images')")
parser.add_argument('key_name', type=str, help="The key name (e.g., 'prometheus', 'rabbitmq', 'redis', 'opensearch')")
args = parser.parse_args()

if args.command == 'desc':
    if args.key_name in IMAGES:
        category = IMAGES[args.key_name]['category']
        images_list = IMAGES[args.key_name]['list']
        total_images = len(images_list)

        print(f"{'-'*40}")
        print(f"Category '{args.key_name}': {category}")
        print(f"{'-'*40}")
        
        print("List of Images:")
        for image in images_list:
            print(f"- {image}")
        
        print(f"{'-'*40}")
        print(f"Total images count for '{args.key_name}': {total_images}")
        print(f"{'-'*40}")
    else:
        print(f"Key '{args.key_name}' not found.")

elif args.command == 'get-images':
    if args.key_name == 'all':
        for key in IMAGES:
            images_list = IMAGES[key]['list']
            for image in images_list:
                print(image)
    elif args.key_name in IMAGES:
        images_list = IMAGES[args.key_name]['list']
        for image in images_list:
            print(image)
    else:
        print(f"Key '{args.key_name}' not found.")
