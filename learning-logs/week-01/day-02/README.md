# Day 2 - Data Processing & First Machine Learning Model

## 🎯 Objective
Learn how to handle messy industrial data, apply Mechanical Engineering domain knowledge (unit conversion), and train a basic Machine Learning model to predict machine failure.

## 🧠 Key Learnings & Reflections

### 1. Data Cleaning (Garbage In, Garbage Out)
If we feed raw, messy data (like text "OUT_OF_RANGE" or empty NaN values) directly into an AI, the AI will process bad "fuel" and produce useless predictions. We must clean it first using Pandas. Tools like `pd.to_numeric(errors='coerce')` and `dropna()` act like a massive, fast `if-else` statement designed specifically for processing thousands of data rows instantly.

### 2. The Mechanical Engineering Advantage (Domain Knowledge)
The factory sensor provided temperatures in Fahrenheit. A standard programmer might just feed the raw numbers into the AI. But as a Mechanical Engineer, I know that engineering formulas and material limits (like 100°C) are based on Celsius. Converting `(F - 32) * 5/9` ensures the AI learns physically accurate thresholds.

### 3. Understanding `fit()` and `predict()`
- `model.fit()` is the training phase. It calls the Scikit-Learn tool to study the patterns and categories from our cleaned historical CSV data.
- `model.predict()` is the inference phase. It takes new, unseen data and compares it against the patterns it learned during `fit()` to make a prediction.

### 4. Data Integrity vs. Human Readability
I learned that using `.round()` can actually reduce AI accuracy because it destroys data precision. Instead, we keep the raw decimal data intact for the AI, but use Pandas display formatting (`pd.options.display.float_format`) just for the output screen. This makes the data readable for humans without sacrificing AI performance.

### 5. The Human Element (Accepting Errors)
I deliberately left my messy, duplicated code in this repository. I want to look back years from now and remember the days when I struggled to copy, paste, and implement simple logic. This serves as a reminder to myself: never give up when facing errors. It is part of the journey.