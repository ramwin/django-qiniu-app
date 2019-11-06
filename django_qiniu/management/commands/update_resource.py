#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-11-06 17:50:50


import logging
import time
from django.core.management.base import BaseCommand
from django_qiniu.models import Bucket, Resource


log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "根新所有的Resource"

    def handle(self, *args, **kwargs):
        for bucket in Bucket.objects.all():
            log.info("处理{}".format(bucket))
            marker = None
            ret, eof, info = bucket.bucket_manager.list(bucket.name, marker=marker)
            if eof is True:
                log.info("处理完毕")
                for itemdata in ret["items"]:
                    Resource.objects.get_or_create(bucket=bucket, key=itemdata["key"])
