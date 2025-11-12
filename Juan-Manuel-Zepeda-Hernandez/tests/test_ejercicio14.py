from src.ejercicio14 import Servicio

def test_service(mocker):
    mock_logger = mocker.Mock()
    
    service = Servicio(logger=mock_logger)
    
    service.procesar_data()
    
    mock_logger.info.assert_called_once_with("Procesando data...")