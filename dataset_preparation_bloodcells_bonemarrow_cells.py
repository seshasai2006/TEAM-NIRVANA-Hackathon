import pandas as pd
import numpy as np

# Shared HLA pools
HLA_A = ["A*01:01", "A*02:01", "A*24:02", "A*26:01"]
HLA_B = ["B*07:02", "B*08:01", "B*15:01", "B*40:01"]
HLA_C = ["C*03:03", "C*04:01", "C*07:01", "C*12:03"]
HLA_DRB1 = ["DRB1*01:01", "DRB1*04:01", "DRB1*07:01", "DRB1*15:01"]
HLA_DQB1 = ["DQB1*02:01", "DQB1*03:01", "DQB1*05:01", "DQB1*06:03"]

BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
ETHNICITIES = ["European", "Asian", "African", "Hispanic", "Middle Eastern"]
GENDERS = ["Male", "Female"]

# ----------------------------
# Blood Cell Donors
# ----------------------------
def generate_bloodcell_donors(n=1200):
    donors = []
    for i in range(n):
        donors.append({
            "DonorID": f"BC{i+1}",
            "Donor_A": np.random.choice(HLA_A),
            "Donor_B": np.random.choice(HLA_B),
            "Donor_C": np.random.choice(HLA_C),
            "Donor_DRB1": np.random.choice(HLA_DRB1),
            "Donor_DQB1": np.random.choice(HLA_DQB1),
            "BloodGroup": np.random.choice(BLOOD_GROUPS),
            "Age": np.random.randint(18, 60),
            "Gender": np.random.choice(GENDERS),
            "Ethnicity": np.random.choice(ETHNICITIES),
            "RBC_Count": round(np.random.uniform(4.0, 6.0), 2),   # million/µL
            "Platelet_Count": round(np.random.uniform(150, 400), 0), # x10⁹/L
            "MCV": round(np.random.uniform(80, 100), 1)          # fL
        })
    return pd.DataFrame(donors)

# ----------------------------
# Bone Marrow Donors
# ----------------------------
def generate_bonemarrow_donors(n=1200):
    donors = []
    for i in range(n):
        donors.append({
            "DonorID": f"BM{i+1}",
            "Donor_A": np.random.choice(HLA_A),
            "Donor_B": np.random.choice(HLA_B),
            "Donor_C": np.random.choice(HLA_C),
            "Donor_DRB1": np.random.choice(HLA_DRB1),
            "Donor_DQB1": np.random.choice(HLA_DQB1),
            "BloodGroup": np.random.choice(BLOOD_GROUPS),
            "Age": np.random.randint(18, 60),
            "Gender": np.random.choice(GENDERS),
            "Ethnicity": np.random.choice(ETHNICITIES),
            "CD34_Count": round(np.random.uniform(2.0, 10.0), 2),   # x10⁶/kg
            "EngraftmentScore": round(np.random.uniform(0.5, 1.0), 2),
            "ViabilityPercent": round(np.random.uniform(80, 100), 1) # %
        })
    return pd.DataFrame(donors)

# ----------------------------
# Save CSVs
# ----------------------------
bloodcell_df = generate_bloodcell_donors()
bonemarrow_df = generate_bonemarrow_donors()

bloodcell_df.to_csv("donors_bloodcells.csv", index=False)
bonemarrow_df.to_csv("donors_bonemarrow.csv", index=False)

print("✅ Donor datasets created:")
print("- donors_bloodcells.csv")
print("- donors_bonemarrow.csv")