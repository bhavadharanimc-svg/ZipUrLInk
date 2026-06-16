# ⚡ ZipUrLink

**Shorten. Share. Track.**

ZipUrLink is a modern URL shortening platform built with Python, Flask, and SQLite that transforms long URLs into clean, shareable links while providing real-time click analytics.

Designed for creators, marketers, students, and businesses, ZipUrLink helps users manage links efficiently and gain insights into link engagement through an intuitive analytics dashboard.

---

## 🚀 Features

* 🔗 Instantly shorten long URLs
* ⚡ Fast redirection using unique short codes
* 📊 Real-time click tracking and analytics
* 📈 Dashboard displaying total links and click counts
* 🎨 Modern responsive user interface
* 💾 Persistent storage using SQLite
* 📋 One-click copy functionality

---

## 🎯 Problem Statement

Long URLs are difficult to share across social media, emails, presentations, and messaging platforms. Additionally, users often lack visibility into how their shared links perform.

ZipUrLink solves this by providing:

* Clean, shortened URLs
* Click tracking for every link
* Centralized analytics dashboard
* Improved user experience for sharing links

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Utilities

* MD5 Hashing (Short Code Generation)

---

## 📸 Application Preview

### Home Dashboard

* URL shortening interface
* Instant link generation
* Copy-to-clipboard support

### Analytics Dashboard

* Total links created
* Total clicks tracked
* Individual link performance metrics

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/bhavadharanimc-svg/ZipUrLInk
cd url_shortener
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install flask
```

### 5. Run Application

```bash
python app.py
```

### 6. Open Browser

```text
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```text
url_shortener/
│
├── static/
│   └── logo.png
│
├── templates/
│   └── index.html
│
├── app.py
├── database.py
├── urls.db
├── requirements.txt
└── README.md
```

---

## 🔄 How It Works

1. User enters a long URL
2. A unique short code is generated
3. URL and short code are stored in SQLite
4. Users access the generated short URL
5. Click count is automatically updated
6. Analytics dashboard displays performance metrics

---

## 📊 Example

**Original URL**

```text
https://www.example.com/blog/how-to-build-a-url-shortener
```

**Shortened URL**

```text
http://127.0.0.1:5000/a1b2c3
```

---

## 🔮 Future Enhancements

* User Authentication
* Custom Short URLs
* QR Code Generation
* Link Expiration
* Advanced Analytics
* Geographic Click Tracking
* PostgreSQL Integration
* REST API Support
* Dark Mode

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

### Built using Flask

**ZipUrLink — Shorten. Share. Track.**
