from board.model import Base, engine
from board.setapp import create_app

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    app = create_app()
    app.run(debug=True)
