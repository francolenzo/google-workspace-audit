from reporting.common import cargar_json

def generar_modulo4():
    logins_sospechosos = cargar_json("data/audit_logs/logins_sospechosos.json")
    cambios_admin = cargar_json("data/audit_logs/cambios_admin.json")
    apps_terceros = cargar_json("data/audit_logs/apps_terceros.json")
    eventos_drive = cargar_json("data/audit_logs/drive_eventos.json")

    html = """
    <!-- Módulo 4: Eventos de Seguridad -->
    <div class="box">
        <h2>📝 Módulo 4: Eventos de Seguridad y Actividad</h2>
        <table>
            <tr><th>Categoría</th><th>Cantidad</th></tr>
            <tr><td>Logins sospechosos/fallidos</td><td>{}</td></tr>
            <tr><td>Cambios de configuración/admin</td><td>{}</td></tr>
            <tr><td>Apps de terceros autorizadas</td><td>{}</td></tr>
            <tr><td>Eventos relevantes de Drive</td><td>{}</td></tr>
        </table>
    """.format(
        len(logins_sospechosos),
        len(cambios_admin),
        len(apps_terceros),
        len(eventos_drive)
    )

    # Detalle de logins sospechosos
    if logins_sospechosos:
        html += """
        <h3>⚠️ Logins sospechosos</h3>
        <table>
            <tr><th>Usuario</th><th>Fecha</th><th>Tipo</th><th>IP</th></tr>
        """
        for e in logins_sospechosos[:10]:
            usuario = e.get("actor", {}).get("email", "N/A")
            fecha = e.get("id", {}).get("time", "N/A")
            tipo = next((ev["name"] for ev in e.get("events", []) if ev.get("name")), "N/A")
            ip = e.get("ipAddress", "N/A")
            html += f"<tr><td>{usuario}</td><td>{fecha}</td><td>{tipo}</td><td>{ip}</td></tr>"
        if len(logins_sospechosos) > 10:
            html += f"<tr><td colspan='4'>... y {len(logins_sospechosos) - 10} más</td></tr>"
        html += "</table>"

    # Detalle de cambios admin
    if cambios_admin:
        html += """
        <h3>⚠️ Cambios de configuración/admin</h3>
        <table>
            <tr><th>Usuario</th><th>Fecha</th><th>Acción</th></tr>
        """
        for e in cambios_admin[:10]:
            usuario = e.get("actor", {}).get("email", "N/A")
            fecha = e.get("id", {}).get("time", "N/A")
            accion = next((ev.get("name") for ev in e.get("events", []) if ev.get("name")), "N/A")
            html += f"<tr><td>{usuario}</td><td>{fecha}</td><td>{accion}</td></tr>"
        if len(cambios_admin) > 10:
            html += f"<tr><td colspan='3'>... y {len(cambios_admin) - 10} más</td></tr>"
        html += "</table>"

    # Detalle de apps de terceros
    if apps_terceros:
        html += """
        <h3>⚠️ Apps de terceros autorizadas recientemente</h3>
        <table>
            <tr><th>Usuario</th><th>Fecha</th><th>App</th></tr>
        """
        for e in apps_terceros[:10]:
            usuario = e.get("actor", {}).get("email", "N/A")
            fecha = e.get("id", {}).get("time", "N/A")
            app = next((ev.get("parameters", [{}])[0].get("value", "N/A") for ev in e.get("events", []) if "parameters" in ev), "N/A")
            html += f"<tr><td>{usuario}</td><td>{fecha}</td><td>{app}</td></tr>"
        if len(apps_terceros) > 10:
            html += f"<tr><td colspan='3'>... y {len(apps_terceros) - 10} más</td></tr>"
        html += "</table>"

    # Detalle de eventos de Drive
    if eventos_drive:
        html += """
        <h3>⚠️ Eventos relevantes de Drive</h3>
        <table>
            <tr><th>Usuario</th><th>Fecha</th><th>Acción</th></tr>
        """
        for e in eventos_drive[:10]:
            usuario = e.get("actor", {}).get("email", "N/A")
            fecha = e.get("id", {}).get("time", "N/A")
            accion = next((ev.get("name") for ev in e.get("events", []) if ev.get("name")), "N/A")
            html += f"<tr><td>{usuario}</td><td>{fecha}</td><td>{accion}</td></tr>"
        if len(eventos_drive) > 10:
            html += f"<tr><td colspan='3'>... y {len(eventos_drive) - 10} más</td></tr>"
        html += "</table>"

    html += "</div>"
    return html
