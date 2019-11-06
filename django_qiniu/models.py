from django.db import models
from qiniu import Auth, BucketManager


class Bucket(models.Model):
    # TODO 暂时不支持多个帐号
    name = models.SlugField(primary_key=True)
    private = models.BooleanField("是否是私有空间", default=False)
    access_key = models.SlugField(blank=False)
    secret_key = models.SlugField(blank=False)
    domain = models.CharField(blank=False, max_length=127)

    @property
    def qiniu_auth(self):
        if hasattr(self, "_qiniu_auth"):
            return self._aqiniu_uth
        self._aqiniu_uth = Auth(self.access_key, self.secret_key)
        return self._aqiniu_uth

    @property
    def bucket_manager(self):
        if hasattr(self, "_bucket_manager"):
            return self._bucket_manager
        self._bucket_manager = BucketManager(self.qiniu_auth)
        return self._bucket_manager


class Resource(models.Model):
    """七牛的资源"""
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    key = models.CharField("文件名", blank=False, max_length=127)
    # TODO size, updatetime, filetype, storagetype

    class Meta:
        unique_together = ("bucket", "key")
