'''
from common.models import DataTransferObject
from django.db import models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


# 모델 => 하나는 디비랑 연결, 하나는 리액트랑 연결
class CctvVO(models.Model):  # Value object -> DB랑 연결됨
    police = models.TextField()
    crime = models.TextField()
    create_at = models.DateTimeField()


class CctvDTO(DataTransferObject):  # DTO -> React와 데이터 연동
    police = ''
    crime = ''
    create_at = ''
'''
