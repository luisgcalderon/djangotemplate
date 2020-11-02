from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.

from myproject.apps.core.models import (
    UrlBase, 
    CreationModificationDateBase,
    object_relation_base_factory as generic_relation
)

FavoriteObjectBase = generic_relation(
    is_required=True
)

OwnerBase = generic_relation(
    prefix="owner",
    prefix_verbose=_("Owner"),
    is_required=True,
    add_related_name=True,
    limit_content_type_choices_to={
        "model__in": (
            "user",
            "group",
        )
    }
)

class Like(FavoriteObjectBase, OwnerBase):
    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
    def __str__(self):
        return _("{owner} likes {object}".format(
            owner=self.owner_content_object,
            object=self.content_object
        ))

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