# Sentiment Analysis Web App 😊😒👌❤️😍😁😎😀😉

<div align="center">
  <p><strong>🎯 An Intelligent Sentiment Analysis Tool Powered by NLP & Machine Learning</strong></p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/NLP-TextBlob%20%26%20VADER-green?style=flat-square" alt="NLP">
  <img src="https://img.shields.io/badge/Web-Flask-lightgrey?style=flat-square" alt="Web Framework">
  <img src="https://img.shields.io/badge/License-MIT-red?style=flat-square" alt="License">
</div>

---

## 📌 About this App

Welcome to the **Sentiment Analysis Web App** – a smart, user-friendly tool designed to understand the emotions behind text and online content. 

This application is powered by **Natural Language Processing (NLP)** and **Machine Learning (ML)** algorithms that classify text into different sentiments such as **positive, negative, or neutral**. To make it even more engaging, the results are represented using expressive emojis 😊😢😍😠, helping users instantly grasp the mood conveyed by the text.

### 🎯 Key Purpose
- Analyze sentiment from user input or web content
- Perform real-time sentiment classification
- Web scrape content from URLs for sentiment analysis
- Display results with emojis for better readability and engagement

---

## ✨ Key Features

✅ **Text Sentiment Analysis** - Type or paste any text, and the app will instantly predict its sentiment.

✅ **URL Sentiment Analysis** - Provide a website link, and the app performs web scraping to fetch the content & analyze its sentiment.

✅ **Emoji-Based Results** - Sentiments are displayed with expressive emojis for instant visual understanding:
  - 😊 Positive sentiment
  - 😢 Negative sentiment  
  - 😐 Neutral sentiment

✅ **Fast & Accurate Predictions** - Leverages ML algorithms for quick and reliable sentiment classification.

✅ **Versatile Application** - Perfect for analyzing reviews, customer feedback, blog posts, social media comments, or any text content.

---

## 📊 How It Works

### 1. **Input Methods**
   - **Direct Text Input**: Paste or type text directly into the application
   - **URL Input**: Provide a website URL for web scraping and sentiment analysis

### 2. **Processing Pipeline**
   - Text preprocessing and cleaning
   - Feature extraction using NLP techniques
   - Sentiment classification using trained ML models
   - Emoji mapping for sentiment visualization

### 3. **Output**
   - Sentiment label (Positive/Negative/Neutral)
   - Confidence score
   - Visual emoji representation
   - Sentiment breakdown (if applicable)

---

## 📸 Screenshots

### 🏠 Home Page
The main interface where users can input text or URL
![Home Page](Screenshots/home.png)

### 📊 Results Page  
Displays sentiment analysis results with emoji indicators
![Results Page](Screenshots/hh.png)

### ℹ️ About Us Page
Project information and documentation
![About Us Page](Screenshots/about.png)

---

## 🛠️ Tech Stack

**Backend & NLP:**
- **Python 3.8+** - Core programming language
- **TextBlob** - Simplified NLP library for sentiment analysis
- **VADER (Valence Aware Dictionary & sEntiment Reasoner)** - Lexicon-based sentiment analyzer
- **BeautifulSoup** - Web scraping library
- **Requests** - HTTP library for fetching web content

**Web Framework:**
- **Flask** - Lightweight Python web framework
- **HTML/CSS** - Frontend markup and styling
- **JavaScript** - Client-side interactivity

**Additional Tools:**
- **NLTK** - Natural Language Toolkit for text processing
- **Pandas** - Data manipulation and analysis

---

## 📋 Table of Contents

1. [Features](#-key-features)
2. [How It Works](#-how-it-works)
3. [Screenshots](#-screenshots)
4. [Tech Stack](#️-tech-stack)
5. [Installation & Setup](#-installation--setup)
6. [Usage](#-usage)
7. [Project Structure](#-project-structure)
8. [Future Improvements](#-future-improvements)
9. [Contributing](#-contributing)
10. [License](#-license)
11. [Author](#-author)

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/HarshChoudhary2003/sentiment-analysis-webapp.git
   cd sentiment-analysis-webapp
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python Sentiment.py
   ```

5. **Access the App**
   - Open your browser and navigate to: `http://localhost:5000`

---

## 🚀 Usage

### Method 1: Analyze Text Sentiment
1. Enter any text in the input box
2. Click the **"Analyze"** button
3. Get sentiment instantly with emoji representation

### Method 2: Analyze URL Content
1. Paste a URL in the input field
2. The app will scrape the webpage content
3. Analyze sentiment of the extracted text
4. View results with confidence scores

### Example Use Cases
- **Customer Reviews**: Analyze product reviews to understand customer satisfaction
- **Social Media Monitoring**: Track sentiment in tweets, comments, and posts
- **Feedback Analysis**: Process customer feedback for sentiment trends
- **Blog Sentiment**: Analyze the tone of blog articles or news content
- **Survey Responses**: Process open-ended survey answers

---

## 📁 Project Structure

```
sentiment-analysis-webapp/
├── Sentiment.py              # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── Screenshots/              # Application screenshots
│   ├── home.png             # Home page screenshot
│   ├── hh.png               # Results page screenshot
│   └── about.png            # About page screenshot
├── templates/               # HTML templates
│   ├── index.html           # Home page
│   ├── results.html         # Results page
│   └── about.html           # About page
└── static/                  # Static files
    ├── css/                 # Stylesheets
    └── js/                  # JavaScript files
```

---

## 🔮 Future Improvements

- [ ] Multi-language sentiment analysis support
- [ ] Real-time sentiment dashboard
- [ ] Historical sentiment tracking and analytics
- [ ] API endpoint for external integrations
- [ ] Enhanced emoji selection based on sentiment intensity
- [ ] Aspect-based sentiment analysis
- [ ] Deployment to cloud platforms (Heroku, AWS)
- [ ] Docker containerization
- [ ] Mobile app version

---

## 📊 Sentiment Classification Guide

| Sentiment | Score Range | Emoji | Description |
|-----------|-------------|-------|-------------|
| **Positive** | 0.6 - 1.0 | 😊😍😁 | Content expresses happiness, satisfaction, or positive emotions |
| **Neutral** | 0.4 - 0.6 | 😐 | Content is factual or balanced without strong emotions |
| **Negative** | 0.0 - 0.4 | 😢😠 | Content expresses sadness, anger, or negative emotions |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/improvement`)
3. **Make** your changes
4. **Commit** with clear messages (`git commit -m 'Add improvement'`)
5. **Push** to your fork (`git push origin feature/improvement`)
6. **Open** a Pull Request

### Guidelines
- Follow PEP 8 coding standards
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation if needed

---

## 📜 License

This project is open-source and licensed under the **MIT License**. See the LICENSE file for more details.

You are free to use, modify, and distribute this project as per the license terms.

---

## 👨‍💻 Author

**Harsh Choudhary**
- 📍 Location: Mandi, Himachal Pradesh, India
- 🔗 GitHub: [@HarshChoudhary2003](https://github.com/HarshChoudhary2003)
- 💼 Open to collaborations on NLP, ML, and Web Development projects

---

## 📧 Support & Contact

- **Questions?** Open an issue on [GitHub Issues](https://github.com/HarshChoudhary2003/sentiment-analysis-webapp/issues)
- **Feedback?** Feel free to reach out directly
- **Collaboration?** Let's connect and build amazing projects together!

---

## 🌟 Show Your Support

If you found this project helpful or interesting, please consider:
- ⭐ **Giving it a star** on GitHub
- 🍴 **Forking** the repository
- 💬 **Sharing** it with others
- 🐛 **Reporting bugs** or **suggesting features**

<div align="center">
  <p><strong>Made with ❤️ by Harsh Choudhary</strong></p>
  <p>Happy Sentiment Analyzing! 😊</p>
</div>
