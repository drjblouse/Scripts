#!/usr/bin/env python
import sys
import boto3
import json


AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION = 'us-west-2'
AWS_DOMAIN = ''


class ContainerDetail:
    pass


def get_ecs_clusters(filter_name=None):
    cluster_list = list()
    client = boto3.client('ecs')
    response = client.list_clusters()
    if filter_name:
        for cluster in response['clusterArns']:
            if filter_name.lower() in cluster.lower():
                cluster_list.append(cluster)
    else:
        for cluster in response['clusterArns']:
            cluster_list.append(cluster)
    return cluster_list


def get_container_amis(cluster_id):
    client = boto3.client('ecs')
    container_description = get_container_description(client, cluster_id)
    print(json.dumps(container_description['containerInstances'], indent=4,
                     sort_keys=True))
    cluster_hosts = dict()
    for container_detail in container_description['containerInstances']:
        cluster_hosts[container_detail['containerInstanceArn']] = \
            container_detail['ec2InstanceId']
    print(json.dumps(cluster_hosts, indent=4, sort_keys=True))


def get_container_description(client, cluster_id):
    response = client.list_container_instances(
        cluster=cluster_id)
    container_description = client.describe_container_instances(
        cluster=cluster_id,
        containerInstances=response['containerInstanceArns'])
    return container_description


def get_task_detail(client, cluster_id):
    response = client.list_tasks(cluster=cluster_id)
    tasks = list()
    for task in response['taskArns']:
        tasks.append(task)
    task_detail = client.describe_tasks(cluster=cluster_id, tasks=tasks)
    return task_detail


def get_tasks_by_filter(filter_name=None):
    cluster_list = get_ecs_clusters(filter_name)
    print(cluster_list)
    for cluster in cluster_list:
        get_container_amis(cluster)


def main():
    hosted_zone = sys.argv[1]
    get_tasks_by_filter(hosted_zone)


if __name__ == "__main__":
    main()
