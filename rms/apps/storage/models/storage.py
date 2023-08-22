from django.db import models


class StorageModel(models.Model):

    name = models.CharField(max_length=50, blank=False, unique=True)
    user = models.ForeignKey(
        'users.UserModel', 
        related_name='storage_user', 
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Мосто хранения'
        verbose_name_plural = 'Места хранения'
        db_table = 'storage'

    def __str__(self):
        return self.name
