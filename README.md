# English→Arabic Translation & Grammar Correction Tool

(https://eng2arab.streamlit.app/)

A simple and intuitive Streamlit application that lets you translate English text to Arabic and correct English grammar, powered by Hugging Face Transformers.

## 🛠️ Features

* **Translate to Arabic**: Uses the pre-trained `Helsinki-NLP/opus-mt-en-ar` model for high-quality English→Arabic translation.
* **Grammar Correction**: Leverages a fine-tuned T5 model (`vennify/t5-base-grammar-correction`) to fix grammatical errors in English sentences.
* **Dual-Mode Interface**: Perform translation and grammar correction from a single input area.
* **CI/CD**: Automated deployment to Streamlit Cloud via GitHub Actions on every push to `main`.

## 🚀 Quick Start

### Prerequisites

* Python 3.8+
* Git

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/translation-app.git
   cd translation-app
   ```
2. **Create a virtual environment** (optional but recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running Locally

```bash
streamlit run app.py
```

* Open [http://localhost:8501](http://localhost:8501) in your browser.
* Enter English text, click **Translate to Arabic** or **Check Grammar**.

## 📦 Deployment

Continuous deployment is configured via GitHub Actions:

1. Push code to the `main` branch.
2. The workflow in `.github/workflows/ci-cd.yml` installs dependencies and deploys the app to Streamlit Cloud automatically.

## 🤝 Contributing

Contributions are welcome! Fork the repo and submit a pull request.

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
