#!/home/flaskappdev/flaskappdev/flaskappenv/bin/python3.6
import flaskr

app = flaskr.create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
