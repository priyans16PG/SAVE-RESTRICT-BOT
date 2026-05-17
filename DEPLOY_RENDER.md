# Deploying to Render

## Option A (Recommended): Blueprint with `render.yaml`

1. Push this repo to your GitHub account.
2. In Render, click **New +** → **Blueprint**.
3. Connect your GitHub repo and select this project.
4. Render will detect `render.yaml` and create `lockedsaver-bot` automatically.
5. Fill required environment variables in Render:
   - `BOT_TOKEN`
   - `API_ID`
   - `API_HASH`
   - `DB_URI`
   - `ADMINS`
   - `LOG_CHANNEL` (recommended; avoids startup log error)
6. Click **Apply** / **Deploy**.

## Option B: Manual Web Service Setup

1. Create a new **Web Service** on Render from your GitHub repo.
2. Use:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python bot.py`
3. Add the same environment variables listed above.
4. Deploy.

## Notes

- Do NOT commit `.env` with secrets.
- `DB_NAME` defaults to `SaveRestricted2` if not provided.
- Health endpoint is `/` via `keep_alive.py`.