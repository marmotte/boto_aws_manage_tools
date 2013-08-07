# -*- coding: utf-8 -*-
#!/usr/bin/env python
__author__ = 'yosuke'

"""
スポットインスタンスを生成するサンプル
"""

from time import sleep
import boto.ec2

# インスタンス生成に必要な情報(最小)
image_id = 'ami-XXXXXXXX'
key_name = 'key_name'
max_price = '0.01'
instance_type = 't1.micro'
subnet_id = 'subnet-XXXXXXXX'
security_group_ids = ['sg-XXXXXXXX']

# EC2に接続する - ex. Asia Pacific(Tokyo)
conn = boto.ec2.connect_to_region('ap-northeast-1')

# VPCにSpot Instanceリクエストを送る
spot_request = conn.request_spot_instances(
                    max_price,
                    image_id=image_id,
                    count=1,
                    instance_type=instance_type,
                    key_name=key_name,
                    subnet_id=subnet_id,
                    security_group_ids=security_group_ids
                    )

# RequestからInstanceが生成されるのを監視する
print "Spot Request: %s" % spot_request[0].id
while True:
    instans_status = conn.get_all_spot_instance_requests(request_ids=spot_request[0].id)
    if instans_status[0].instance_id:
        break
    print ".",
    sleep(1)
print " Done."
print "Instance ID: %s" % instans_status[0].instance_id

