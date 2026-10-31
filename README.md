# LETICIA'S CAFE website

A responsive single-page café website with two colour themes and a working customer review form.

## Features
- Warm coffee / cream / caramel theme
- Alternative classic charcoal / neutral theme (use the theme button in the header)
- Mobile-friendly navigation and layout
- Menu, about, gallery, events and contact sections
- Customer reviews are saved in the database and shown on the same page
- Basic input validation and a hidden anti-spam field

## Run on Android / Termux

1. Install Python if needed: `pkg install python`
2. Open this project folder in Termux.
3. Create and activate a virtual environment:
   `python -m venv venv`
   `source venv/bin/activate`
4. Install packages:
   `pip install -r requirements.txt`
5. Start:
   `python app.py`
6. Open `http://127.0.0.1:5000` in your browser.

## Deploying for a real public website

This is a working starter website, but do not publish it unchanged. Before launch:
1. Replace all placeholder contact details, location, hours and menu prices with verified café information.
2. Replace the illustrative photos in `app/static/images/` with the café's own approved photos if available.
3. Set a strong, private `SECRET_KEY` environment variable.
4. Configure a persistent PostgreSQL database and set its connection string in `DATABASE_URL`. The default SQLite database is suitable for local testing, but many cloud hosts have temporary filesystems, so reviews may disappear after redeployment/restart unless persistent storage is configured.
5. Add a review moderation / reporting process and a privacy notice before accepting public submissions.
6. Test the site on phones and computers and confirm the business owner approves all wording and images.

## Images

Copy the ten supplied image files into `app/static/images/`:
`logo.png`, `coffee.png`, `interior.png`, `food.png`, `cake.png`, `milkshake.png`, `juice.png`, `customer.png`, `service.png`, `friends.png`.

The ZIP includes image placeholders only if generated image files are supplied separately; add the ten image files to the images folder before launch.
