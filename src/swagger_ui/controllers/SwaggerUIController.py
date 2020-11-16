"""A SwaggerUIController Module."""
from pathlib import Path
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class SwaggerUIController(Controller):
    """SwaggerUIController Controller Class."""

    def show(self, view: View):
        if Path('storage/static/schemas/openapi.json'):  # then we have one
            view.render('swagger-ui')
        else:  # return petstore
            view.render('swagger-ui' {'schema': 'https://petstore3.swagger.io/api/v3/openapi.json'})