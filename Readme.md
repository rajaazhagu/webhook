

This project demonstrates capturing GitHub webhook events and displaying them in a minimal UI. The project receives GitHub webhook events (push, pull request, merge) and stores them in MongoDB Atlas, then displays them via a Flask-powered web interface.

---

```
webhook-repo/
|
|-- app.py              # Flask App (backend)
|-- templates/
|   |-- index.html      # Frontend UI
|-- requirements.txt    # Python dependencies               # MongoDB Atlas connection string (secured)
```

---

### MongoDB Atlas Setup
1. Create a free cluster at [MongoDB Atlas](https://cloud.mongodb.com).
2. Create a database: `github_events` with collection `events`.
3. Copy your MongoDB URI from Atlas.
4. Update `.env` file:
```
MONGODB_URI="<your_mongodb_uri_here>"
```

---

###  Running the Application
1. Install dependencies:
```bash
pip3 install 
```

2. Run Flask app locally:
```bash
python3 app.py
```

---

### Expose App with ngrok
1. Download ngrok from [ngrok.com/download](https://ngrok.com/download).
2. Authenticate ngrok:
```bash
ngrok config add-authtoken <your-ngrok-auth-token>
```
3. Run ngrok to expose your local Flask app:
```bash
ngrok http 5000
```
4. Copy the HTTPS URL shown by ngrok (e.g., `https://abc123.ngrok.io`).

---

###  GitHub Webhook Setup
1. Go to your GitHub **action-repo**.
2. Navigate to **Settings → Webhooks → Add Webhook**.
3. Fill the webhook form:
   - **Payload URL:** `https://abc123.ngrok.io/webhook` (replace with your ngrok URL)
   - **Content Type:** `application/json`
   - **Events to trigger:**
     - Push
     -  Pull Request
4. Click **Add webhook**.

Now, GitHub will send webhook events to your app.

---

###  Features
- Receives push, pull request, and merge events.
- Saves events to MongoDB Atlas.
- Displays latest events on the web page (auto-refresh every 15 seconds).



# webhook
