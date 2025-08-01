# 🧠 Product Recommendation System

A simple, user-based recommendation system built with **Python** and **scikit-learn**.  
It uses **cosine similarity** to recommend products to users based on the preferences of similar users.

--------------------------------------------------------------------------------------------------------------------

## 📌 What It Does

- Uses user-product rating data to build a **user-product matrix**
- Computes **user similarity** using cosine similarity
- Recommends products that similar users have rated highly
- Text-based interface to test recommendations for different user IDs

------------------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack

- Python
- Pandas
- scikit-learn (for cosine similarity)

------------------------------------------------------------------------------------------------------------

## 🧪 Sample Data
This project includes a small hardcoded dataset with:
- 3 Users
- 5 Products
- Ratings between 1–5
```python
'UserID': [1, 1, 1, 2, 2, 2, 3, 3, 3],
'Product': ['Product A', 'Product B', ..., 'Product E'],
'Rating': [4, 5, ..., 2]

--------------------------------------------------------------------------------------------------

**▶️ How to Run**
1. Clone the repository
git clone https://github.com/your-username/product-recommendation-system.git
2. Install dependencies
pip install pandas scikit-learn
3. Run the script
python recommendation_sys.py
Then enter a User ID like 1, 2, or 3 when prompted.

--------------------------------------------------------------------------------------------------
**🧠 How It Works**
->Creates a user-product rating matrix
->Calculates similarity between users using cosine similarity
->Predicts weighted ratings for unrated products
->Recommends the top N highest predicted ratings

--------------------------------------------------------------------------------------------------
**📁 File Structure**
product-recommendation-system/
├── recommendation_sys.py   # Main Python script
└── README.md               # Project documentation

----------------------------------------------------------------------------------------------------
**👩‍💻 Author**
Crafted with curiosity 🚀 by Sahithi — turning ideas into code, one project at a time.

-----------------------------------------------------------------------------------------------------
**📄 License**
This project is open-source and available under the MIT License.
