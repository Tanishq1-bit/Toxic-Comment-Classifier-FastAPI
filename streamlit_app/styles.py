def load_css():
    return """
    <style>

    /* Hide Streamlit Menu & Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main App */
    .stApp{
        background: linear-gradient(135deg,#0f172a,#1e293b);
        color: #cbd5e1;
    }

    /* Title */
    .main-title{
        text-align:center;
        font-size:42px;
        font-weight:bold;
        color:#38bdf8;
        margin-bottom:5px;
    }

    .sub-title{
        text-align:center;
        font-size:18px;
        color:#cbd5e1;
        margin-bottom:30px;
    }

    /* Cards */

    .card{
        background:#1e293b;
        padding:20px;
        border-radius:15px;
        border:1px solid #334155;
        box-shadow:0 5px 15px rgba(0,0,0,0.3);
        margin-bottom:20px;
    }

    /* Prediction Card */

    .prediction{
        font-size:30px;
        font-weight:bold;
        text-align:center;
    }

    /* Risk Cards */

    .high{
        background:#7f1d1d;
        color:white;
        padding:15px;
        border-radius:12px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
    }

    .medium{
        background:#854d0e;
        color:white;
        padding:15px;
        border-radius:12px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
    }

    .low{
        background:#14532d;
        color:white;
        padding:15px;
        border-radius:12px;
        text-align:center;
        font-size:22px;
        font-weight:bold;
    }

    /* Sidebar */

    section[data-testid="stSidebar"]{
        background:#0f172a;
    }

    /* Buttons */

    div.stButton > button{
        width:100%;
        border-radius:10px;
        height:50px;
        font-size:18px;
        font-weight:bold;
        background:#0ea5e9;
        color:white;
        border:none;
        transition:0.3s;
    }

    div.stButton > button:hover{
        background:#0284c7;
        transform:scale(1.03);
    }

    /* Text Area */

    textarea{
        font-size:18px !important;
        border-radius:10px !important;
    }

    /* Success Box */

    .success-box{
        background:#14532d;
        padding:15px;
        border-radius:12px;
        color:white;
    }

    /* Error Box */

    .error-box{
        background:#7f1d1d;
        padding:15px;
        border-radius:12px;
        color:white;
    }

    /* Footer */

    .footer{
        text-align:center;
        color:#94a3b8;
        margin-top:40px;
        font-size:15px;
    }

    </style>
    """