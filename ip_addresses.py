#!/usr/bin/env python
from utility import get_tagged_instances_by_environment
import sys


def main():
    hosted_zone = sys.argv[1] 
    hosts = get_tagged_instances_by_environment(hosted_zone)
    for host in hosts:
        print(host)


if __name__ == "__main__":
    main()
