from datetime import datetime
from reporting.common import cargar_json
import os

def cargar_cantidad(path):
    """Devuelve la cantidad de elementos del archivo JSON, o N/A si no existe."""
    if os.path.exists(path):
        try:
            return len(cargar_json(path))
        except Exception:
            return "N/A"
    else:
        return "N/A"

def cargar_valor(path, key):
    """Devuelve el valor de una clave en un archivo JSON, o N/A si no existe."""
    if os.path.exists(path):
        try:
            return cargar_json(path).get(key, "N/A")
        except Exception:
            return "N/A"
    else:
        return "N/A"

def generar_portada_y_resumen():
    config = cargar_json("config/config.json") if os.path.exists("config/config.json") else {}
    resumen = cargar_json("data/auth_and_access/resumen_general.json") if os.path.exists("data/auth_and_access/resumen_general.json") else {}

    hallazgos = [
        ("Usuarios con MFA desactivado", cargar_cantidad("data/auth_and_access/usuarios_sin_mfa.json")),
        ("Archivos públicos", cargar_cantidad("data/dlp_and_sharing/archivos_publicos.json")),
        ("Archivos compartidos fuera del dominio", cargar_cantidad("data/dlp_and_sharing/archivos_externos.json")),
        ("Delegaciones de Gmail", cargar_cantidad("data/email_security/delegaciones.json")),
        ("Reenvíos externos", cargar_cantidad("data/email_security/reenvios_externos.json")),
        ("Logins sospechosos", cargar_cantidad("data/audit_logs/logins_sospechosos.json")),
        ("Apps de terceros conectadas", cargar_valor("data/environment_security/configuracion_seguridad.json", "apps_terceros_detectadas") if os.path.exists("data/environment_security/configuracion_seguridad.json") else "N/A"),
    ]

    # Si "Apps de terceros conectadas" devuelve lista, usamos el len:
    if isinstance(hallazgos[-1][1], list):
        hallazgos[-1] = (hallazgos[-1][0], len(hallazgos[-1][1]))

    html = f"""
    <div class="box">
        <h2>📅 Portada</h2>
        <div class="item"><span class="label">Fecha de ejecución:</span> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
        <div class="item"><span class="label">Dominio auditado:</span> {config.get("domain", "Desconocido")}</div>
        <div class="item"><span class="label">Administrador autenticado:</span> {config.get("admin_email", "Desconocido")}</div>
        <div class="item"><span class="label">Versión del script:</span> v0.3.0</div>
    </div>

    <div class="box" style="border: 2px dashed #3498db; background-color: #ecf6fc;">
        <h2>👨‍💻 Sobre el Autor</h2>
        <p><strong>Franco Lenzo</strong> — Especialista en ciberseguridad e identidades digitales.</p>
        <p>Creado con ❤️ y Python 🐍</p>
        <p>
            🌐 <a href="https://www.linkedin.com/in/francolenzo/" target="_blank">LinkedIn</a> |
            🐙 <a href="http://github.com/francolenzo" target="_blank">GitHub</a>
        </p>
    </div>

    <div class="box">
        <h2>📊 Resumen General</h2>
        <div class="item"><span class="label">Usuarios totales:</span> {resumen.get("usuarios_totales", "N/A")}</div>
        <div class="item"><span class="label">Usuarios sin MFA:</span> {resumen.get("usuarios_sin_mfa", "N/A")}</div>
        <div class="item"><span class="label">Usuarios inactivos:</span> {resumen.get("usuarios_inactivos", "N/A")}</div>
        <div class="item"><span class="label">Usuarios privilegiados:</span> {resumen.get("usuarios_privilegiados", "N/A")}</div>
        <div class="item"><span class="label">Unidades organizativas:</span> {resumen.get("unidades_organizativas", "N/A")}</div>
        <div class="item"><span class="label">Grupos:</span> {resumen.get("grupos", "N/A")}</div>
        <div class="item"><span class="label">Fecha de auditoría:</span> {resumen.get("fecha_auditoria", "N/A")}</div>
    </div>

    <div class="box">
        <h2>📈 Hallazgos Destacados</h2>
        <table>
            <tr><th>Item</th><th>Resultado</th></tr>
    """

    for titulo, cantidad in hallazgos:
        icono = "✅" if cantidad == 0 or cantidad == "N/A" else "⚠️"
        html += f"<tr><td>{titulo}</td><td>{icono} {cantidad}</td></tr>"

    html += "</table></div>"

    return html
