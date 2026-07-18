import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Olist E-commerce Analytics Capstone", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium UI/UX styling
st.markdown("""
    <style>
    /* Main Background & Fonts */
    .main {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Global Card/Container styling */
    div.stAlert {
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Styled Key Metrics Card container */
    .metric-card {
        background: linear-gradient(145deg, #161b22, #0f141c);
        border: 1px solid #30363d;
        padding: 24px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }
    .metric-title {
        font-size: 0.95rem;
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .metric-value-red {
        font-size: 2.5rem;
        font-weight: bold;
        color: #ff6b6b;
    }
    .metric-value-green {
        font-size: 2.5rem;
        font-weight: bold;
        color: #3fb950;
    }
    
    /* Custom headers and text styling */
    h1, h2, h3 {
        font-weight: 700 !important;
        letter-spacing: -0.5px;
    }
    .main-title {
        background: linear-gradient(90deg, #58a6ff, #bc8cff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        margin-bottom: 5px !important;
    }
    .highlight-box {
        background-color: #161b22;
        border-left: 5px solid #58a6ff;
        padding: 15px 20px;
        border-radius: 4px 8px 8px 4px;
        margin: 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Set matplotlib/seaborn globally to dark theme matching Streamlit UI
plt.style.use("dark_background")
sns.set_theme(style="dark", rc={
    "axes.facecolor": "#161b22",
    "figure.facecolor": "#0d1117",
    "grid.color": "#21262d",
    "text.color": "#c9d1d9",
    "axes.labelcolor": "#8b949e",
    "xtick.color": "#8b949e",
    "ytick.color": "#8b949e"
})

# Sidebar Navigation
st.sidebar.markdown("""
    <div style='text-align: center; padding-bottom: 10px;'>
        <h2 style='color: #58a6ff; font-size: 1.5rem; margin-bottom: 0;'>Olist Platform</h2>
        <p style='color: #8b949e; font-size: 0.85rem;'>Analytics & ML Control Panel</p>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
page = st.sidebar.radio("📌 GO TO SECTION:", [
    "1. Project Overview & Objective", 
    "2. Exploratory Data Analysis (EDA)", 
    "3. Customer Value Tiers",
    "4. Predictive Modeling & Operational Risk",
    "5. Executive Recommendations"
])
st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Toggle sidebar width or expand charts to view more details during the presentation.")

# ----------------- PAGE 1: OVERVIEW -----------------
if page == "1. Project Overview & Objective":
    st.markdown("<h1 class='main-title'>📦 Olist E-commerce Analytics Capstone</h1>", unsafe_allow_html=True)
    st.markdown("### Strategic Operations & Data Science Framework")
    st.write("Welcome to the interactive executive platform designed for the Olist performance optimization project.")
    
    col_l, col_r = st.columns([2, 1])
    with col_l:
        st.markdown("""
        <div class='highlight-box'>
            <h4 style='margin-top: 0; color: #58a6ff;'>🎯 Core Objective</h4>
            Identify major logistical bottlenecks, analyze critical customer spend distributions, and implement an 
            advanced machine learning classifier to proactively flag delayed shipments before they damage our customer retention and brand equity.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### Key Highlights of the Pipeline:")
        st.markdown("""
        * **Customer Clustering & Tiering:** Using modern SQL segmentation tools to pinpoint top contributors.
        * **Predictive Logistics:** Transforming a reactive 'complaint-handling' shipping framework into a proactive, automated risk mitigation process.
        * **Dynamic Business Logic:** Turning complex model recall metrics into easily understandable strategies for checkout and marketing departments.
        """)
    with col_r:
        st.image("https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?q=80&w=600&auto=format&fit=crop", caption="Data-Driven Modern Logistics", use_container_width=True)

# ----------------- PAGE 2: EDA -----------------
elif page == "2. Exploratory Data Analysis (EDA)":
    st.markdown("<h1 class='main-title'>📊 Exploratory Data Analysis (EDA)</h1>", unsafe_allow_html=True)
    st.subheader("Top 5 High-Value Product Categories by Revenue")
    
    # Static mockup mimicking actual notebook database extraction
    categories = ['Health & Beauty', 'Housewares', 'Watches & Gifts', 'Bed, Bath & Table', 'Office Furniture']
    revenue = [1250000, 1100000, 950000, 890000, 720000]
    
    col_plot, col_insight = st.columns([2, 1])
    
    with col_plot:
        fig, ax = plt.subplots(figsize=(10, 5))
        colors = sns.color_palette("coolwarm", len(categories))
        sns.barplot(x=revenue, y=categories, palette=colors, ax=ax, edgecolor="#30363d")
        ax.set_xlabel("Total Platform Revenue (BRL)")
        ax.set_ylabel("Product Category")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)
        
    with col_insight:
        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
        st.info("💡 **Revenue Concentration Insight:**\n\nOur data isolates **Health & Beauty** and **Housewares** as the absolute superstar revenue drivers of the entire platform. Securing robust supply chains and strict courier guidelines for these specific segments will have the highest immediate impact on preventing customer friction.")

# ----------------- PAGE 3: CUSTOMER TIERS -----------------
elif page == "3. Customer Value Tiers":
    st.markdown("<h1 class='main-title'>💎 Customer Value Tiers (NTILE Analysis)</h1>", unsafe_allow_html=True)
    st.write("Using SQL NTILE(4) functions, we bucketed our client database into four equal spend segments to isolate core revenue drivers.")
    
    quartiles = ['Quartile 1\n(Top 25% Spenders)', 'Quartile 2', 'Quartile 3', 'Quartile 4']
    revenue_contrib = [9500000, 3100000, 1500000, 700000] 
    
    col_chart, col_stat = st.columns([2, 1])
    
    with col_chart:
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=quartiles, y=revenue_contrib, palette="Blues_r", ax=ax, edgecolor="#30363d")
        ax.set_ylabel("Total Platform Spend (BRL)")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        st.pyplot(fig)
        
    with col_stat:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🔥 Quartile 1 Concentration</div>
            <div class="metric-value-green">R$ 9.5M</div>
            <p style='margin-top: 10px; font-size: 0.9rem; color: #8b949e;'>
                Quartile 1 completely dominates platform revenue — driving nearly more than the other three quartiles combined!
            </p>
        </div>
        """, unsafe_allow_html=True)
        st.warning("⚠️ **Strategic Pivot:** Instead of high-churn marketing campaigns targeting all segments, resources should immediately prioritize VIP retention policies for Quartile 1.")

# ----------------- PAGE 4: PREDICTIVE MODELING -----------------
elif page == "4. Predictive Modeling & Operational Risk":
    st.markdown("<h1 class='main-title'>🤖 Predictive Modeling: The Differentiator</h1>", unsafe_allow_html=True)
    st.write("Addressing severe dataset imbalance (~92% on-time orders vs 8% late deliveries) using custom balanced class weights.")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        metrics = ['Baseline Recall', 'Model Recall']
        values = [0.0, 0.55]
        
        fig, ax = plt.subplots(figsize=(6, 4))
        bars = ax.bar(metrics, values, color=['#ff6b6b', '#3fb950'], width=0.4, edgecolor="#30363d")
        ax.set_ylim(0, 1.0)
        ax.set_ylabel('Recall Score')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2.0, height + 0.02, f'{height*100:.2f}%', ha='center', weight='bold', color="#c9d1d9")
        st.pyplot(fig)
        
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Baseline Recall</div>
            <div class="metric-value-red">0.00%</div>
            <p style='margin-top: 10px; font-size: 0.85rem; color: #8b949e;'>
                A naive standard model fails to flag a single late shipment.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">Optimized Recall</div>
            <div class="metric-value-green">55.00%</div>
            <p style='margin-top: 10px; font-size: 0.85rem; color: #8b949e;'>
                Our balanced model successfully uncovers over half of all delayed deliveries.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    st.info("💡 **Why Recall Over Accuracy?** A lazy baseline achieves 92% accuracy simply by guessing 'On Time' for every order, but provides 0% utility. By applying **balanced class weights**, we force the model to identify the rare late cases, turning it into an active tool for customer satisfaction.")

# ----------------- PAGE 5: RECOMMENDATIONS -----------------
elif page == "5. Executive Recommendations":
    st.markdown("<h1 class='main-title'>🚀 Strategic Executive Recommendations</h1>", unsafe_allow_html=True)
    st.write("Connecting all data pipeline discoveries to clear, practical steps to protect Olist's revenue and operations.")
    
    col_l, col_r = st.columns([1, 1])
    
    with col_l:
        st.markdown("""
        ### 💎 1. Focus on Our Best Customers
        * **Insight:** The top 25% of our customers generate almost as much revenue as the rest of the customer base combined.
        * **Action:** Shift **30% of the standard marketing budget** away from broad acquisitions and focus it on targeted loyalty programs, perks, and VIP retention campaigns.
        
        ### 🛡️ 2. Fix Shipping Expectations Early
        * **Insight:** Logistics issues can push high-value customers to abandon our platform.
        * **Action:** Embed our **55% Recall model** right into the checkout. If an order is flagged as high-risk, the system will dynamically add a **2-to-3-day buffer** to the estimated delivery date on-screen to keep customer expectations realistic from day one.
        """)
        
    with col_r:
        st.markdown("""
        ### 📦 3. Support Our Superstar Categories
        * **Insight:** Our sales volume and platform growth are heavily carried by two specific powerhouse categories: **Health & Beauty** and **Housewares**.
        * **Action:** Prioritize logistics resources and establish strict carrier guidelines (SLAs) specifically for these segments to keep fulfillment fast and secure.
        """)
        
        st.markdown("---")
        st.success("🎯 **Business Summary:** Deploying these workflows enables Olist to systematically protect its primary revenue sources while scaling operations smoothly.")
