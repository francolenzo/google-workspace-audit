from reporting.common import cargar_json

def generar_modulo5():
    delegaciones = cargar_json("data/email_security/delegaciones.json")
    reenvios = cargar_json("data/email_security/reenvios_externos.json")
    imap_pop = cargar_json("data/email_security/imap_pop.json")

    html = """
    <!-- Módulo 5: Seguridad de Email -->
    <div class="box">
        <h2>📧 Módulo 5: Seguridad de Email</h2>
        <table>
            <tr><th>Categoría</th><th>Cantidad</th></tr>
            <tr><td>Usuarios con delegaciones activas</td><td>{}</td></tr>
            <tr><td>Usuarios con reenvíos externos</td><td>{}</td></tr>
            <tr><td>Usuarios con IMAP/POP habilitado</td><td>{}</td></tr>
        </table>
    """.format(
        len(delegaciones),
        len(reenvios),
        len(imap_pop)
    )

    if delegaciones:
        html += """
        <h3>⚠️ Usuarios con delegaciones</h3>
        <table>
            <tr><th>Usuario</th><th>Delegados</th></tr>
        """
        for d in delegaciones[:10]:
            user = d.get("user", "N/A")
            delegates = ", ".join([dg.get("delegateEmail", "N/A") for dg in d.get("delegates", [])])
            html += f"<tr><td>{user}</td><td>{delegates}</td></tr>"
        if len(delegaciones) > 10:
            html += f"<tr><td colspan='2'>... y {len(delegaciones) - 10} más</td></tr>"
        html += "</table>"

    if reenvios:
        html += """
        <h3>⚠️ Usuarios con reenvíos automáticos externos</h3>
        <table>
            <tr><th>Usuario</th><th>Reenvía a</th></tr>
        """
        for r in reenvios[:10]:
            user = r.get("user", "N/A")
            to = r.get("to", "N/A")
            html += f"<tr><td>{user}</td><td>{to}</td></tr>"
        if len(reenvios) > 10:
            html += f"<tr><td colspan='2'>... y {len(reenvios) - 10} más</td></tr>"
        html += "</table>"

    if imap_pop:
        html += """
        <h3>⚠️ Usuarios con IMAP/POP habilitado</h3>
        <table>
            <tr><th>Usuario</th><th>IMAP</th><th>POP</th></tr>
        """
        for i in imap_pop[:10]:
            user = i.get("user", "N/A")
            imap = "Sí" if i.get("imap") else "No"
            pop = i.get("pop", "N/A")
            html += f"<tr><td>{user}</td><td>{imap}</td><td>{pop}</td></tr>"
        if len(imap_pop) > 10:
            html += f"<tr><td colspan='3'>... y {len(imap_pop) - 10} más</td></tr>"
        html += "</table>"

    html += "</div>"
    return html
