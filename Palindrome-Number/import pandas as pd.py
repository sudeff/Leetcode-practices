import pandas as pd
import ace_tools as tools

# Create a table of common continuous distributions and their key features
data = {
    "Distribution": ["Uniform", "Normal", "Exponential", "Gamma", "Beta", "Cauchy", "Weibull", "Pareto"],
    "PDF": [
        "f(x) = 1 / (b - a)",
        "f(x) = (1 / (σ√2π)) * e^(-(x - μ)^2 / (2σ^2))",
        "f(x) = λ e^{-λx}",
        "f(x) = (β^α / Γ(α)) x^{α-1} e^{-βx}",
        "f(x) = (1 / B(α, β)) x^{α-1}(1 - x)^{β-1}",
        "f(x) = 1 / [π(1 + x^2)]",
        "f(x) = (k / λ)(x / λ)^{k - 1} e^{-(x / λ)^k}",
        "f(x) = (α x_m^α) / x^{α + 1}"
    ],
    "Support": [
        "x ∈ [a, b]",
        "x ∈ (-∞, ∞)",
        "x ≥ 0",
        "x ≥ 0",
        "x ∈ (0, 1)",
        "x ∈ (-∞, ∞)",
        "x ≥ 0",
        "x ≥ x_m"
    ],
    "Mean": [
        "(a + b) / 2",
        "μ",
        "1 / λ",
        "α / β",
        "α / (α + β)",
        "Undefined",
        "λΓ(1 + 1/k)",
        "α x_m / (α - 1), if α > 1"
    ],
    "Variance": [
        "(b - a)^2 / 12",
        "σ^2",
        "1 / λ^2",
        "α / β^2",
        "(αβ) / ((α + β)^2(α + β + 1))",
        "Undefined",
        "λ^2[Γ(1 + 2/k) - (Γ(1 + 1/k))^2]",
        "[x_m^2 α / ((α - 1)^2(α - 2))], if α > 2"
    ],
    "Shape": [
        "Flat",
        "Bell-shaped",
        "Right-skewed",
        "Right-skewed",
        "Flexible",
        "Heavy-tailed",
        "Flexible",
        "Heavy-tailed"
    ]
}

df = pd.DataFrame(data)
tools.display_dataframe_to_user(name="Continuous Distributions Summary", dataframe=df)
