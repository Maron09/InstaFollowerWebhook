# InstaFollowerWebhook

This is a simple Flask application that serves as a webhook endpoint. It receives incoming JSON payloads and prints them to the console. Additionally, it responds with a JSON message confirming the receipt of the event.
<hr>
<strong>Prerequisites</strong>
<li>Python 3.x</li>
<li>Flask</li>
<hr>
<strong>Installation</strong>
<br>
<li>Clone the repository or download the source code:</li>

<code>git clone <repository_url></code>
<br>
<li>Navigate to the project directory:</li>

<code>cd <project_directory></code>
<br>
<li>Install the required dependencies using pip:</li>

<code>pip install -r requirements.txt</code>
<br>
<strong>Usage</strong>
<br>
<li>Start the Flask server:</li>

<code>python app.py</code>
<br>
<li>By default, the application runs on http://localhost:5000/.</li>

<li>Send a POST request to the server with a JSON payload:</li>


<code>curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://localhost:5000/</code>
<br>
<li>The application will print the received JSON payload to the console.</li>
<br>
<strong>Configuration</strong>
You can modify the Flask application by editing the app.py file. Here are some aspects you might want to customize:

<li>Debug mode: By default, the application runs in debug mode. To disable it, change the following line in app.py:</li>

<code>app.run(debug=True)</code>
<li>Route: The webhook endpoint is currently set to '/'. If you want to use a different endpoint, modify the route decorator in app.py:</li>

<code>@app.route('/your/endpoint', methods=['POST'])</code>
<br>
<strong>License</strong>
This project is licensed under the MIT License.

Feel free to adjust and expand the README file to suit your specific needs. Make sure to include any additional instructions or information that would be helpful to users interacting with your Flask application.
