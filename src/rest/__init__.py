from flask import Flask
from configuration import environmentConfigurationDictionary

def create_application (environment_name) :
    application = Flask(__name__)
    environmentConfigurationDictionary[environment_name].init_app(application)

    from .api import mlEnvironmentTemplate as mlEnvironmentTemplate_blueprint
    application.register_blueprint(mlEnvironmentTemplate_blueprint, url_prefix='/api')

    return application