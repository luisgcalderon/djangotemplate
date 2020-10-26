from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

from myproject.apps.core.models import UrlBase, CreationModificationDateBase

class Idea(UrlBase, CreationModificationDateBase):
    title = models.CharField(
        _("Title"),
        max_length=200,
    )
    content = models.TextField(
        _("Content"),
    )
    slug = models.SlugField(_("Slug for the urls"), max_length=50)

    # class Meta:
    #     verbose_name = _("Idea")
    #     verbose_name_plural = _("Ideas")

    def __str__(self):
        return self.title
    
    def get_url_path(self):
        return reverse("idea_details", kwargs={
            "idea_id": str(self.pk),
        })