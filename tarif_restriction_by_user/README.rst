=============================
Tarif Restriction by User
=============================

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3
.. image:: https://img.shields.io/badge/GitLab-Repositorio-orange?logo=gitlab
   :target: https://gitlab.com/broobe/odoo/gc-odoo-ramos-addons
   :alt: Repositorio en GitLab

Overview
========
This module, **Tarif Restriction by User**, is designed to restrict which tariffs can be used by each user in Odoo. It provides a way to manage and control tariff usage based on user permissions, ensuring that only authorized users can access specific tariffs.

Key Features
============
- Restrict tariff usage per user.
- Seamless integration with Odoo's sales and product modules.
- Easy configuration through user settings.

Installation
============
1. Ensure that the dependencies `base`, `sale`, and `product` are installed in your Odoo instance.
2. Copy the module folder `tarif_restriction_by_user` into your Odoo addons directory.
3. Update the module list by navigating to Apps > Update Apps List in Odoo.
4. Search for "Tarif Restriction by User" in the Apps menu and install the module.

Configuration
=============
1. Go to **Settings > Users & Companies > Users**.
2. Open a user form and configure the tariffs that the user is allowed to use.
3. Save the changes.

Usage
=====
1. When creating or editing a sale order, the system will restrict the available tariffs based on the user's configuration.
2. Users will only see the tariffs they are authorized to use.

Dependencies
============
- `base`
- `sale`
- `product`

License
=======
This module is licensed under the GPL-3 License.

Author
======
Developed by **Gauchocode**.
