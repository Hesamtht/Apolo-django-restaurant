from django.db import models
from django.urls import reverse

class Food(models.Model):
    CATEGORIES = (
        ('پیش غذا', 'پیش غذا'),
        ('غذای اصلی', 'غذای اصلی'),
        ('دسر', 'دسر')
    )

    category = models.CharField(max_length = 20 , choices = CATEGORIES , default = 'غذای اصلی')
    name = models.CharField("اسم" , max_length = 70)
    slug = models.SlugField(max_length = 70 , default = '')
    description = models.CharField("توضیحات" , max_length = 250)
    rate = models.IntegerField("امتیاز" , default = 100)
    price = models.IntegerField("قیمت")
    time = models.IntegerField("زمان لازم")
    pub_date = models.DateField("تاریخ انتشار" , auto_now = False , auto_now_add = True)
    photo = models.ImageField("عکس" , upload_to = "foods/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu:detail' , args = [self.slug])
