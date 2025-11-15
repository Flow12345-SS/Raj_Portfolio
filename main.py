from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Rajahemed’s Portfolio Backend API",
    description="""
This API powers **Rajahemed’s Full-Stack Portfolio**.
""",
    version="1.0.5"
)

@app.get("/", response_class=HTMLResponse, tags=["Home"], summary="Rajahemed’s Portfolio Home Page")
def home():
    return """
    <html>
    <head>
        <title>Rajahemed Portfolio</title>

<style>
    body {
        margin: 0;
        font-family: Arial, sans-serif;

        /* ⭐ ONLY THIS COLOR CHANGED ⭐ */
        background: linear-gradient(135deg, #dbeafe, #e9d5ff);

        color: #4a275f;
        overflow-x: hidden;
        position: relative;
    }

    .shape {
        position: absolute;
        border-radius: 50%;
        background: rgba(200, 140, 255, 0.20);
        animation: float 6s infinite ease-in-out;
    }
    .shape1 { width: 130px; height: 130px; top: 10%; left: 15%; background: rgba(255,182,193,0.35); }
    .shape2 { width: 210px; height: 210px; top: 65%; left: 72%; background: rgba(186,232,255,0.35); }
    .shape3 { width: 90px; height: 90px; top: 40%; left: 38%; background: rgba(255,200,255,0.30); }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-35px); }
        100% { transform: translateY(0px); }
    }

    .typewriter {
        font-size: 42px;
        font-weight: bold;
        white-space: nowrap;
        overflow: hidden;
        border-right: 4px solid #b30086;
        width: 0;
        animation: typing 4s steps(25) forwards, blink 0.7s infinite;
        color: #b30086;
    }
    @keyframes typing { from { width: 0; } to { width: 430px; } }
    @keyframes blink { 50% { border-color: transparent; } }

    .profile {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 4px solid #d63384;
        margin-bottom: 15px;
        object-fit: cover;
        box-shadow: 0 0 18px #ff80bf;
    }

    .btn, .github-btn {
        padding: 12px 25px;
        margin: 10px;
        background: white;
        border: 2px solid #d63384;
        color: #d63384;
        border-radius: 8px;
        cursor: pointer;
        font-size: 18px;
        transition: 0.3s;
        box-shadow: 0 0 10px #ffb3d9;
    }
    .btn:hover, .github-btn:hover {
        background: #ffedf7;
        transform: scale(1.05);
        box-shadow: 0 0 18px #ff80bf;
    }

    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        width: 60%;
        margin: 20px auto;
        border: 2px solid #ffb3d9;
        box-shadow: 0 0 15px #ffd6e9;
        cursor: pointer;
    }

    h2 {
        color: #b30086;
        text-shadow: 0 0 8px #ffd6e9;
    }

    .social-icons a {
        margin: 10px;
        font-size: 30px;
        color: #b30086;
        text-decoration: none;
        transition: 0.3s;
    }
    .social-icons a:hover {
        color: #ff1493;
        text-shadow: 0 0 12px #ff80bf;
    }

    .modal {
        display: none;
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        backdrop-filter: blur(8px);
        background: rgba(0,0,0,0.4);
    }

    .modal-content {
        background: white;
        padding: 25px;
        border-radius: 15px;
        width: 50%;
        margin: 10% auto;
        border: 2px solid #ffb3d9;
        color: #4a275f;
        animation: popup 0.4s ease;
        box-shadow: 0 0 25px #ff80bf;
    }

    .github-btn {
        background: #000;
        color: white;
        font-size: 16px;
        margin-top: 15px;
    }
</style>

</head>

<body>

<div class="shape shape1"></div>
<div class="shape shape2"></div>
<div class="shape shape3"></div>

<div class="section">

    <img class="profile" src="https://photos.app.goo.gl/4DkN1NJL1hr5F9E57" />

    <div class="typewriter">Rajahemed Kotekhan</div>

    <p>AI/ML Engineer • Software Developer • Data Analyst</p>

    <div class="social-icons" style="margin-top: 15px;">

        <a href="https://github.com/Rajahemed" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733609.png" width="38" />
        </a>

        <a href="https://linkedin.com/in/rajahemed-kotekhan" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="38" />
        </a>

    </div>

<div id="about" class="section">
    <h2>👨‍💻 About Me</h2>
    <div class="card">
        Hi, I’m <b>Rajahemed Kotekhan</b> — ML Engineer & Developer building real-world AI solutions.
    </div>
</div>

<div id="skills" class="section">
    <h2>💡 Skills</h2>
    <div class="card">
        Python • FastAPI • ML • CNN • SQL • Docker • Data Engineering
    </div>
</div>

<div id="projects" class="section">
    <h2>🚀 My Projects</h2>

    <div class="card" onclick="openModal('sugarcane')">
        <h3>🍃 Sugarcane Leaf Disease Detection</h3>
        <p>CNN • Deep Learning • Streamlit</p>
    </div>

    <div class="card" onclick="openModal('quantum')">
        <h3>⚛️ Quantum AI for Drug Discovery</h3>
        <p>Qiskit • PennyLane • FastAPI</p>
    </div>

    <div class="card" onclick="openModal('powerbi')">
        <h3>📊 Meta Ads Performance Dashboard</h3>
        <p>Power BI • DAX • Data Analytics</p>
    </div>

    <div class="card" onclick="openModal('inventory')">
        <h3>📦 Inventory Management System</h3>
        <p>PHP • MySQL • Web App</p>
    </div>
</div>

<div id="modal" class="modal">
    <div class="modal-content">
        <span class="close" onclick="closeModal()">✖</span>
        <h2 id="modal-title"></h2>
        <p id="modal-text"></p>

        <a id="github-link" href="#" target="_blank">
            <button class="github-btn">🔗 View on GitHub</button>
        </a>
    </div>
</div>

<script>
function scrollToSection(id) {
    document.getElementById(id).scrollIntoView({ behavior: "smooth" });
}

function openModal(project) {
    const title = document.getElementById('modal-title');
    const text = document.getElementById('modal-text');
    const link = document.getElementById('github-link');
    const modal = document.getElementById('modal');

    if (project === "sugarcane") {
        title.innerHTML = "🍃 Sugarcane Leaf Disease Detection";
        text.innerHTML = "• 92% accuracy TensorFlow CNN model.<br>• Streamlit web app.<br>• Tools: TensorFlow, Streamlit.";
        link.href = "https://github.com/Rajahemed";
    }

    if (project === "quantum") {
        title.innerHTML = "⚛️ Quantum AI for Drug Discovery";
        text.innerHTML = "• Qiskit + PennyLane model.<br>• RDKit for molecules.<br>• 65% faster screening.";
        link.href = "https://github.com/Rajahemed";
    }

    if (project === "powerbi") {
        title.innerHTML = "📊 Meta Ads Performance Dashboard";
        text.innerHTML = "• Power BI dashboard.<br>• CTR, CPC, ROI analysis.";
        link.href = "https://github.com/Rajahemed";
    }

    if (project === "inventory") {
        title.innerHTML = "📦 Inventory Management System";
        text.innerHTML = "• PHP + MySQL app.<br>• Auto reorder alerts.";
        link.href = "https://github.com/Rajahemed";
    }

    modal.style.display = "block";
}

function closeModal() {
    document.getElementById('modal').style.display = "none";
}
</script>

</body>
</html>
"""
