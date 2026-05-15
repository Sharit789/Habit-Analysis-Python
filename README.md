# 📊 Personal Habit Analysis Dashboard

A **Python data visualization project** that tracks and analyzes daily personal habits — Reading, Exercise, Sleeping, and CS Self-Improvement — using **Matplotlib** and **Seaborn**.

![Habit Analysis Dashboard](habit_analysis.png)

---

## 🚀 Features

- **Stacked Bar Chart** — Daily hours per habit across the week
- **Donut Chart** — Weekly time split (%) between all 4 habits
- **Line Trend Chart** — 4-week progress tracking
- **Horizontal Bar Chart** — CS self-improvement breakdown (Algorithms, System Design, Problem Solving)
- **Heatmap** — Habit intensity across each day of the week
- Dark-themed, color-coded dashboard designed for readability

---

## 🧠 Habits Tracked

| Habit | Description |
|---|---|
| 📚 **Reading** | Books, articles, technical documentation |
| 🏋️ **Exercise** | Gym, running, physical workout sessions |
| 😴 **Sleeping** | Daily sleep duration (quality sleep tracking) |
| 💻 **Self-Improvement** | CS topics — Algorithms, System Design, Problem Solving |

---

## 📁 Project Structure

```
habit-analysis/
│
├── habit_analysis.py       # Main Python script
├── habit_analysis.png      # Output dashboard image
└── README.md               # Project documentation
```

---

## 🛠️ Requirements

Make sure you have **Python 3.8+** installed, then install the dependencies:

```bash
pip install matplotlib seaborn numpy pandas
```

Or install from a requirements file:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
matplotlib
seaborn
numpy
pandas
```

---

## ▶️ How to Run

**Step 1 — Clone the repository**

```bash
git clone https://github.com/your-username/habit-analysis.git
cd habit-analysis
```

**Step 2 — Install dependencies**

```bash
pip install matplotlib seaborn numpy pandas
```

**Step 3 — Run the script**

```bash
python habit_analysis.py
```

The dashboard will be saved as `habit_analysis.png` in the same folder and displayed on screen.

---

## 📊 Sample Data Used

The data reflects a **realistic weekday/weekend pattern** for a CS-focused self-improvement routine:

### Weekly Daily Hours

| Day | Reading | Exercise | Sleeping | Self-Improvement |
|-----|---------|----------|----------|-----------------|
| Monday | 1.0h | 1.0h | 7.0h | 1.5h |
| Tuesday | 0.5h | 0.0h | 6.5h | 2.0h |
| Wednesday | 1.5h | 1.0h | 7.0h | 1.0h |
| Thursday | 1.0h | 0.5h | 6.5h | 2.5h |
| Friday | 0.5h | 1.0h | 6.0h | 2.0h |
| Saturday | 2.0h | 1.5h | 8.5h | 1.0h |
| Sunday | 2.5h | 0.5h | 9.0h | 0.5h |

### CS Self-Improvement (Weekly Total)

| Topic | Hours/Week |
|---|---|
| Problem Solving | 10.5h |
| Algorithms | 8.5h |
| System Design | 5.0h |

---

## 🎨 Color Palette

| Habit | Color | Hex |
|---|---|---|
| Reading | Sky Blue | `#4CC9F0` |
| Exercise | Vivid Pink | `#F72585` |
| Sleeping | Deep Purple | `#7B2D8B` |
| Self-Improvement | Mint Green | `#06D6A0` |

Background: Dark theme `#0F0F1A` — easy on the eyes for long study sessions.

---

## ✏️ Customize Your Own Data

To personalize the dashboard with your own habit data, edit this section in `habit_analysis.py`:

```python
# ── Realistic weekly data (hours / day) ─────────────────
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

data = {
    "reading":          [1.0, 0.5, 1.5, 1.0, 0.5, 2.0, 2.5],  # ← change these
    "exercise":         [1.0, 0.0, 1.0, 0.5, 1.0, 1.5, 0.5],
    "sleeping":         [7.0, 6.5, 7.0, 6.5, 6.0, 8.5, 9.0],
    "self_improvement": [1.5, 2.0, 1.0, 2.5, 2.0, 1.0, 0.5],
}
```

Simply replace the numbers with your own daily hours and re-run the script.

---

## 📌 Tech Stack

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-4DBFC5?style=flat)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?style=flat&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.x-150458?style=flat&logo=pandas&logoColor=white)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)

---

> *"Track your habits. Track your growth."* 🚀
