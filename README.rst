feincms-pagepermissions
=======================

A simple `FeinCMS <https://github.com/feincms/feincms>`_ extension that adds 
permission-checking to a model. The model is assumed to be a Page, but it could
be any FeinCMS model.


Usage
-----

Install using `pip <https://pypi.python.org/pypi/pip/>`_:

::

    pip install feincms-pagepermissions

Change your Django settings to include pagepermissions:

.. code:: python

    INSTALLED_APPS += (
        'pagepermissions',
    )

Then add the extension to your content type:

.. code:: python

    Page.register_extensions(
        ...
        'pagepermissions.extension',
    )

If you need to specify arguments for `permissions` field, i.e. `limit_choices_to`:

.. code:: python

    from pagepermissions.extension import ExtensionFactory as PagePermissionExtensionFactory
    
    Page.register_extensions(
        ...
        PagePermissionExtensionFactory.with_model_params(
            'MyCustomPermissionExt',
            limit_choices_to=Q(…)
        ),
    )

This will add a permissions field to your content type that you will have to add
yourself through syncdb or South or otherwise.

When you edit or add a page you will have the option of setting the
permissions required for a user to view that page. You can select multiple
permissions, and if the user has any of those they will be able to view the
page. Otherwise they will receive a 403.

Finally, you may also want to keep a page out of the navigation if the user has
no permission to view it. For this, there is a template filter called 
``check_page_permission``. Use it as follows in your template:

.. code:: django

   {% load feincms_page_tags feincms_pagepermissions_tags %}
   
   {% feincms_nav feincms_page level=1 depth=1 as level1 %}
   {% for page in level1 %}
       {% if page|check_page_permission:user %}
          ...display page navigation...
       {% endif %}
   {% endfor %}


Contributing
------------

Your pull requests are very welcome! Please follow the established code style.


License
-------

feincms-pagepermissions is released under the `BSD license
<http://opensource.org/licenses/BSD-3-Clause>`_.
