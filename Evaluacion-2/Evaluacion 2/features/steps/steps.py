from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuración inicial
def iniciar_navegador():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@given('que puedo acceder a la aplicación')
def step_impl(context):
    context.driver = iniciar_navegador()
    context.driver.get("https://www.recorrido.cl/")
    time.sleep(2)

@when('puedo acceder al login')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Iniciar sesión").click()
    time.sleep(2)

@when('ingreso como usuario "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.ID, "user_email").send_keys(email)

@when('ingreso una clave incorrecta "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.ID, "user_password").send_keys(password)

@when('ingreso la clave correcta "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.ID, "user_password").send_keys(password)

@when('realizo el envío de los datos')
def step_impl(context):
    context.driver.find_element(By.NAME, "commit").click()
    time.sleep(3)

@then('se inicia sesión y redirecciona al dashboard "{url}"')
def step_impl(context, url):
    assert context.driver.current_url == url

@then('muestra un mensaje de "{message}"')
def step_impl(context, message):
    alert = context.driver.find_element(By.CLASS_NAME, "alert")
    assert message in alert.text

@when('dejo el campo de usuario vacío')
def step_impl(context):
    context.driver.find_element(By.ID, "user_email").clear()

@when('dejo el campo de clave vacío')
def step_impl(context):
    context.driver.find_element(By.ID, "user_password").clear()

@then('redirecciona a "{url}"')
def step_impl(context, url):
    assert context.driver.current_url == url

@then('aparece un mensaje de error "{message}"')
def step_impl(context, message):
    error = context.driver.find_element(By.CLASS_NAME, "error")
    assert message in error.text

@when('navego a la página de registro')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Regístrate").click()
    time.sleep(2)

@when('ingreso un correo electrónico válido "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.ID, "user_email").send_keys(email)

@when('ingreso una contraseña válida "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.ID, "user_password").send_keys(password)

@when('confirmo la contraseña "{password}"')
def step_impl(context, password):
    context.driver.find_element(By.ID, "user_password_confirmation").send_keys(password)

@when('valido el captcha')
def step_impl(context):
    # Aquí se debería implementar la validación del captcha
    pass

@when('hago clic en el botón de "Registrarse"')
def step_impl(context):
    context.driver.find_element(By.NAME, "commit").click()
    time.sleep(3)

@then('se crea la cuenta y se envía un correo para activarla')
def step_impl(context):
    message = context.driver.find_element(By.CLASS_NAME, "notice").text
    assert "Te hemos enviado un correo" in message

@when('dejo sin dato en correo electrónico')
def step_impl(context):
    context.driver.find_element(By.ID, "user_email").clear()

@then('no se crea la cuenta y muestra un mensaje "{message}"')
def step_impl(context, message):
    error = context.driver.find_element(By.CLASS_NAME, "error").text
    assert message in error

@when('pagina principal carga')
def step_impl(context):
    assert context.driver.title == "Recorrido.cl"

@when('ingreso ciudad de partida "{ciudad}"')
def step_impl(context, ciudad):
    context.driver.find_element(By.ID, "from-input").send_keys(ciudad)
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".suggestion").click()

@when('ingreso ciudad de llegada "{ciudad}"')
def step_impl(context, ciudad):
    context.driver.find_element(By.ID, "to-input").send_keys(ciudad)
    time.sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, ".suggestion").click()

@when('ingreso fecha de ida mañana')
def step_impl(context):
    # Seleccionar la fecha de mañana
    pass  # Implementación según el datepicker utilizado

@when('hago clic en el botón de "Buscar"')
def step_impl(context):
    context.driver.find_element(By.ID, "search-button").click()
    time.sleep(3)

@then('abre una nueva pestaña con los viajes disponibles')
def step_impl(context):
    context.driver.switch_to.window(context.driver.window_handles[1])
    assert "Resultados de búsqueda" in context.driver.title

@when('presiono fecha de ida')
def step_impl(context):
    context.driver.find_element(By.ID, "departure-date").click()

@when('escribo fecha menor a hoy "{fecha}"')
def step_impl(context, fecha):
    # Intentar seleccionar una fecha pasada
    pass  # Implementación según el datepicker utilizado

@then('no permite seleccionar día anterior a hoy')
def step_impl(context):
    # Verificar que no se pueda seleccionar la fecha
    pass

@when('selecciono la opción de "¿Olvidaste tu contraseña?"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "¿Olvidaste tu contraseña?").click()
    time.sleep(2)

@when('ingreso un correo electrónico registrado "{email}"')
def step_impl(context, email):
    context.driver.find_element(By.ID, "user_email").send_keys(email)

@then('recibo un mensaje de confirmación y un correo con las instrucciones para restablecer mi contraseña')
def step_impl(context):
    message = context.driver.find_element(By.CLASS_NAME, "notice").text
    assert "Te hemos enviado instrucciones" in message

@when('ingreso un correo electrónico no registrado')
def step_impl(context):
    context.driver.find_element(By.ID, "user_email").send_keys("correo_no_registrado@dominio.com")

@then('aparece un mensaje de error indicando que el correo no está registrado')
def step_impl(context):
    error = context.driver.find_element(By.CLASS_NAME, "error").text
    assert "no encontrado" in error

@when('hago clic en el botón de "Cerrar sesión"')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Cerrar sesión").click()
    time.sleep(2)

@then('soy redirigido a la página de inicio y mi sesión se cierra correctamente')
def step_impl(context):
    assert context.driver.current_url == "https://www.recorrido.cl/"
    context.driver.quit()
