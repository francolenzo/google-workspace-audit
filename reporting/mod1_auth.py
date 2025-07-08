from reporting.common import cargar_json


def generar_modulo1():
    sin_mfa = cargar_json("data/auth_and_access/usuarios_sin_mfa.json")
    inactivos = cargar_json("data/auth_and_access/usuarios_inactivos.json")
    privilegiados = cargar_json("data/auth_and_access/usuarios_privilegiados.json")
    delegaciones = cargar_json("data/auth_and_access/usuarios_con_delegaciones.json")
    resumen = cargar_json("data/auth_and_access/resumen_general.json")

    html = """
    <!-- Módulo 1: Autenticación y Accesos -->
    <div class="box">
        <h2>🔐 Módulo 1: Autenticación y Accesos</h2>
        <table>
            <tr><th>Categoría</th><th>Resultado</th></tr>
            <tr><td>Usuarios totales</td><td>{}</td></tr>
            <tr><td>Usuarios sin MFA</td><td>{}</td></tr>
            <tr><td>Usuarios inactivos</td><td>{}</td></tr>
            <tr><td>Usuarios privilegiados</td><td>{}</td></tr>
            <tr><td>Usuarios con delegaciones (placeholder)</td><td>{}</td></tr>
            <tr><td>Unidades organizativas (OUs)</td><td>{}</td></tr>
            <tr><td>Grupos</td><td>{}</td></tr>
        </table>
    </div>
    """.format(
        resumen.get("usuarios_totales", "N/A"),
        len(sin_mfa),
        len(inactivos),
        len(privilegiados),
        len(delegaciones),
        resumen.get("unidades_organizativas", "N/A"),
        resumen.get("grupos", "N/A")
    )

    return html
