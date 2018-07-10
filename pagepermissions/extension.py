from django.core.exceptions import PermissionDenied
from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms import extensions

class ExtensionFactory:
    @staticmethod
    def with_model_params(name, **model_kwargs):
        return type(name, (Extension, ), {'model_kwargs': model_kwargs})


class Extension(extensions.Extension):

    def handle_model(self):

        #
        # Add custom fields to the (Page) class
        #
        model_kwargs = getattr(self, 'model_kwargs', {})
        self.model.add_to_class('permissions',
                                models.ManyToManyField('auth.Permission',
                                                verbose_name=_('permissions'),
                                                blank=True,
                                                **model_kwargs))

        #
        # Add request processor to do permission checks
        #
        self.model.register_request_processor(permission_request_processor)

    def handle_modeladmin(self, modeladmin):
        #
        # Add custom fields to the admin class
        #
        modeladmin.add_extension_options(_('Permissions'), {
            'fields': ['permissions',],
        })


def has_permission_to_view(page, user):
    """
    Check whether the user has permission to view the page. If the user has
    any of the page's permissions, they have permission. If the page has no set
    permissions, they have permission.

    """
    if page.permissions.count() == 0:
        return True
    for perm in page.permissions.all():
        perm_label = '%s.%s' % (perm.content_type.app_label, perm.codename)
        if user.has_perm(perm_label):
            return True
    return False


def permission_request_processor(page, request):
    """
    Raise PermissionDenied unless the user has permission to view the given
    page.

    """
    if not has_permission_to_view(page, request.user):
        raise PermissionDenied
