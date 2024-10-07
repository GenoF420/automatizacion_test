Feature: Recuperación de contraseña

  Scenario: Recuperar contraseña con correo registrado
    Given que accedo a la aplicación y navego a la página de inicio de sesión
    When selecciono la opción de "¿Olvidaste tu contraseña?"
    And ingreso un correo electrónico registrado "fhlbkblgfaiapsoddc@hthlm.com"
    Then recibo un mensaje de confirmación y un correo con las instrucciones para restablecer mi contraseña

  Scenario: Recuperar contraseña con correo no registrado
    Given que accedo a la aplicación y navego a la página de inicio de sesión
    When selecciono la opción de "¿Olvidaste tu contraseña?"
    And ingreso un correo electrónico no registrado
    Then aparece un mensaje de error indicando que el correo no está registrado
