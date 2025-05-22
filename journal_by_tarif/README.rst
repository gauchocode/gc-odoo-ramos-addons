==============================
Journal by Tarif
==============================

Este módulo permite restringir los diarios (``account.journal``) disponibles en las facturas, en función de la **lista de precios** (``product.pricelist``) asociada a una **orden de venta** (``sale.order``).

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

.. image:: https://img.shields.io/badge/GitLab-Repositorio-orange?logo=gitlab
   :target: https://gitlab.com/broobe/odoo/gc-odoo-ramos-addons
   :alt: Repositorio en GitLab

Características
===============

* Añade un campo ``journal_ids`` a las listas de precios, donde se pueden definir los diarios permitidos.
* Al generar una factura desde una orden de venta, se asigna automáticamente un diario válido basado en la lista de precios.
* El campo ``journal_id`` en la factura solo mostrará los diarios definidos en la tarifa (si corresponde).
* Se realiza una validación adicional para asegurar que no se utilicen diarios no permitidos.

Cómo funciona
=============

#. En la lista de precios (``product.pricelist``), seleccioná los diarios permitidos.
#. Cuando una orden de venta con esa lista de precios genera una factura:
   * Se asigna automáticamente uno de los diarios permitidos.
   * El dominio del campo ``journal_id`` se restringe a esos diarios.
   * Si un usuario intenta cambiar a un diario no permitido, el sistema lo bloquea con una validación.

Instalación
===========

Para instalar este módulo:

#. Copiá este módulo en tu carpeta de ``addons``.
#. Reiniciá el servidor de Odoo.
#. Activá el modo desarrollador.
#. Instalá el módulo desde la vista de aplicaciones.

Configuración
=============

No se requiere configuración adicional.

Uso
===

1. Configurá los diarios permitidos en la lista de precios.
2. Generá una orden de venta y facturala. Se usará automáticamente un diario válido.
3. El sistema validará que el diario seleccionado esté permitido.

Traducciones
============

Este módulo incluye soporte para traducción al español. Usá el archivo ``es.po`` ubicado en la carpeta ``i18n``.

Bug Tracker
===========

Los errores se rastrean en GitLab Issues:
`https://gitlab.com/broobe/odoo/gc-odoo-ramos-addons/-/issues <https://gitlab.com/broobe/odoo/gc-odoo-ramos-addons/-/issues>`_

Si encontrás un problema, verificá si ya fue reportado o creá uno nuevo con los pasos para reproducirlo.

Créditos
========

Contribuidores
--------------

* Pedro Esteban Jabie

Mantenedor
----------

Este módulo es mantenido por Gauchocode.

Licencia
========

AGPL-3. Ver el archivo LICENSE para más detalles.
