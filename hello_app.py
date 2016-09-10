import os
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def hello():
    return "https://www.google.com/search?q=pics+of+byu+logo&espv=2&biw=1280&bih=647&tbm=isch&imgil=-bSPBp8cHmj2xM%253A%253BhkvmBNlBOG2AYM%253Bhttp%25253A%25252F%25252Falvo.dvrlists.com%25252Fbyu-logo%25252F&source=iu&pf=m&fir=-bSPBp8cHmj2xM%253A%252ChkvmBNlBOG2AYM%252C_&usg=__ibdAZEyFWvSoEH_JCy2cXn_MAMw%3D&ved=0ahUKEwi8p-nDy4PPAhUB7GMKHa8wDLcQyjcINQ&ei=B1rTV_yHFIHYjwOv4bC4Cw#imgrc=-bSPBp8cHmj2xM%3A"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
