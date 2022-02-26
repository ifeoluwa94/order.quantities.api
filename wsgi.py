from app import init_app
import os

app_factory = init_app()

if __name__ == "__main__":
    app_factory.run(debug=True, host="0.0.0.0",
                    port=int(os.environ.get("PORT", 8080)))
