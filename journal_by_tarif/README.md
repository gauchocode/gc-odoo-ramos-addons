
# Journal by Tarif - Odoo 16

Este módulo permite restringir los diarios (`account.journal`) disponibles al crear facturas, en función de la **lista de precios** (`product.pricelist`) asociada a una **orden de venta** (`sale.order`).

## Características

- Añade un campo `journal_ids` a las listas de precios, donde se pueden definir los diarios permitidos.
- Al generar una factura desde una orden de venta, se asigna automáticamente un diario válido basado en la lista de precios.
- El campo `journal_id` en la factura solo mostrará los diarios definidos en la tarifa (si corresponde).
- Se realiza una validación adicional para asegurar que no se utilicen diarios no permitidos.
- Compatible con Odoo 16, sin necesidad de modificaciones en el frontend ni JS adicional.

## Cómo funciona

1. En la lista de precios (`product.pricelist`), seleccioná los diarios permitidos.
2. Cuando una orden de venta con esa lista de precios genera una factura:
   - Se asigna automáticamente uno de los diarios permitidos.
   - El dominio del campo `journal_id` se restringe a esos diarios.
   - Si un usuario intenta cambiar a un diario no permitido, el sistema lo bloquea con una validación.

## Instalación

1. Copiá este módulo en tu carpeta de `addons`.
2. Reiniciá el servidor de Odoo.
3. Activá el modo desarrollador.
4. Instalá el módulo desde la vista de aplicaciones.

## Traducciones

Este módulo incluye soporte para traducción al español. Usá el archivo `es.po` ubicado en la carpeta `i18n`.

## Créditos

Desarrollado por Pedro Esteban Jabie.
