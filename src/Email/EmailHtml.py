from src import app


class EmailHtml:

    @staticmethod
    def email_activation(code):
        html = f"""
            <a href="{app.config['FRONT_LINK']}/email/?code={code}">click to this link</a>
        """
        return html

    @staticmethod
    def password_restore(code):
        html = f"""
                <a href="{app.config['FRONT_LINK']}/guest/?restore_password_security_code={code}">click to this link</a>
            """
        return html
