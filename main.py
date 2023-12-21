from src.infrastructure.app import create_app

app = create_app()

if __name__ == "__main__":
    from flask_injector import FlaskInjector
    from src.infrastructure.app import AppModule
    
    FlaskInjector(app=app, modules=[AppModule])

    app.run(debug=True, port=8080)