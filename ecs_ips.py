#!/usr/bin/env python
import sys
from utility import get_tagged_instances_by_environment, get_ecs_ips

AWS_ZONE = sys.argv[1]

hosted_zone = AWS_ZONE
hosts = get_tagged_instances_by_environment(hosted_zone)
ecs_ips = get_ecs_ips(hosts)
print(' '.join(ecs_ips))
