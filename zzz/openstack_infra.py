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
      'mariadb-server',
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

def print_category_details(key, category, images_list):
    print(f"{'-'*40}\nCategory '{key}': {category}\n{'-'*40}\nList of Images:")
    for image in images_list:
        print(f"- {image}")
    print(f"{'-'*40}\nTotal images count for '{key}': {len(images_list)}\n{'-'*40}")

def print_images(images_list):
    for image in images_list:
        print(image)

def handle_desc_command(key_name):
    if key_name == 'all':
        for key, details in IMAGES.items():
            print_category_details(key, details['category'], details['list'])
    elif key_name in IMAGES:
        details = IMAGES[key_name]
        print_category_details(key_name, details['category'], details['list'])
    else:
        print(f"Key '{key_name}' not found.")

def handle_get_images_command(key_name):
    if key_name == 'all':
        for details in IMAGES.values():
            print_images(details['list'])
    elif key_name in IMAGES:
        print_images(IMAGES[key_name]['list'])
    else:
        print(f"Key '{key_name}' not found.")

if args.command == 'desc':
    handle_desc_command(args.key_name)
elif args.command == 'get-images':
    handle_get_images_command(args.key_name)
