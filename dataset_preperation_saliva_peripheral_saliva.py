import pandas as pd
import numpy as np

# ----------------------------
# Shared HLA allele pools
# ----------------------------
HLA_A = ["A*01:01", "A*02:01", "A*24:02", "A*26:01"]
HLA_B = ["B*07:02", "B*08:01", "B*15:01", "B*40:01"]
HLA_C = ["C*03:03", "C*04:01", "C*07:01", "C*12:03"]
HLA_DRB1 = ["DRB1*01:01", "DRB1*04:01", "DRB1*07:01", "DRB1*15:01"]
HLA_DQB1 = ["DQB1*02:01", "DQB1*03:01", "DQB1*05:01", "DQB1*06:03"]

BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
ETHNICITIES = ["European", "Asian", "African", "Hispanic", "Middle Eastern"]
GENDERS = ["Male", "Female"]

# ----------------------------
# Tissue Biopsy Donors
# ----------------------------
def generate_tissue_donors(n=1200):
    tissue_types = ["Skin", "Muscle", "Liver", "Lung"]
    donors = []
    for i in range(n):
        donors.append({
            "DonorID": f"T{i+1}",
            "Donor_A": np.random.choice(HLA_A),
            "Donor_B": np.random.choice(HLA_B),
            "Donor_C": np.random.choice(HLA_C),
            "Donor_DRB1": np.random.choice(HLA_DRB1),
            "Donor_DQB1": np.random.choice(HLA_DQB1),
            "BloodGroup": np.random.choice(BLOOD_GROUPS),
            "Age": np.random.randint(18, 60),
            "Gender": np.random.choice(GENDERS),
            "Ethnicity": np.random.choice(ETHNICITIES),
            "TissueType": np.random.choice(tissue_types),
            "ViabilityScore": round(np.random.uniform(0.5, 1.0), 2)  # 0.5–1.0
        })
    return pd.DataFrame(donors)

# ----------------------------
# Saliva / Cheek Swab Donors
# ----------------------------
def generate_saliva_donors(n=1200):
    donors = []
    for i in range(n):
        donors.append({
            "DonorID": f"S{i+1}",
            "Donor_A": np.random.choice(HLA_A),
            "Donor_B": np.random.choice(HLA_B),
            "Donor_C": np.random.choice(HLA_C),
            "Donor_DRB1": np.random.choice(HLA_DRB1),
            "Donor_DQB1": np.random.choice(HLA_DQB1),
            "BloodGroup": np.random.choice(BLOOD_GROUPS),
            "Age": np.random.randint(18, 60),
            "Gender": np.random.choice(GENDERS),
            "Ethnicity": np.random.choice(ETHNICITIES),
            "DNA_Quality": round(np.random.uniform(0.6, 1.0), 2),  # 0.6–1.0
            "ContaminationFlag": np.random.choice([0, 1], p=[0.9, 0.1]) # mostly clean
        })
    return pd.DataFrame(donors)

# ----------------------------
# Peripheral Blood Donors
# ----------------------------
def generate_blood_donors(n=1200):
    donors = []
    for i in range(n):
        donors.append({
            "DonorID": f"B{i+1}",
            "Donor_A": np.random.choice(HLA_A),
            "Donor_B": np.random.choice(HLA_B),
            "Donor_C": np.random.choice(HLA_C),
            "Donor_DRB1": np.random.choice(HLA_DRB1),
            "Donor_DQB1": np.random.choice(HLA_DQB1),
            "BloodGroup": np.random.choice(BLOOD_GROUPS),
            "Age": np.random.randint(18, 60),
            "Gender": np.random.choice(GENDERS),
            "Ethnicity": np.random.choice(ETHNICITIES),
            "WBC_Count": round(np.random.uniform(4.0, 11.0), 2),  # x10^9/L
            "Hemoglobin": round(np.random.uniform(12.0, 17.5), 1) # g/dL
        })
    return pd.DataFrame(donors)

# ----------------------------
# Save datasets
# ----------------------------
tissue_df = generate_tissue_donors()
saliva_df = generate_saliva_donors()
blood_df = generate_blood_donors()

tissue_df.to_csv("donors_tissue.csv", index=False)
saliva_df.to_csv("donors_saliva.csv", index=False)
blood_df.to_csv("donors_blood.csv", index=False)

print("✅ Donor datasets created:")
print("- donors_tissue.csv")
print("- donors_saliva.csv")
print("- donors_blood.csv")
