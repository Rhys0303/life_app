from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200, verbose_name="項目名稱")
    description = models.TextField(blank=True, verbose_name="詳細內容")
    completed = models.BooleanField(default=False, verbose_name="是否完成")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "生活小幫手項目"
        verbose_name_plural = "生活小幫手項目"