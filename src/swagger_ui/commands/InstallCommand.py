"""A InstallCommand Command."""
import os
from cleo import Command
from pathlib import Path
from masonite.packages import append_file, append_web_routes

package_directory = Path(__file__).parent.parent


class InstallCommand(Command):
    """
    Installs needed package files into the repository

    swaggerui:install
    """

    # files: list[tuple] = [(tuple(from, too)]
    files = [
        # Storage config update for Swagger-UI
        ("configs/storage.py", "config/storage.py"),
        # Templates for Swagger-UI
        (
            "resources/templates/swaggerui.html",
            "resources/templates/swaggerui.html",
        ),
        (
            "resources/templates/resources/templates/oauth2-redirect.html",
            "resources/templates/resources/templates/oauth2-redirect.html",
        ),
        # Stylesheet and icons for Swagger-UI
        ("static/css/swagger-ui.css", "storage/static/css/swagger-ui.css"),
        ("static/img/favicon-16x16", "storage/static/img/favicon-16x16"),
        ("static/img/favicon-32x32", "storage/static/img/favicon-32x32"),
        # JavaScript files for Swagger-UI
        (
            "static/js/swagger-ui-bundle.js",
            "storage/static/js/swagger-ui-bundle.js",
        ),
        (
            "static/js/swagger-ui-standalone-preset.js",
            "storage/static/js/swagger-ui-standalone-preset.js",
        ),
        ("static/js/swagger-ui.js", "storage/static/js/swagger-ui.js"),
    ]

    def handle(self):
        # Adding new files for the package
        for from_relative, to_location in self.files:
            from_location = os.path.abspath(
                os.path.join(package_directory, from_relative)
            )
            append_file(from_location=from_location, to_location=to_location)

        # Adds new webroute /docs for the SwaggerUIController@show to serve
        append_web_routes("routes/web.py")
