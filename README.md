# 🛡️ Sistema de Gestión de Identidades con Django

Este proyecto es un sistema de gestión de identidades desarrollado en **Django, React y Rust**, diseñado para integrarse con múltiples aplicativos y permitir una administración segura, escalable y personalizable de usuarios, roles y permisos.

## 🎯 Objetivo

Construir una solución integral para la gestión de identidades digitales que permita:

- Definir **aplicativos**, **módulos** y **roles**.
- Crear flujos de solicitud de acceso y validación para identidades.
- Controlar permisos mediante integración con **LDAP**.
- Automatizar notificaciones vía correo electrónico.
- Facilitar la administración centralizada desde un panel moderno.

---

## 🔧 Funcionalidades principales

- 📋 **Formularios dinámicos** para:
  - Registro de aplicativos.
  - Configuración de módulos y roles por aplicativo.
  - Solicitud de identidades (creación de acceso).
  
- 🧩 **Flujo jerárquico**:
  - Solicitud enviada por usuario o sistema.
  - Revisión por **supervisor**.
  - Aprobación final por **administrador**.

- 📤 **Envío automático de notificaciones por correo** en cada etapa.

- 🔐 **Autenticación e integración con LDAP** para validar identidad y permisos según el aplicativo.

- 📊 Panel de administración moderno y personalizable (con soporte para Tailwind CSS).

- 🔄 Arquitectura extensible: posibilidad de agregar APIs REST, logs, historiales de actividad, y más.

---

## 🛠️ Tecnologías utilizadas

- **Django 5.x**
- **React** para interfaces dinámicas del frontend
- **Rust** para microservicios de alto rendimiento
- **Tailwind CSS** para estilos modernos y personalizables
- **PostgreSQL**
- **LDAP (Active Directory)** integración para autenticación
- **Celery + Redis** para tareas asíncronas
- **SMTP** para envío de correos
- **Unfold Admin** como panel administrativo moderno

---

## 📌 Próximas funcionalidades

- Firma electrónica de autorizaciones.
- Soporte para multifactor (2FA).
- Dashboard con métricas y auditoría.
- Exportación de datos (PDF/Excel).
- API REST para integración con sistemas externos.
