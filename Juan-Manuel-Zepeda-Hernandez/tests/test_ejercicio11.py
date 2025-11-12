from src.ejercicio11 import Notificador

def test_enviar_mensaje(capfd):
    notificador = Notificador()
    notificador.enviar_mensaje("Mundo")
    captured = capfd.readouterr()
    assert captured.out == "Hola Mundo\n"