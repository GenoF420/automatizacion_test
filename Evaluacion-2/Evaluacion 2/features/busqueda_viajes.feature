Feature: Búsqueda de viajes

  Scenario: Buscar viajes disponibles
    Given que puedo acceder a la aplicación
    When pagina principal carga
    And ingreso ciudad de partida "Santiago"
    And ingreso ciudad de llegada "La Serena"
    And ingreso fecha de ida mañana
    And hago clic en el botón de "Buscar"
    Then abre una nueva pestaña con los viajes disponibles

  Scenario: Seleccionar fecha anterior a hoy
    Given que puedo seleccionar fecha
    When presiono fecha de ida
    And escribo fecha menor a hoy "30/08/2024"
    Then no permite seleccionar día anterior a hoy
