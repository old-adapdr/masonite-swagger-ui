"""A InstallCommand Command."""
import os
import shutil
from cleo import Command
from pathlib import Path
from masonite.packages import append_file, append_web_routes, create_controller

package_directory = Path(__file__).parent.parent

def append_image(from_location, to_location):
    shutil.copy(from_location, os.path.join(os.getcwd(), to_location))
    print("\033[92m {} has been appended! \033[0m".format(to_location))


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
            "resources/templates/swagger-ui.html",
            "resources/templates/swagger-ui.html",
        ),
        (
            "resources/templates/oauth2-redirect.html",
            "resources/templates/oauth2-redirect.html",
        ),
        # Stylesheet and icons for Swagger-UI
        ("static/css/swagger-ui.css", "storage/static/css/swagger-ui.css"),
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
        # Petshop Swagger/OpenAPI example
        ('static/schemas/petshop.json', 'storage/static/schemas/petshop.json')
    ]
    controller = 'controllers/SwaggerUIController.py'
    routes = "routes/web.py"
    images = [
        ("static/img/favicon-16x16.png", "storage/static/img/favicon-16x16.png"),
        ("static/img/favicon-32x32.png", "storage/static/img/favicon-32x32.png"),
    ]

    def handle(self):
        # Adding new files for the package
        for from_relative, to_location in self.files:
            from_location = os.path.abspath(
                os.path.join(package_directory, from_relative)
            )
            append_file(from_location=from_location, to_location=to_location)

        for from_relative, to_location in self.images:
            from_location = os.path.abspath(
                os.path.join(package_directory, from_relative)
            )
            append_image(from_location=from_location, to_location=to_location)

        # Adds new SwaggerUIController
        create_controller(os.path.abspath(os.path.join(package_directory, self.controller)))

        # Adds new webroute /docs for the SwaggerUIController@show to serve
        append_web_routes(os.path.abspath(os.path.join(package_directory, self.routes)))
