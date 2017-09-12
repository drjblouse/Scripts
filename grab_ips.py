#!/usr/bin/env python
import sys
from utility import get_tagged_instances_by_environment, get_stack_ips

AWS_ZONE = sys.argv[1]
SERVICE = sys.argv[2]

hosted_zone = AWS_ZONE
hosts = get_tagged_instances_by_environment(hosted_zone)
stack_ips = get_stack_ips(hosts, SERVICE)
print(' '.join(stack_ips))
