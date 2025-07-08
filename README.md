
# Google Workspace Audit 🚀

**Auditoría y reporte automatizado de seguridad para Google Workspace**

[![LinkedIn](https://img.shields.io/badge/autor-Franco%20Lenzo-blue)](https://www.linkedin.com/in/francolenzo/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## 📝 Descripción

Este proyecto es una herramienta open-source en Python para auditar de forma automatizada la seguridad y el cumplimiento de buenas prácticas en un dominio de Google Workspace. Permite generar un reporte detallado en HTML sobre aspectos críticos como autenticación, MFA, archivos públicos, delegaciones de Gmail, uso de aplicaciones de terceros, y más.

> **Ideal para equipos de seguridad, administradores de Google Workspace, y consultores que buscan una visión rápida y clara del estado de seguridad de una organización.**

---

## 🎯 Features principales

- **Auditoría de MFA**: Detecta usuarios sin segundo factor habilitado.
- **Análisis de archivos públicos y compartidos fuera del dominio** (DLP básico).
- **Revisión de delegaciones y reenvíos externos en Gmail**.
- **Eventos críticos de seguridad** (logins sospechosos, cambios de admins, apps de terceros).
- **Reporte HTML listo para compartir** (portada, resumen, hallazgos destacados, secciones modulares).
- **Framework modular**: fácil de extender y customizar.
- **Ejecución local y 100% open source**.

---

## ⚡ Instalación y setup rápido

1. **Cloná el repo:**
   ```bash
   git clone https://github.com/francolenzo/google-workspace-audit.git
   cd google-workspace-audit
   ```

2. **Creá y activá tu entorno virtual:**
   ```bash
   python3 -m venv myenvv
   source myenvv/bin/activate
   ```

3. **Instalá las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Descargá y agregá tu archivo `credentials.json`:**
   - Desde [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
   - **Colocá el archivo en la raíz del proyecto**
   - _Nunca subas este archivo a GitHub_

5. **Corré el setup de configuración inicial:**
   ```bash
   python main.py
   ```
   - Ingresá tu dominio y admin cuando el script lo solicite.
   - Se abrirá un navegador para autorizar el acceso OAuth2.

---

## 🛡️ Seguridad


- El código está pensado para ser seguro por diseño, pero siempre revisá y adaptá a tus políticas internas.

---

## 🖥️ Uso

Después de correr el script, encontrarás el **reporte HTML** en la carpeta `/output/`.  
Ábrelo con tu navegador para ver el resumen y los hallazgos de la auditoría.

---

## 🛠️ Extensión y personalización

- Podés modificar o agregar módulos en la carpeta `/modules/` para nuevas auditorías.
- El reporte HTML se arma en `/reporting/`. Todo es fácilmente personalizable.
- Se aceptan contribuciones y sugerencias para nuevos módulos.

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
