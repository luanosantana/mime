from mime.container import Container
from mime.web.routes import create_app


if __name__ == "__main__":
    container = Container()
    app = create_app()

    app.run(host="0.0.0.0")
