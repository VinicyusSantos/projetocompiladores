def generate_html(form):
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{form.title}</title>
</head>
<body>
    <h1>{form.title}</h1>
    <form>
"""
    for field in form.fields:
        label = field.label
        if field.kind in ("text", "email", "number"):
            html += f'        <label>{label}</label><br>\n'
            html += f'        <input type="{field.kind}"><br><br>\n\n'
        elif field.kind == "checkbox":
            html += f'        <label>{label}</label>\n'
            html += f'        <input type="checkbox"><br><br>\n\n'
        elif field.kind == "submit":
            html += f'        <button type="submit">{label}</button>\n'
    html += """    </form>
</body>
</html>
"""
    return html
