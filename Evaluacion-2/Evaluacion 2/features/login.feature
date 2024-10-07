Feature: Inicio de sesión en la aplicación

  Scenario: Iniciar sesión con usuario válido y contraseña incorrecta
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And ingreso como usuario "fhlbkblgfaiapsoddc@hthlm.com"
    And ingreso una clave incorrecta "clavenoesfalsa123"
    And realizo el envío de los datos
    Then se inicia sesión y redirecciona al dashboard "https://www.recorrido.cl/es/users/dashboard#"
    And muestra un mensaje de "Has iniciado sesión"

  Scenario: Intentar iniciar sesión dejando campos vacíos
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And dejo el campo de usuario vacío
    And dejo el campo de clave vacío
    And realizo el envío de los datos
    Then redirecciona a "https://www.recorrido.cl/users/sign_in?locale=es"
    And aparece un mensaje de error "Email o contraseña inválidos."

  Scenario: Iniciar sesión con usuario válido y contraseña incorrecta
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And ingreso como usuario "fhlbkblgfaiapsoddc@hthlm.com"
    And ingreso una clave incorrecta "clavefalsa123"
    And realizo el envío de los datos
    Then redirecciona a "https://www.recorrido.cl/users/sign_in?locale=es"
    And aparece un mensaje de error "Email o contraseña inválidos."

  Scenario: Iniciar sesión con usuario inválido y contraseña correcta
    Given que puedo acceder a la aplicación
    When puedo acceder al login
    And ingreso como usuario "usuarioFalso@algo.cl"
    And ingreso la clave correcta "clavenoesfalsa123"
    And realizo el envío de los datos
    Then redirecciona a "https://www.recorrido.cl/users/sign_in?locale=es"
    And aparece un mensaje de error "Email o contraseña inválidos."
