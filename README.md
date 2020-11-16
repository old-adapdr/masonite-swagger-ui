# Masonite Swagger UI
The intention of this package is provide an easy method to adding SwaggerUI / OpenAPIUI to masonite.

## Installation
1. `pip3 install masonite-swagger-ui`
2. Add the package to the providers list:
    ```py
    from swagger_ui.providers import SwaggerUIProvider

    # ...

    PROVIDERS = [
    # ...
      SwaggerUIProvider
    ]
    ```
3. Run the install command: `craft swaggerui:install` this will copy over all the required scaffolding you need!

Thats it! You can now do `craft serve` and navigate to `/docs` to try it out in action!
