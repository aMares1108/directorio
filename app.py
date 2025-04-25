from dotenv import load_dotenv
load_dotenv()
from logging import basicConfig, DEBUG
basicConfig(filename='app.log', level=DEBUG, format='%(asctime)s: %(levelname)s: %(name)s: %(message)s', encoding='utf-8')

from app import create_app

app = create_app()

if __name__=='__main__':
    app.run(debug=True)