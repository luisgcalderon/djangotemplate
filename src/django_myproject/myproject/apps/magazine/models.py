from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class NewsArticle(models.Model):
    created_at = models.DateField(_("Created at"), auto_now_add=True)
    title = models.CharField(_("Title"), max_length=255)
    body = models.TextField(_("Body"))
    theme = models.CharField(_("Theme"), max_length=20)

    class Meta:
        verbose_name = _("News Article")
        verbose_name_plural = _("News Articles")

    def __str__(self):
        return self.title