.. _web-services-api--authentication--oauth:

:oro_show_local_toc: false

.. index::
    single: Security; OAuth Authorization; OAuth Authentication
    single: OAuth Authorization
    single: OAuth Authentication

OAuth Authentication
====================

|OAuth 2.0| is the industry-standard protocol for authorization. OAuth 2.0 focuses on client developer simplicity
while providing specific authorization flows for web applications, desktop applications, mobile phones,
and living room devices.

It is implemented by the :ref:`OroOAuth2ServerBundle <dev-guide>` that supports
|OAuth 2.0 Authorization Code Grant|, |OAuth 2.0 Client Credentials Grant| and |OAuth 2.0 Password Grant|.

For more details, see :ref:`Manage OAuth Applications <dev-guide>`
and :ref:`Manage Storefront OAuth Applications <dev-guide>`.

Generate Tokens
---------------

.. toctree::
   :titlesonly:

   oauth-authorization-code
   oauth-client-credentials
   oauth-password
   oauth-password-refresh


.. note::

    In order to use OAuth authentication, private and public keys should be generated and placed
    to the server. Please contact your administrator or please follow
    the :ref:`OroOAuth2ServerBundle documentation <dev-guide>`
    if you see the following error message:

    *The encryption key does not exist.*

.. note::

    If the system has the customer portal package installed, OAuth authorization for customer users
    to the storefront API resources is enabled automatically.


.. include:: /include/include-links-dev.rst
   :start-after: begin
