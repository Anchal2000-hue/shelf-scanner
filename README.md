# Shelf Scanner 📚🤖

An AI-powered book discovery app that scans your bookshelf from a photo and identifies all your books with recommendations!

## Features

- 📸 Upload a photo of your bookshelf
- 🤖 AI identifies all visible books instantly
- 📖 Get title, author, genre, rating & summary for each book
- ⭐ Personalized reading recommendations
- ❤️ Wishlist — save books you want to read
- 📱 Works on mobile camera too

## Tech Stack

- **Python** + **Flask** (backend)
- **Groq AI** + **LLaMA 4 Scout** with Vision (book identification)
- **HTML/CSS/JavaScript** (frontend)
- **localStorage** (wishlist persistence)

## Live Demo

👉 [shelf-scanner-9of0.onrender.com](https://shelf-scanner-9of0.onrender.com)

## Run Locally

1. Clone the repo
```bash
   git clone https://github.com/Anchal2000-hue/shelf-scanner.git
   cd shelf-scanner
```

2. Install dependencies
```bash
   pip install -r requirements.txt
```

3. Create `.env` file
4. Run the app
```bash
   python app.py
```

5. Open http://127.0.0.1:5000

## How It Works

1. Upload a photo of your bookshelf
2. AI vision model scans and identifies every book
3. Get detailed info — title, author, genre, rating, summary
4. Add books to your wishlist to read later
5. Get overall collection recommendations

## Screenshots

![Shelf Scanner](https://shelf-scanner-9of0.onrender.com)

## Author

**Anchal** — [github.com/Anchal2000-hue](https://github.com/Anchal2000-hue)