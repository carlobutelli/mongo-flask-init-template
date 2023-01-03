import os


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'this-really-needs-to-be-changed')
    SWAGGER = {
        "swagger_version": "2.0",
        "title": "FIT - Flask Init Template",
        "headers": [
            ("Access-Control-Allow-Origin", '*'),
            ("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"),
            ("Access-Control-Allow-Credentials", "true"),
        ]
    }
    MONGODB_DATABASE_HOST = os.environ.get("MONGODB_DATABASE_HOST",
                                           "mongodb://0.0.0.0:27018/?retryWrites=true&w=majority")
    MONGODB_USER = os.environ.get("MONGODB_USER")
    MONGODB_USER_PASSWORD = os.environ.get("MONGODB_USER_PASSWORD")
    MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE')


class LocalConfig(BaseConfig):
    """Development configuration"""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(BaseConfig):
    """Test environment configuration"""
    TESTING = True


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
