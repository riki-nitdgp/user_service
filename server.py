from app.main import app
from app.config import AppConfig
import uvicorn


if __name__ == '__main__':
    config = AppConfig.config
    uvicorn.run(app, port=config['PORT'], host=config['HOST'], log_level='info')

