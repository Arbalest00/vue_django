from django.apps import AppConfig


class UsrDataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "usr_data"
    
    def ready(self):
        from .models import usr_data  # 导入模型
        usr_data.objects.all().delete()  # 删除所有usr_data记录
    
