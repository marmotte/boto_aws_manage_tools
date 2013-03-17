#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'marmotte'

"""
指定リージョンに登録された、EC2インスタンスの情報を取得するサンプル
"""

import boto,boto.ec2

# AWSリージョン情報を取得する
#print boto.ec2-sample.regions()

# EC2に接続する - ex. Asia Pacific(Tokyo)
conn = boto.ec2.connect_to_region("ap-northeast-1")

# リージョン内のインスタンス一覧を取得
reservations = conn.get_all_instances()
for reservation in reservations:
    print "* %s" % reservation
    for instance in  reservation.instances:
        print " - InstanceID   : %s" % instance.id
        print " - InstanceType : %s" % instance.instance_type
        print " - DNSName      : %s" % instance.public_dns_name
        print " - IP ADDRESS   : %s" % instance.ip_address
        print " - STATUS       : %s" % instance.state
        print " - AZ           : %s" % instance._placement
        print " - TAG NAME     : %s" % instance.tags[u'Name']
