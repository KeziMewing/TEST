from flask import Flask, redirect, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Check the User-Agent header
    if 'Roblox' in request.headers.get('User-Agent', ''):
        # Fetch the Lua code from GitHub
        lua_url = 'https://raw.githubusercontent.com/KeziMewing/MG/refs/heads/main/KeziMiniGamesRank'
        try:
            response = requests.get(lua_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.text  # Return the Lua code
        except requests.RequestException:
            return 'Error fetching the Lua code.', 500  # Handle fetch error
    else:
        # Redirect browser users to Discord
        return redirect('https://discord.gg/NaCE9GX33Z')

if __name__ == '__main__':
    app.run(debug=True)
