from dependency_injector import containers, providers


class Logger:
    def log(self, message: str) -> None:
        print(f"LOG: {message}")

class Servicio:
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def procesar_data(self) -> None:
        self.logger.log("Procesando data...")

class Container(containers.DeclarativeContainer):
    logger = providers.Singleton(Logger)
    servicio = providers.Factory(Servicio, logger=logger)

continer= Container()
service = continer.servicio()

service.procesar_data()