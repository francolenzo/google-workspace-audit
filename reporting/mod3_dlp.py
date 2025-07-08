from reporting.common import cargar_json

def generar_modulo3():
    publicos = cargar_json("data/dlp_and_sharing/archivos_publicos.json")
    externos = cargar_json("data/dlp_and_sharing/archivos_externos.json")
    sospechosos = cargar_json("data/dlp_and_sharing/archivos_sospechosos.json")

    html = """
    <!-- Módulo 3: DLP y Compartición -->
    <div class="box">
        <h2>🛡️ Módulo 3: DLP y Compartición de Archivos</h2>
        <table>
            <tr><th>Categoría</th><th>Cantidad</th></tr>
            <tr><td>Archivos públicos (acceso anyone)</td><td>{}</td></tr>
            <tr><td>Archivos compartidos fuera del dominio</td><td>{}</td></tr>
            <tr><td>Archivos sospechosos (nombres críticos)</td><td>{}</td></tr>
        </table>
    """.format(
        len(publicos),
        len(externos),
        len(sospechosos)
    )

    # Sección de detalles, solo si hay hallazgos
    if publicos:
        html += """
        <h3>⚠️ Archivos públicos</h3>
        <table>
            <tr><th>Nombre</th><th>Propietario</th><th>Tipo</th></tr>
        """
        for a in publicos[:10]:
            nombre = a.get("name", "N/A")
            owner = (a.get("owners", [{}])[0].get("emailAddress", "N/A")
                        if a.get("owners") else "N/A")
            mime = a.get("mimeType", "N/A")
            html += f"<tr><td>{nombre}</td><td>{owner}</td><td>{mime}</td></tr>"
        if len(publicos) > 10:
            html += f"<tr><td colspan='3'>... y {len(publicos) - 10} más</td></tr>"
        html += "</table>"

    if externos:
        html += """
        <h3>⚠️ Archivos compartidos fuera del dominio</h3>
        <table>
            <tr><th>Nombre</th><th>Propietario</th><th>Tipo</th></tr>
        """
        for a in externos[:10]:
            nombre = a.get("name", "N/A")
            owner = (a.get("owners", [{}])[0].get("emailAddress", "N/A")
                        if a.get("owners") else "N/A")
            mime = a.get("mimeType", "N/A")
            html += f"<tr><td>{nombre}</td><td>{owner}</td><td>{mime}</td></tr>"
        if len(externos) > 10:
            html += f"<tr><td colspan='3'>... y {len(externos) - 10} más</td></tr>"
        html += "</table>"

    if sospechosos:
        html += """
        <h3>⚠️ Archivos sospechosos por nombre</h3>
        <table>
            <tr><th>Nombre</th><th>Propietario</th><th>Tipo</th></tr>
        """
        for a in sospechosos[:10]:
            nombre = a.get("name", "N/A")
            owner = (a.get("owners", [{}])[0].get("emailAddress", "N/A")
                        if a.get("owners") else "N/A")
            mime = a.get("mimeType", "N/A")
            html += f"<tr><td>{nombre}</td><td>{owner}</td><td>{mime}</td></tr>"
        if len(sospechosos) > 10:
            html += f"<tr><td colspan='3'>... y {len(sospechosos) - 10} más</td></tr>"
        html += "</table>"

    html += "</div>"
    return html
