import os
import requests
from flask import Flask, request, render_template, redirect, url_for, session
from flask_dance.contrib.digitalocean import (make_digitalocean_blueprint,
                                              digitalocean)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "bd042ab3623ccee8791da7aae39e9fbf")
app.config["DIGITALOCEAN_OAUTH_CLIENT_ID"] = os.environ.get("DIGITALOCEAN_OAUTH_CLIENT_ID")
app.config["DIGITALOCEAN_OAUTH_CLIENT_SECRET"] = os.environ.get("DIGITALOCEAN_OAUTH_CLIENT_SECRET")

digitalocean_bp = make_digitalocean_blueprint(scope="read,write")
app.register_blueprint(digitalocean_bp, url_prefix="/")


@app.route('/', methods=['GET'])
def index():
    if digitalocean.authorized:
        return redirect(url_for("droplets"))
    error = request.args.get('error', None)

    return render_template(
        'index.html',
        oauth_url=url_for("digitalocean.login"),
        error=error
    )


@app.route('/droplets', methods=['GET'])
def droplets():
    error = None
    try:
        token = digitalocean.access_token
        headers = {"Authorization": f"Bearer {token}"}
        api_droplet_list_url = "https://api.digitalocean.com/v2/droplets"

        servers = requests.get(api_droplet_list_url, headers=headers,
                               timeout=3).json()
        return render_template(
            'server_list.html',
            oauth_url=url_for("digitalocean.login"),
            servers=servers.get('droplets', None)
        )
    except TypeError as e:
        error = f'Error: {e}'
        print(error)
    return redirect(url_for('.index', error=error))
