"""A SwaggerUIProvider Service Provider."""

from masonite.provider import ServiceProvider
from ..commands.InstallCommand import InstallCommand


class SwaggerUIProvider(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        self.app.bind("install-swagger-ui", InstallCommand())

    def boot(self):
        """Boots services required by the container."""
        pass
