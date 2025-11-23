from flask import Flask, request

app = Flask(__name__)

@app.route('/clicked_url', methods=['POST'])
def clicked_url():
    url = request.json.get('url')
    if url:
        print("User clicked on URL:", url)
        # You can process the URL here, such as saving it to a database or performing any other action.
        return 'Received URL'
    else:
        return 'No URL received'

if __name__ == '__main__':
    app.run(debug=True)
