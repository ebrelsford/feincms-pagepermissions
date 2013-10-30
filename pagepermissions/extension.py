from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.translation import ugettext_lazy as _


def has_permission_to_view(page, user):
    """
    Check whether the user has permission to view the page. If the user has
    any of the page's permissions, they have permission. If the page has no set
    permissions, they have permission.

    """
    if page.permissions.count() == 0:
        return True
    for perm in page.permissions.all():
        if user.has_perm(perm):
            return True
    return False


def permission_request_processor(page, request):
    """
    Raise PermissionDenied unless the user has permission to view the given
    page.

    """
    if not has_permission_to_view(page, request.user):
        raise PermissionDenied


def register(cls, admin_cls):

    #
    # Add custom fields to the (Page) class
    #
    cls.add_to_class('permissions',
                     models.ManyToManyField('auth.Permission',
                                            verbose_name=_('permissions'),
                                            blank=True,
                                            null=True))

    #
    # Add request processor to do permission checks
    #
    cls.register_request_processor(permission_request_processor)

    #
    # Add custom fields to the admin class
    #
    admin_cls.add_extension_options(_('Permissions'), {
        'fields': ['permissions',],
    })
