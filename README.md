# 🌱 LeafScan - AI-Powered Plant Health Diagnosis & Care Advisory System

A complete **full-stack plant disease detection and agricultural care system** built using **React (Vite)** on the frontend and **FastAPI (Python)** on the backend with **Deep Learning (PyTorch/TensorFlow)** inference models.  
Enables real-time leaf image diagnosis, detailed disease prevention advisory, weather insights, and community forum collaboration, storing data in **PostgreSQL** and cloud assets in **Cloudinary**.

---

## 🧱 Tech Stack

### 🖥️ Frontend

- **Framework:** React 19 (Vite 7)
- **Styling:** Tailwind CSS v4
- **Animations:** Framer Motion & Lottie React
- **Routing:** React Router DOM v7
- **HTTP Client:** Axios
- **Icons & Visualization:** Lucide React & Recharts
- **Notifications:** React Hot Toast

### ⚙️ Backend

- **Framework:** FastAPI (Python 3.12)
- **Machine Learning / AI:** PyTorch & TensorFlow (Plant Disease Diagnosis Models)
- **Database & ORM:** PostgreSQL 15 & SQLAlchemy 2.0 (with Alembic migrations)
- **Image Storage & CDN:** Cloudinary API
- **Containerization:** Docker & Docker Compose
- **Authentication & Security:** JWT (Python-Jose) & Passlib (Bcrypt)
- **Validation:** Pydantic v2 & Pydantic Settings

---

## 📸 Screenshots

### Disease Diagnosis & Upload
![LeafScan Diagnosis](https://github.com/DevRahuL-01/LeafScan/blob/main/screenshots/diagnosis.png)

### Dashboard & Analytics
![LeafScan Dashboard](https://github.com/DevRahuL-01/LeafScan/blob/main/screenshots/dashboard.png)

---

## 📁 Project Structure

```text
LeafScan Project/
│
├── leafscan-monolithic/         # FastAPI + ML Backend
│   ├── app/                     # Main Application Package (routers, ml, services, database)
│   ├── docker-compose.yml       # PostgreSQL & pgAdmin Docker setup
│   ├── requirements.txt         # Python dependencies
│   └── .env                     # Backend environment configuration
│
├── leafscan-frontend/           # React + Vite Frontend
│   ├── src/                     # React components, pages, services, hooks
│   ├── package.json             # Frontend dependencies & scripts
│   └── vite.config.js           # Vite configuration
│
└── README.md                    # Root Project Documentation
```

---

## ⚙️ Backend Setup (FastAPI + Python)

### 🧩 Prerequisites

- **Python:** 3.10+ (Python 3.12 recommended)
- **Docker Desktop:** Installed and running (for PostgreSQL database)
- **Cloudinary Account:** For image upload integration

### 🧰 Steps to Run Backend

1. Navigate to the backend folder:

   ```bash
   cd leafscan-monolithic
   ```

2. Create and activate a Python virtual environment:

   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the PostgreSQL database container:

   ```bash
   docker-compose up -d
   ```

5. Configure your environment variables in `.env` (refer to `.env` template for `DATABASE_URL`, `CLOUDINARY_*`, and `SECRET_KEY`).

6. Run the FastAPI development server:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

📍 **Backend Server URL:** [http://localhost:8000](http://localhost:8000)  
📚 **Swagger API Documentation:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 💻 Frontend Setup (React + Vite)

### 🧩 Prerequisites

- **Node.js:** 18+ (Node 20+ recommended)
- **Package Manager:** npm / yarn / pnpm

### ⚙️ Steps to Run Frontend

1. Navigate to the frontend directory:

   ```bash
   cd leafscan-frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Configure your `.env` file with backend service endpoints:

   ```env
   VITE_BACKEND_URL=http://localhost:8000
   ```

4. Start the development server:

   ```bash
   npm run dev
   ```

📍 **Frontend Web Application URL:** [http://localhost:5173](http://localhost:5173)

---

## 🔗 Communication & Diagnostic Flow

1. **Leaf Image Upload:**
   - User uploads or captures a plant leaf image in the React frontend interface.

2. **Backend Processing & Cloud Storage:**
   - Frontend sends the image payload via Axios to FastAPI backend.
   - The backend validates, preprocesses the image, and uploads it securely to Cloudinary CDN.

3. **AI Inference & Diagnosis:**
   - Deep learning computer vision models (PyTorch/TensorFlow) process the image tensors to classify plant diseases and compute diagnosis confidence metrics.

4. **Advisory & History Persistence:**
   - Backend links diagnosis details with plant care instructions, stores historical diagnostic logs in PostgreSQL, and streams structured JSON responses back to the React UI.

---

## 🧰 Common Commands

| Task | Command | Directory |
| :--- | :--- | :--- |
| **Run backend** | `uvicorn app.main:app --reload` | `leafscan-monolithic` |
| **Start database** | `docker-compose up -d` | `leafscan-monolithic` |
| **Stop database** | `docker-compose down` | `leafscan-monolithic` |
| **Run frontend** | `npm run dev` | `leafscan-frontend` |
| **Build frontend** | `npm run build` | `leafscan-frontend` |
| **Run frontend tests** | `npm test` | `leafscan-frontend` |

---

## 🧑‍💻 Author

**Rahul Nanhore**  
*Full Stack & AI Developer*  
🌐 [LinkedIn](https://www.linkedin.com/in/rahulnanhore)  
🐙 [GitHub](https://github.com/DevRahuL-01)  

---

⭐ **If this project helped you, consider giving it a star on GitHub!**
