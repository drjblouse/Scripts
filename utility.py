from boto import ec2
from keys import AWS_ACCESS_KEY_ID, AWS_DOMAIN, \
    AWS_REGION, AWS_SECRET_ACCESS_KEY


def get_aws_filter(hosted_zone):
    if AWS_DOMAIN not in hosted_zone:
        hosted_zone = hosted_zone + '.' + AWS_DOMAIN
    filter_dict = {"tag:HostedZone": hosted_zone}
    return filter_dict


def get_tagged_instances_by_environment(hosted_zone):
    hosts = list()
    ec2_conn = ec2.connect_to_region(
        AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    filter_dict = get_aws_filter(hosted_zone)
    reservations = ec2_conn.get_all_instances(filters=filter_dict)
    for res in reservations:
        for inst in res.instances:
            if inst.private_ip_address:
                hosts.append('{0} - {1}'.format(inst.tags['Service'],
                                                inst.private_ip_address))
    hosts.sort()
    return hosts


def get_ecs_ips(hosts):
    return get_stack_ips(hosts, 'ECS')


def get_stack_ips(hosts, filter_name):
    ecs_ips = list()
    for host in hosts:
        host_split = host.split('-')
        if filter_name.lower() in host_split[0].lower():
            ecs_ips.append(host_split[1].strip())
    return ecs_ips
