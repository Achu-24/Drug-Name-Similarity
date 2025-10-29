# 💊 Drug Name Similarity Finder

### 🎯 Aim
This project helps users find the correct medicine name even if they enter it partially or with spelling mistakes.  
It uses NLP-based string similarity to suggest the most likely correct names.

---

### ⚙️ Tech Stack
- **Python**
- **Pandas**
- **FuzzyWuzzy / RapidFuzz** for similarity scoring  
- **Streamlit** for interactive UI

---

### 🧠 How It Works
1. The system reads a list of drug names from a CSV file.  
2. When the user types a drug name (even partially or incorrectly),  
   it calculates the similarity between the input and all known drug names.  
3. It then displays the **top matching results** using fuzzy string matching.

---

### 📁 Data
`data/drug_names.csv` — contains a list of real or sample medicine names.  
Example:

Paracetamol
Pantoprazole
Omeprazole
Cetirizine
Ibuprofen


---

### 🚀 How to Run

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Achu-24/Drug-Name-Similarity.git
cd Drug-Name-Similarity

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run in Terminal Mode
python src/main.py

4️⃣ Run with Streamlit UI
streamlit run src/app_streamlit.py


Then open your browser at http://localhost:8501

🧩 Example

Input:

para

Output:

Did you mean:
=> Paracetamol
=> Pantoprazole
=> Omeprazole

---ThankYou---