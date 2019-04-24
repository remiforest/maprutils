#! /usr/bin/python
# coding: utf-8

"""
MapR Utilities

Simplifying programming on MapR environments

"""

__version__ = "0.0.1"


""" Cluster utilities """

def get_cluster_name():
    """ returns the name of the first (default) cluster in mapr-clusters.conf """
    with open('/opt/mapr/conf/mapr-clusters.conf', 'r') as conf_file:
        first_line = conf_file.readline().rstrip()
        return first_line.split(' ')[0]



def get_cluster_cldb(cluster_name=None):
    """ returns an array with the IP and ports of the cluster CLDB """ 
    with open('/opt/mapr/conf/mapr-clusters.conf', 'r') as conf_file:
        if cluster_name:
            for line in enumerate(conf_file):
                if cluster_name in line:
                    break
            else:
                raise Exception('Unknown cluster {}'.format(cluster_name))
        else:
            line = conf_file.readline()

        return [ip_port for ip_port in line.rstrip().split(' ') if ":" in ip_port]



def get_cluster_ip(cluster_name=None):
    """ returns an array with the IP of the cluster node running the CLDB """
    return [ip_port.split(":")[0] for ip_port in get_cluster_cldb(cluster_name)]



def is_secure(cluster_name=None):
    """ returns True if cluster is secured, False if not """
    with open('/opt/mapr/conf/mapr-clusters.conf', 'r') as conf_file:
        if cluster_name:
            for line in enumerate(conf_file):
                if cluster_name in line:
                    break
            else:
                raise Exception('Unknown cluster {}'.format(cluster_name))
        else:
            line = conf_file.readline()

        return "secure=true" in line
