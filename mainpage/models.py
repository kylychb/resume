from django.db import models
from ckeditor.fields import RichTextField

from .utils import derictory_path


class PersonalInfo(models.Model):
    fullname = models.CharField("Полное имя", max_length=255)
    profession = models.CharField("Профессия", max_length=255)
    resume_file = models.FileField("Файл резюме", upload_to=derictory_path)
    about_me = RichTextField("Текст обо мне")
    image = models.ImageField("Картинка баннера", upload_to=derictory_path, null=True)
    image_mobile = models.ImageField("Картинка баннера для мобилки", upload_to=derictory_path, null=True)
    email = models.CharField("Почта", max_length=255, default="")
    phone_number = models.CharField("Номер телефона", max_length=255, default="")
    linked_in = models.CharField("Ссылка на LinkedIn", max_length=255, default="")
    github = models.CharField("Ссылка на GitHub", max_length=255, default="")

    class Meta:
        verbose_name = "Персональная информальная"
        verbose_name_plural = "Персональная информация"

    def __str__(self):
        return self.fullname


class AdditionalInfo(models.Model):
    icon = models.ImageField("Иконка", upload_to=derictory_path)
    title = models.CharField("Заголовок", max_length=50)
    text_card = RichTextField("Текст")

    class Meta:
        verbose_name = "Дополнительная информация"
        verbose_name_plural = "Дополнительная информация"

        def __str__(self):
            return self.title

class Experience(models.Model):
    title = models.CharField("Заголовок", max_length=50)
    text_card = RichTextField("Текст")

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"

        def __str__(self):
            return self.title

class WorkExperiance(models.Model):
    icon = models.ImageField("Иконка компаний", upload_to=derictory_path)
    company_name = models.CharField("Название компаний", max_length=100)
    positions = models.CharField("Позиция на работе", max_length=255)
    responsibility = RichTextField("Обязанности по работе")

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"

        def __str__(self):
            return self.company_name

class Portfolio(models.Model):
    image = models.ImageField("Картинка", upload_to=derictory_path)
    image_mobile = models.ImageField("Картинка для мобилки", upload_to=derictory_path)
    project_name = models.CharField("Название проекта", max_length=255)
    github_link = models.CharField("Ссылка на гитхаб проекта", max_length=255, null=True, blank=True)
    live_demo = models.TextField("Ссылка на демо", null=True, blank=True)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проект"

        def __str__(self):
            return self.project_name