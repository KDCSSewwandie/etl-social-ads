Social Ads ETL & Insight Challenge

This repository contains my submission for the Data Internship ETL & Insight Challenge. The project uses a social advertisement dataset to demonstrate an ETL (Extract, Transform, Load) pipeline and generates visual insights using Python.

## Dataset

**File**: social_ads.csv
**Source**: Kaggle (Social Advertisement Dataset)
**Columns**:
  - User ID: Identifier (not used in analysis)
  - Gender: Gender of the user (not used in current version)
  - Age: Age of the user
  - EstimatedSalary: User's estimated salary
  - Purchased: Whether the user purchased (1 = Yes, 0 = No)


## Technologies Used

- **Language**: Python 3.12
- **Libraries**:
  - `pandas` – Data handling
  - `seaborn`, `matplotlib` – Data visualization
- **Tools**:
  - Git & GitHub – Version control and submission



## 🔄 ETL Pipeline Overview (`etl_pipeline.py`)

### 1. **Extract**
- Reads the raw CSV file from `data/social_ads.csv`

### 2. **Transform**
- Adds a new column `AgeGroup` by binning ages:
  - 18–25 → "18-25"
  - 26–35 → "26-35"
  - 36–45 → "36-45"
  - 46–60 → "46-60"

### 3. **Load**
- Saves the cleaned DataFrame to `data/cleaned_social_ads.csv`



## Visual Insights (`insights.py`)

Generates 4 key visualizations:

1. **Purchase Distribution**
   - `purchase_distribution.png`
   - Shows how many users purchased vs didn’t

2. **Age Distribution by Purchase**
   - `age_vs_purchase.png`
   - Histogram of age, split by purchase

3. **Estimated Salary vs Purchase**
   - `salary_vs_purchase.png`
   - Histogram of salary, split by purchase

4. **Purchase Rate by Age Group**
   - `agegroup_purchase_rate.png`
   - Average purchase rate per age group

---

##  How to Run This Project

### ✅ Clone the repository
```bash
git clone https://github.com/your-username/etl-social-ads.git
cd etl-social-ads
✅ Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate      # Windows
✅ Install the required packages
bash
Copy
Edit
pip install -r requirements.txt
✅ Run the ETL pipeline
bash
Copy
Edit
python etl_pipeline.py
✅ Run the insights/visualization script
bash
Copy
Edit
python insights.py
✅ Check generated PNGs in your project folder
📸 Sample Output Previews
Chart	Description
purchase_distribution.png	Purchase count by class (0/1)
age_vs_purchase.png	Age vs Purchase distribution
salary_vs_purchase.png	Salary vs Purchase distribution
agegroup_purchase_rate.png	Purchase rate across age groups

👩‍💻 Author
Chandima Sewvandi
Data Internship Applicant
📧 Email: sewvandichandima@gmail.com
🌐 GitHub: https://github.com/KDCSSewwandie

📌 Notes
Clean, well-commented Python code

Easy to extend for further analysis (e.g., gender-based segmentation)

Bonus features: Age group analysis added

✅ Submission
To submit this project, I’ve included:

ETL script

Insight visualizations

This README

GitHub repository as per the challenge instructions




