
# Google Workspace Audit 🚀

**Auditoría y reporte automatizado de seguridad para Google Workspace**

[![LinkedIn](https://img.shields.io/badge/autor-Franco%20Lenzo-blue)](https://www.linkedin.com/in/francolenzo/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 🧪 Estado del proyecto

**Versión:** `v0.0.1`  
_Este proyecto está en pleno desarrollo y evolución activa._  
Ya estoy trabajando en la próxima versión con nuevas features y mejoras, basadas en feedback de la comunidad y casos reales.

¡Se aceptan sugerencias, issues y PRs!

---

## 📝 Descripción

Este proyecto es una herramienta open-source en Python para auditar de forma automatizada la seguridad y el cumplimiento de buenas prácticas en un dominio de Google Workspace. Permite generar un reporte detallado en HTML sobre aspectos críticos como autenticación, MFA, archivos públicos, delegaciones de Gmail, uso de aplicaciones de terceros, y más.

> **Ideal para equipos de seguridad, administradores de Google Workspace, y consultores que buscan una visión rápida y clara del estado de seguridad de una organización.**

---

## 🎯 Features principales

- **Auditoría de MFA:** Detecta usuarios sin segundo factor habilitado.
- **Análisis de archivos públicos y compartidos fuera del dominio** (DLP básico).
- **Revisión de delegaciones y reenvíos externos en Gmail**.
- **Eventos críticos de seguridad:** logins sospechosos, cambios de admins, apps de terceros.
- **Reporte HTML listo para compartir:** portada, resumen, hallazgos destacados, secciones modulares.
- **Framework modular:** fácil de extender y customizar.
- **Ejecución local y 100% open source.**

---

## ⚡ Instalación y setup rápido

1. **Cloná el repo:**
   ```bash
   git clone https://github.com/francolenzo/google-workspace-audit.git
   cd google-workspace-audit
   ```

2. **Creá y activá tu entorno virtual:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Instalá las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔑 Cómo obtener tu archivo `credentials.json` en Google Cloud Console

1. Ingresá a [Google Cloud Console](https://console.cloud.google.com/apis/credentials).
2. Creá un nuevo proyecto, o seleccioná uno existente.
3. Hacé click en “**Pantalla de consentimiento OAuth**” y configurá como “Interna” o “Externa” (según necesidad).
4. En “**Credenciales**”, hacé click en “Crear credenciales” → “ID de cliente de OAuth”.
5. Elegí “**Aplicación de escritorio**” como tipo de aplicación.
6. Descargá el archivo `credentials.json` y colocalo en la raíz del proyecto (junto a `main.py`).

> **Este archivo es privado y sensible. No lo compartas ni lo subas a ningún repositorio.**

---

## 🚦 Primer uso: autenticación y configuración

Al ejecutar el script por primera vez (`python3 main.py`):

- Te pedirá el dominio y el correo del administrador de Google Workspace.
- Confirmá que el archivo `credentials.json` esté en la raíz.
- El script abrirá un enlace (o te dará un link) para autenticarte con tu cuenta admin de Google Workspace y autorizar los permisos requeridos.
- Una vez autenticado, se guarda localmente el token de acceso (`token.pickle`).  
  No tendrás que volver a autenticarte salvo que expire o borres ese archivo.

---

## 🖥️ Uso básico

Después de ejecutar el script:

- Encontrarás el **reporte HTML** en la carpeta `/output/`.
- El reporte principal estará en `output/reporte_resumen_general.html`.  
  Abrilo en tu navegador para visualizar los hallazgos y el resumen de auditoría.

---

## 🛡️ Seguridad

- **Nunca subas tus credenciales (`credentials.json`, `token.pickle`) ni outputs personales al repo.**
- El proyecto incluye un `.gitignore` para evitar subir información sensible.
- El código está pensado para ser seguro por diseño, pero siempre revisá y adaptá a tus políticas internas.

---

## 🛠️ Extensión y personalización

- Podés modificar o agregar módulos en la carpeta `/modules/` para nuevas auditorías.
- El reporte HTML se arma en `/reporting/`, todo es personalizable.
- Se aceptan contribuciones y sugerencias para nuevos módulos, integraciones o visualizaciones.

---

## 🚧 Roadmap (v0.1+)

- Mejoras de visualización en el reporte.
- Integración de más fuentes de datos y módulos de seguridad.
- Soporte para ejecución con Docker.
- Mejora en manejo de errores y mensajes amigables.
- Ejemplos de reporte y screenshots en `/docs`.

¿Tenés ideas o sugerencias? ¡Sumalas vía issues o PR!

---

## 🤝 Contribuciones

¿Querés sumar?  
1. Abrí un issue con tu propuesta o bug.
2. Hacé un fork y mandá un Pull Request.
3. ¡Sumate a la comunidad de ciberseguridad colaborativa!

---

## 👤 Autor

[Franco Lenzo](https://www.linkedin.com/in/francolenzo/)  
Especialista en ciberseguridad, identidades digitales y automatización.

---

## ⚠️ Disclaimer

> **Este proyecto es educativo y experimental. Úsalo bajo tu propio riesgo y nunca en entornos productivos sin revisar el código.**

---
