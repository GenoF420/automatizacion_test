Feature: Registro de nuevos usuarios

  Scenario: Registro exitoso con datos válidos
    Given que puedo acceder a la aplicación
    When navego a la página de registro
    And ingreso un correo electrónico válido "rekaw87146@amxyy.com"
    And ingreso una contraseña válida "Clave1234"
    And confirmo la contraseña "Clave1234"
    And valido el captcha
    And hago clic en el botón de "Registrarse"
    Then se crea la cuenta y se envía un correo para activarla

  Scenario: Registro fallido sin correo electrónico
    Given que puedo acceder a la aplicación
    When navego a la página de registro
    And dejo sin dato en correo electrónico
    And ingreso una contraseña válida "Clave1234"
    And confirmo la contraseña "Clave1234"
    And valido el captcha
    And hago clic en el botón de "Registrarse"
    Then no se crea la cuenta y muestra un mensaje "Correo electrónico es requerido"

  Scenario: Registro fallido con contraseñas no coincidentes
    Given que puedo acceder a la aplicación
    When navego a la página de registro
    And ingreso un correo electrónico válido "rekaw87146@amxyy.com"
    And ingreso una contraseña válida "Clave1234"
    And confirmo la contraseña "Clave12345"
    And valido el captcha
    And hago clic en el botón de "Registrarse"
    Then no se crea la cuenta y muestra un mensaje "Contraseñas no coinciden"
