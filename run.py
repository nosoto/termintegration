from app.main import app
import os

if __name__ == "__main__":
  #port = int(os.environ.get("PORT", 5000))
  #app.run(threaded=True, port=port)
  app.run(port=2555)
  
