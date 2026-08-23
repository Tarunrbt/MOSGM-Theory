
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar

# 18-galaxy Stable Candidate sample
d = diag_stable_18.copy()

# MOSGM interpolation variable
d["mu_x"] = 1 / (1 - np.exp(-d["x_eff"]))

galaxies = d["galaxy_id"].unique()
n_boot = 5000

seeds = [42, 7, 123, 2026, 999]

def fit_kappa(boot_d):
    def sq(k):
        pred = boot_d["g_bar"] * (
            1 + k * (boot_d["mu_x"] - 1)
        )
        lr = np.log10(pred) - np.log10(boot_d["g_obs"])
        return (lr ** 2).mean()

    result = minimize_scalar(
        sq,
        bounds=(0.01, 3.0),
        method="bounded"
    )

    return result.x


all_results = []

for seed in seeds:

    print(f"Running seed {seed}...")

    rng = np.random.default_rng(seed)
    kappa_boot = []

    for _ in range(n_boot):

        sample_gal = rng.choice(
            galaxies,
            size=len(galaxies),
            replace=True
        )

        boot_d = pd.concat(
            [d[d["galaxy_id"] == g] for g in sample_gal],
            ignore_index=True
        )

        kappa_boot.append(fit_kappa(boot_d))

    kappa_boot = np.array(kappa_boot)

    lower = np.percentile(kappa_boot, 2.5)
    upper = np.percentile(kappa_boot, 97.5)

    all_results.append({
        "seed": seed,
        "median": np.median(kappa_boot),
        "lower_95": lower,
        "upper_95": upper,
        "mean": np.mean(kappa_boot),
        "std": np.std(kappa_boot),
        "kappa_0582_excluded": not (lower <= 0.582 <= upper)
    })


results_df = pd.DataFrame(all_results)

print("\n===== BOOTSTRAP SENSITIVITY =====")
display(results_df)

print("\n===== LOWER 95% CI =====")
print(results_df["lower_95"].describe())

print(
    "\nMinimum lower CI:",
    results_df["lower_95"].min()
)

print(
    "Maximum lower CI:",
    results_df["lower_95"].max()
)

print(
    "\nκ=0.582 excluded in all seeds:",
    results_df["kappa_0582_excluded"].all()
)
