import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import seaborn as sns
import numpy as np
import pandas as pd

# ── Palette ──────────────────────────────────────────────────────────────────
COLORS = {
    "reading":          "#4CC9F0",   # sky blue
    "exercise":         "#F72585",   # vivid pink
    "sleeping":         "#7B2D8B",   # deep purple
    "self_improvement": "#06D6A0",   # mint green
}
BG      = "#0F0F1A"
CARD_BG = "#1A1A2E"
TEXT    = "#E8E8F0"
ACCENT  = "#FFD166"

# ── Realistic weekly data (hours / day) ─────────────────────────────────────
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

data = {
    "reading":          [1.0, 0.5, 1.5, 1.0, 0.5, 2.0, 2.5],
    "exercise":         [1.0, 0.0, 1.0, 0.5, 1.0, 1.5, 0.5],
    "sleeping":         [7.0, 6.5, 7.0, 6.5, 6.0, 8.5, 9.0],
    "self_improvement": [1.5, 2.0, 1.0, 2.5, 2.0, 1.0, 0.5],
}

df = pd.DataFrame(data, index=days)

# Self-improvement sub-categories (weekly hours total)
cs_topics = {
    "Algorithms":       8.5,
    "System Design":    5.0,
    "Problem Solving": 10.5,
}

# Monthly averages (hours / day)  – 4-week trend
weeks       = ["Week 1", "Week 2", "Week 3", "Week 4"]
monthly_avg = {
    "reading":          [1.1, 1.3, 1.4, 1.6],
    "exercise":         [0.6, 0.7, 0.8, 0.9],
    "sleeping":         [7.2, 7.0, 7.3, 7.5],
    "self_improvement": [1.4, 1.6, 1.8, 1.7],
}

# ── Figure layout ────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(18, 14), facecolor=BG)
fig.suptitle(
    "📊  Personal Habit Analysis Dashboard",
    fontsize=22, fontweight="bold", color=TEXT,
    fontfamily="DejaVu Sans", y=0.97
)

gs = gridspec.GridSpec(
    3, 3,
    figure=fig,
    hspace=0.50, wspace=0.38,
    left=0.06, right=0.96,
    top=0.92, bottom=0.06,
)

ax1 = fig.add_subplot(gs[0, :2])   # stacked bar  (wide)
ax2 = fig.add_subplot(gs[0, 2])    # pie / donut
ax3 = fig.add_subplot(gs[1, :2])   # line trend
ax4 = fig.add_subplot(gs[1, 2])    # CS sub-category bar
ax5 = fig.add_subplot(gs[2, :])    # heatmap (full width)

for ax in [ax1, ax2, ax3, ax4, ax5]:
    ax.set_facecolor(CARD_BG)
    for spine in ax.spines.values():
        spine.set_edgecolor("#2A2A4A")

# ── 1. Stacked bar – daily hours ─────────────────────────────────────────────
habits   = list(data.keys())
bar_w    = 0.55
bottoms  = np.zeros(len(days))
x        = np.arange(len(days))

for habit in habits:
    vals = np.array(data[habit])
    bars = ax1.bar(
        x, vals, bottom=bottoms, width=bar_w,
        color=COLORS[habit], label=habit.replace("_", " ").title(),
        edgecolor=BG, linewidth=0.6, alpha=0.92,
    )
    # label inside bar if tall enough
    for rect, val, bot in zip(bars, vals, bottoms):
        if val >= 0.6:
            ax1.text(
                rect.get_x() + rect.get_width() / 2,
                bot + val / 2,
                f"{val:.1f}h",
                ha="center", va="center",
                fontsize=7.5, color="white", fontweight="bold",
            )
    bottoms += vals

ax1.set_xticks(x)
ax1.set_xticklabels(days, color=TEXT, fontsize=11)
ax1.set_ylabel("Hours", color=TEXT, fontsize=11)
ax1.set_title("Daily Habit Distribution (This Week)", color=ACCENT,
              fontsize=13, fontweight="bold", pad=10)
ax1.tick_params(colors=TEXT)
ax1.yaxis.label.set_color(TEXT)
ax1.legend(
    loc="upper right", facecolor=CARD_BG, edgecolor="#2A2A4A",
    labelcolor=TEXT, fontsize=9, framealpha=0.9,
)
ax1.set_ylim(0, max(bottoms) * 1.12)
ax1.yaxis.set_tick_params(labelcolor=TEXT)

# ── 2. Donut – weekly time split ──────────────────────────────────────────────
weekly_totals = {h: sum(v) for h, v in data.items()}
labels_pie    = [k.replace("_", " ").title() for k in weekly_totals]
sizes         = list(weekly_totals.values())
cols_pie      = [COLORS[k] for k in weekly_totals]
explode       = [0.04] * len(sizes)

wedges, texts, autotexts = ax2.pie(
    sizes, labels=labels_pie, colors=cols_pie,
    autopct="%1.1f%%", pctdistance=0.78,
    startangle=140, explode=explode,
    wedgeprops=dict(width=0.55, edgecolor=BG, linewidth=1.5),
    textprops=dict(color=TEXT, fontsize=8.5),
)
for at in autotexts:
    at.set_fontsize(8)
    at.set_color(BG)
    at.set_fontweight("bold")

ax2.set_title("Weekly Time Split", color=ACCENT,
              fontsize=13, fontweight="bold", pad=10)

# ── 3. Line – 4-week trend ───────────────────────────────────────────────────
x_w = np.arange(len(weeks))
markers = ["o", "s", "D", "^"]

for (habit, vals), mk in zip(monthly_avg.items(), markers):
    ax3.plot(
        x_w, vals,
        marker=mk, markersize=8, linewidth=2.2,
        color=COLORS[habit],
        label=habit.replace("_", " ").title(),
    )
    ax3.fill_between(x_w, vals, alpha=0.10, color=COLORS[habit])

ax3.set_xticks(x_w)
ax3.set_xticklabels(weeks, color=TEXT, fontsize=11)
ax3.set_ylabel("Avg Hours / Day", color=TEXT, fontsize=11)
ax3.set_title("4-Week Progress Trend", color=ACCENT,
              fontsize=13, fontweight="bold", pad=10)
ax3.tick_params(colors=TEXT)
ax3.yaxis.set_tick_params(labelcolor=TEXT)
ax3.legend(
    facecolor=CARD_BG, edgecolor="#2A2A4A",
    labelcolor=TEXT, fontsize=9,
)
ax3.grid(axis="y", color="#2A2A4A", linestyle="--", linewidth=0.8)

# ── 4. Horizontal bar – CS sub-categories ────────────────────────────────────
cs_labels = list(cs_topics.keys())
cs_vals   = list(cs_topics.values())
cs_colors = ["#F8961E", "#43AA8B", "#277DA1"]
y_pos     = np.arange(len(cs_labels))

hbars = ax4.barh(
    y_pos, cs_vals, color=cs_colors,
    edgecolor=BG, linewidth=0.8, height=0.55,
)
for bar, val in zip(hbars, cs_vals):
    ax4.text(
        val + 0.15, bar.get_y() + bar.get_height() / 2,
        f"{val}h", va="center", color=TEXT, fontsize=10, fontweight="bold",
    )

ax4.set_yticks(y_pos)
ax4.set_yticklabels(cs_labels, color=TEXT, fontsize=10)
ax4.set_xlabel("Hours / Week", color=TEXT, fontsize=10)
ax4.set_title("CS Self-Improvement\nBreakdown (Weekly)", color=ACCENT,
              fontsize=11, fontweight="bold", pad=8)
ax4.tick_params(colors=TEXT)
ax4.xaxis.set_tick_params(labelcolor=TEXT)
ax4.set_xlim(0, max(cs_vals) * 1.25)
ax4.grid(axis="x", color="#2A2A4A", linestyle="--", linewidth=0.7)

# ── 5. Heatmap – habit intensity by day ──────────────────────────────────────
heat_df = df.T    # rows = habits, cols = days

# Normalise each habit row 0-1 for colour intensity
heat_norm = heat_df.div(heat_df.max(axis=1), axis=0)

sns.heatmap(
    heat_norm,
    ax=ax5,
    cmap="YlOrRd",
    annot=heat_df.values,
    fmt=".1f",
    linewidths=1.2,
    linecolor=BG,
    cbar_kws={"label": "Relative Intensity", "shrink": 0.6},
    annot_kws={"size": 11, "color": "#0F0F1A", "weight": "bold"},
)

ax5.set_title("Habit Intensity Heatmap (hours – normalised colour)",
              color=ACCENT, fontsize=13, fontweight="bold", pad=10)
ax5.set_xticklabels(days, color=TEXT, fontsize=11, rotation=0)
ax5.set_yticklabels(
    [h.replace("_", " ").title() for h in habits],
    color=TEXT, fontsize=11, rotation=0,
)
ax5.tick_params(axis="both", length=0)

# style colorbar
cbar = ax5.collections[0].colorbar
cbar.ax.yaxis.label.set_color(TEXT)
cbar.ax.tick_params(colors=TEXT)

# ── Footer note ───────────────────────────────────────────────────────────────
fig.text(
    0.5, 0.01,
    "Data reflects a realistic weekday/weekend pattern for a CS-focused self-improvement routine",
    ha="center", color="#888899", fontsize=9, style="italic",
)

plt.savefig(
    "/mnt/user-data/outputs/habit_analysis.png",
    dpi=160, bbox_inches="tight", facecolor=BG,
)
print("✅  Saved → habit_analysis.png")
plt.show()
