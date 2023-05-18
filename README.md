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