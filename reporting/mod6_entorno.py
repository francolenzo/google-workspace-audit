from reporting.common import cargar_json

def generar_modulo6():
    config = cargar_json("data/environment_security/configuracion_seguridad.json")

    verificacion_2fa = config.get("verificacion_en_2_pasos_enforced", "N/A")
    apps_terceros = config.get("apps_terceros_detectadas", [])
    comparticion_externa = config.get("comparticion_externa_detectada", "N/A")

    html = """
    <!-- Módulo 6: Seguridad del Entorno -->
    <div class="box">
        <h2>☁️ Módulo 6: Seguridad del Entorno</h2>
        <table>
            <tr><th>Configuración</th><th>Estado</th></tr>
            <tr><td>2FA (verificación en 2 pasos) forzada</td><td>{}</td></tr>
            <tr><td>Apps de terceros detectadas</td><td>{}</td></tr>
            <tr><td>Compartición externa detectada</td><td>{}</td></tr>
        </table>
    """.format(
        "✅ " + verificacion_2fa if "Sí" in verificacion_2fa else "⚠️ " + verificacion_2fa,
        len(apps_terceros),
        "✅ Sí" if comparticion_externa is True else ("❌ No" if comparticion_externa is False else comparticion_externa)
    )

    # Detalles de apps de terceros
    if apps_terceros:
        html += """
        <h3>⚠️ Apps de terceros conectadas</h3>
        <ul>
        """
        for app in apps_terceros[:10]:
            html += f"<li>{app}</li>"
        if len(apps_terceros) > 10:
            html += f"<li>... y {len(apps_terceros) - 10} más</li>"
        html += "</ul>"

    html += "</div>"
    return html
