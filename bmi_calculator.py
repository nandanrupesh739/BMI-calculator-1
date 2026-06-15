"""
============================================================
  BMI Calculator - Oasis Infobyte Internship Project 2
  Python + Tkinter GUI
============================================================
"""

import tkinter as tk


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 1)


def get_category(bmi: float) -> tuple:
    if bmi < 18.5:
        return "Underweight", "#4FC3F7"
    elif bmi < 25:
        return "Normal Weight", "#66BB6A"
    elif bmi < 30:
        return "Overweight", "#FFA726"
    else:
        return "Obese", "#EF5350"


def get_health_tip(category: str) -> str:
    tips = {
        "Underweight": "💡 Eat nutrient-rich foods, increase protein intake, and consult a dietitian.",
        "Normal Weight": "✅ Great job! Maintain your weight with balanced diet and regular exercise.",
        "Overweight": "💡 Focus on portion control, increase physical activity, and reduce processed foods.",
        "Obese": "💡 Consult a healthcare provider for a personalized weight management plan.",
    }
    return tips.get(category, "")


class BMIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator — Oasis Infobyte")
        self.root.geometry("480x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#0D1117")
        self.unit = tk.StringVar(value="metric")
        self._build_ui()

    def _build_ui(self):
        # Header
        tk.Label(self.root, text="⚖️", font=("Segoe UI Emoji", 32), bg="#0D1117").pack(pady=(30,0))
        tk.Label(self.root, text="BMI Calculator", font=("Segoe UI", 22, "bold"), fg="#FFFFFF", bg="#0D1117").pack()
        tk.Label(self.root, text="Know your Body Mass Index", font=("Segoe UI", 11), fg="#8B949E", bg="#0D1117").pack()

        # Unit Toggle
        tf = tk.Frame(self.root, bg="#161B22", highlightbackground="#30363D", highlightthickness=1)
        tf.pack(pady=20, padx=40, fill="x")
        tk.Radiobutton(tf, text="Metric (kg/cm)", variable=self.unit, value="metric",
                       command=self._update_labels, font=("Segoe UI", 10), fg="#C9D1D9",
                       bg="#161B22", selectcolor="#0D1117", activebackground="#161B22").pack(side="left", padx=20, pady=10)
        tk.Radiobutton(tf, text="Imperial (lbs/in)", variable=self.unit, value="imperial",
                       command=self._update_labels, font=("Segoe UI", 10), fg="#C9D1D9",
                       bg="#161B22", selectcolor="#0D1117", activebackground="#161B22").pack(side="left", padx=20, pady=10)

        # Inputs
        inp = tk.Frame(self.root, bg="#0D1117")
        inp.pack(padx=40, fill="x")

        self.weight_label = tk.Label(inp, text="Weight (kg)", font=("Segoe UI", 11, "bold"), fg="#C9D1D9", bg="#0D1117", anchor="w")
        self.weight_label.pack(fill="x", pady=(10,4))
        self.weight_entry = tk.Entry(inp, font=("Segoe UI", 13), bg="#161B22", fg="#FFFFFF",
                                     insertbackground="#58A6FF", relief="flat", highlightbackground="#30363D", highlightthickness=1)
        self.weight_entry.pack(fill="x", ipady=10)

        self.height_label = tk.Label(inp, text="Height (cm)", font=("Segoe UI", 11, "bold"), fg="#C9D1D9", bg="#0D1117", anchor="w")
        self.height_label.pack(fill="x", pady=(16,4))
        self.height_entry = tk.Entry(inp, font=("Segoe UI", 13), bg="#161B22", fg="#FFFFFF",
                                     insertbackground="#58A6FF", relief="flat", highlightbackground="#30363D", highlightthickness=1)
        self.height_entry.pack(fill="x", ipady=10)

        tk.Label(inp, text="Age (optional)", font=("Segoe UI", 11, "bold"), fg="#C9D1D9", bg="#0D1117", anchor="w").pack(fill="x", pady=(16,4))
        self.age_entry = tk.Entry(inp, font=("Segoe UI", 13), bg="#161B22", fg="#FFFFFF",
                                  insertbackground="#58A6FF", relief="flat", highlightbackground="#30363D", highlightthickness=1)
        self.age_entry.pack(fill="x", ipady=10)

        # Button
        tk.Button(self.root, text="Calculate BMI", font=("Segoe UI", 13, "bold"),
                  fg="#FFFFFF", bg="#238636", activebackground="#2EA043", relief="flat",
                  cursor="hand2", command=self._calculate).pack(padx=40, pady=20, fill="x", ipady=12)

        # Result
        rf = tk.Frame(self.root, bg="#161B22", highlightbackground="#30363D", highlightthickness=1)
        rf.pack(padx=40, fill="x")
        self.bmi_value_label = tk.Label(rf, text="--", font=("Segoe UI", 42, "bold"), fg="#58A6FF", bg="#161B22")
        self.bmi_value_label.pack(pady=(20,4))
        self.category_label = tk.Label(rf, text="Enter your details above", font=("Segoe UI", 13), fg="#8B949E", bg="#161B22")
        self.category_label.pack()
        self.tip_label = tk.Label(rf, text="", font=("Segoe UI", 10), fg="#8B949E", bg="#161B22", wraplength=360, justify="center")
        self.tip_label.pack(pady=(4,20), padx=20)

        # BMI Scale
        sf = tk.Frame(self.root, bg="#0D1117")
        sf.pack(padx=40, pady=16, fill="x")
        tk.Label(sf, text="BMI Scale", font=("Segoe UI", 10, "bold"), fg="#8B949E", bg="#0D1117").pack(anchor="w")
        for label, color, rang in [
            ("Underweight", "#4FC3F7", "< 18.5"),
            ("Normal",      "#66BB6A", "18.5 – 24.9"),
            ("Overweight",  "#FFA726", "25 – 29.9"),
            ("Obese",       "#EF5350", "≥ 30"),
        ]:
            row = tk.Frame(sf, bg="#0D1117")
            row.pack(fill="x", pady=2)
            tk.Label(row, text="●", fg=color, bg="#0D1117", font=("Segoe UI", 12)).pack(side="left")
            tk.Label(row, text=f"{label}  {rang}", font=("Segoe UI", 10), fg="#8B949E", bg="#0D1117").pack(side="left", padx=6)

    def _update_labels(self):
        if self.unit.get() == "metric":
            self.weight_label.config(text="Weight (kg)")
            self.height_label.config(text="Height (cm)")
        else:
            self.weight_label.config(text="Weight (lbs)")
            self.height_label.config(text="Height (inches)")

    def _calculate(self):
        try:
            w = float(self.weight_entry.get())
            h = float(self.height_entry.get())
            if self.unit.get() == "imperial":
                w = w * 0.453592
                h = h * 2.54
            if w <= 0 or h <= 0:
                raise ValueError
            bmi = calculate_bmi(w, h)
            category, color = get_category(bmi)
            tip = get_health_tip(category)
            self.bmi_value_label.config(text=str(bmi), fg=color)
            self.category_label.config(text=category, fg=color)
            self.tip_label.config(text=tip)
        except ValueError:
            self.bmi_value_label.config(text="!", fg="#EF5350")
            self.category_label.config(text="Invalid input — enter positive numbers", fg="#EF5350")
            self.tip_label.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMIApp(root)
    root.mainloop()
