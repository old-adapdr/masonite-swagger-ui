# Adding route to the SwaggerUI controller
ROUTES.append(Get("/docs", "SwaggerUIController@show").name("swagger-ui"))
