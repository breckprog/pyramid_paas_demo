from pyramid.config import Configurator
from pyramid_paas import get_paas_env
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config

from .models import DBSession, Base

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """


    config = Configurator(settings=settings)
    env = get_paas_env(config)
    print env.get_postgresql_url()
    engine = create_engine(env.get_postgresql_url())
    DBSession.configure(bind=engine)
    # Create tables if they don't already exist
    Base.metadata.create_all(engine)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()

