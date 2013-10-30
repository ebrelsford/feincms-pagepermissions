feincms-pagepermissions
=======================

A simple `FeinCMS <https://github.com/feincms/feincms>`_ extension that adds 
permission-checking to a model. The model is assumed to be a Page, but it could
be any FeinCMS model.


Usage
-----

Install using `pip <https://pypi.python.org/pypi/pip/>`_, which should get 
any requirements, eg:

::

    pip install git+git://github.com/ebrelsford/feincms-pagepermissions@master

Change your Django settings to include pagepermissions:

::

    INSTALLED_APPS += (
        'pagepermissions',
    )

Then add the extension to your content type:

::

    Page.register_extensions(
        ...
        'pagepermissions.extension',
    )

This will add a permissions field to your content type that you will have to add
yourself through syncdb or South or otherwise.


Contributing
------------

Your pull requests are very welcome! Please follow the established code style.


License
-------

feincms-pagepermissions is released under the `BSD license
<http://opensource.org/licenses/BSD-3-Clause>`_.
