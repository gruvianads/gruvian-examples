import requests

from flask import Flask, jsonify, render_template

app = Flask(__name__)


# Route to serve ad data
@app.route("/api/ad")
def serve_ad_data():

    token = "<Auth Token>"  # Replace with your actual token
    headers = {"Authorization": f"Bearer {token}"}
    data = {"network_id": 0}  # Replace with your actual network_id
    ad_server_url = "https://api.gruvian.com/auctions"
    response = requests.post(ad_server_url, headers=headers, json=data)
 
    if response.status_code != 201:
        return jsonify({}), response.status_code
   
    ad_data = response.json()
    if ad_data.get("filled", False):
        ad = ad_data["winners"][0]["ad"]
    else: # Default Ad
        ad = {
                'description': {
                    'data': 'Grow your business by advertising on Learn-C.org. Reach developers, students, and enthusiasts for as little as $15 per 1000 visitors', 
                    'type': 'text'
                }, 
                'link_to': {
                    'data': 'https://advertisers.gruvian.com/preview/learn-c', 
                    'type': 'url'
                }, 
                'logo_image': {
                    'data': {
                        'alt': 'alt text',
                        'url': 'https://lh5.googleusercontent.com/proxy/1kSRxfD16cVW-UzLwRmpGbTRzEA7Usdw9gOVPiAFpTQ7NgCwqWrz3zdsP1eJs90FRbqwp3VJ6aYJQe4kp76u8-8dHHAWczgSb09b2qazP6Ep6foqCQ'
                    }, 
                    'type': 'image'
                }, 
                'title': {
                    'data': 'Sponsor Learn-C.org', 
                    'type': 'text'
                }
            }

    return jsonify(ad)


# Route to serve the main page
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
