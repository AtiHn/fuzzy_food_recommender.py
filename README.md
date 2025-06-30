# Fuzzy Food Recommender

This project implements a **fuzzy logic system** in Python to recommend the level of food heaviness (light, moderate, or heavy) based on:

- Health level (0-100)
- Spicy preference (0-10)
- Sweet preference (0-10)
- Sour preference (0-10)

---

## 🧠 How it works

- **Inputs:**
  - Health Level (Poor, Medium, Good)
  - Spicy Preference (Low, Medium, High)
  - Sweet Preference (Low, Medium, High)
  - Sour Preference (Low, Medium, High)

- **Output:**
  - Food Recommendation (Light, Moderate, Heavy)

---

## ⚙️ How to run

Make sure you have `skfuzzy` and `matplotlib` installed:

```bash
pip install scikit-fuzzy matplotlib
```
Then run:
```
python fuzzy_food_recommender.py
```
You'll be prompted to enter your health and taste preferences.

---
## 📈 Sample Output
```
Enter your health level (0 to 100): 75
Enter your spicy preference (0 to 10): 8
Enter your sweet preference (0 to 10): 7
Enter your sour preference (0 to 10): 4
Food Recommendation Level: 8.13
```
In this example, a user with good health and high spicy and sweet preferences receives a Heavy food recommendation (value close to 10).

A plot showing the output membership function will also be displayed.

