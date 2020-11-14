# flask-dance-digitalocean-oauth-example
Example of how to use Oauth with Digital Ocean and Flask-Dance

# Add Necessary Environment Variables 

The easiest way to do this is copy `.env.example` to `.env` and fill in the
necessary information.

```sh
FLASK_ENV=development
SECRET_KEY="enter your key"
DIGITALOCEAN_CLIENT_ID = "found at https://cloud.digitalocean.com/account/api/applications"
DIGITALOCEAN_CLIENT_SECRET = "found at https://cloud.digitalocean.com/account/api/applications"
```

# Run the application

`flask run`
