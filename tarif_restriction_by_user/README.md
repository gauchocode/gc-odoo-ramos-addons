# Tarif Restriction by User

Este módulo extiende la funcionalidad de facturación en Odoo para restringir los diarios (`account.journal`) disponibles al momento de crear una factura, basándose en la **tarifa (pricelist)** asociada a una **orden de venta**.

## 🧩 Funcionalidad

- Cuando una factura (`account.move`) se crea desde una orden de venta (`sale.order`), se asigna automáticamente el campo `sale_order_id`.
- El campo `journal_id` de la factura se restringe dinámicamente a los diarios definidos en el campo `journal_ids` de la tarifa (`pricelist_id`) asociada a esa orden.
- Se aplica un dominio dinámico al campo `journal_id` usando el mecanismo nativo de Odoo (`suitable_journal_ids`).
- Se mantiene la compatibilidad con el comportamiento estándar de Odoo: si no hay orden de venta, el sistema muestra los diarios como siempre.
- Incluye validación para evitar la selección de diarios fuera de los permitidos por la tarifa.

## ✅ Características

- Aplicación automática de restricciones de diario según la tarifa.
- Soporte completo para formularios de factura (`account.move.form`).
- Validación de datos en el backend (`@api.constrains`) para evitar errores de usuario o manipulaciones externas.
- No requiere JavaScript ni personalizaciones frontend.

## ⚙️ Uso

1. Asocie diarios válidos a cada tarifa desde el campo `journal_ids` en el modelo `Pricelist`.
2. Cuando cree una factura desde una orden de venta:
   - Se asociará la orden de venta a la factura (`sale_order_id`).
   - El campo `journal_id` solo mostrará los diarios definidos en la tarifa de esa orden.
3. Si intenta seleccionar un diario fuera de los definidos, se bloqueará la acción con un error.

## 🧠 Consideraciones Técnicas

- El campo `suitable_journal_ids` ha sido sobrescrito para incluir la lógica de tarifa.
- El campo `journal_id` ya posee un dominio nativo basado en `suitable_journal_ids`, por lo que no es necesario modificar la vista XML.
- El método `_compute_suitable_journal_ids` fue adaptado para incluir `sale_order_id`.

## 🏗️ Instalación

1. Copie el módulo en su carpeta de addons (`/mnt/extra-addons`, por ejemplo).
2. Actualice la lista de aplicaciones.
