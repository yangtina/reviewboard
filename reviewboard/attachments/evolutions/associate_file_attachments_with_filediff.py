from django_evolution.mutations import AddField
from django.db import models


MUTATIONS = [
    AddField('FileAttachment', 'filediff', models.ForeignKey, null=True,
              related_model='diffviewer.FileDiff')
]