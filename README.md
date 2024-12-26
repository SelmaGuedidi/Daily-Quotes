# Daily-Quotes

This repository is automatically updated with a new inspirational quote every day, along with its sentiment analysis (positive, negative, or neutral).

**How it works:**

* A GitHub Action is triggered by a daily cron job.
* The Action fetches a new quote.
* The `sentiment_analysis.py` script analyzes the sentiment of the quote.
* The new quote and its sentiment are appended to the `quotes.txt` file.
* The Action commits and pushes the changes to the repository.
