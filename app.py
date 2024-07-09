import config
app = config.app

import routes

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=5000)
    app.run(threaded=True, host=config.HOST, port=config.PORT, debug=config.DEBUG)
