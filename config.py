import os


class Config(object):
    # Segredo para segurança de formulários e sessões
    SECRET_KEY = (
        os.environ.get("SECRET_KEY")
        or "RoU8GV54jSWcDNP0eEqQLsmZa6bKuxBtyHfhJdFnpMwzvT1YCl37IXgAi2kr"
    )

    # Configurações do Banco de Dados
    # Substitua 'nome_do_usuario', 'senha', 'nome_do_banco_de_dados' pelas suas informações reais
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost/psicologia"  # "mysql+pymysql://nome_do_usuario:senha@localhost/nome_do_banco_de_dados"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Outras configurações globais podem ser adicionadas aqui
