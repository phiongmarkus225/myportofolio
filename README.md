# 📊 Data Scientist Professional Portfolio

Sebuah portfolio profesional untuk Data Scientist yang dibangun dengan **Streamlit** dan siap untuk di-deploy ke **Streamlit Cloud**.

## 🌟 Fitur Utama

✅ **Home Page** - Pengenalan diri dengan statistik profesional
✅ **About Me** - Profil lengkap, pengalaman, dan pencapaian
✅ **Portfolio** - Showcase proyek-proyek terbaik dengan detail lengkap
✅ **Skills** - Technical skills dengan progress bars dan kategori
✅ **Education** - Riwayat pendidikan dan sertifikasi profesional
✅ **Contact** - Form kontak dan social media links
✅ **Responsive Design** - Tampilan sempurna di desktop dan mobile
✅ **Modern UI** - Custom CSS styling dengan gradient dan shadows

## 📁 Struktur File

```
myportofolio/
├── portofloi.py                    # Main Streamlit app
├── requirements.txt                # Python dependencies
├── README.md                       # Dokumentasi
└── .streamlit/
    └── config.toml                # Streamlit configuration
```

## 🚀 Quick Start - Menjalankan Secara Lokal

### 1. Clone Repository atau Setup Project
```bash
cd myportofolio
```

### 2. Buat Virtual Environment (Opsional tapi Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Jalankan Streamlit App
```bash
streamlit run portofloi.py
```

Aplikasi akan terbuka di `http://localhost:8501`

## 🌐 Deploy ke Streamlit Cloud

### Langkah 1: Siapkan Repository GitHub
```bash
# Inisialisasi git repository
git init
git add .
git commit -m "Initial commit: Professional Data Science Portfolio"
git remote add origin https://github.com/yourname/myportofolio.git
git push -u origin main
```

### Langkah 2: Setup Streamlit Cloud
1. Buka [Streamlit Cloud](https://share.streamlit.io/)
2. Klik **New app**
3. Pilih:
   - Repository: `yourname/myportofolio`
   - Branch: `main`
   - Main file path: `portofloi.py`
4. Klik **Deploy**

### Langkah 3: Konfigurasi (Opsional)
- Setelah deployment, Anda bisa setting advanced options
- App akan tersedia di: `https://yourname-myportofolio.streamlit.app`

## ✏️ Customization

### 1. Update Informasi Pribadi
Edit `portofloi.py` dan ganti:
- Nama dan deskripsi di section **Home**
- Pengalaman dan pencapaian di section **About Me**
- Project details di section **Portfolio**
- Informasi kontak di section **Contact**

### 2. Update Social Media Links
Cari dan ganti:
- LinkedIn URL
- GitHub URL
- Twitter/Email
- Sesuaikan dengan profile Anda

### 3. Tambah/Edit Projects
Di section **Portfolio**, tambahkan project baru dengan format:
```python
with st.expander("🔹 Project Name - Description", expanded=False):
    # Tambahkan detail project
```

### 4. Customize Theme/Warna
Edit di `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#667eea"        # Warna utama
backgroundColor = "#ffffff"     # Warna background
```

## 📊 Sections Overview

### 🏠 Home
- Greeting message
- Key expertise areas
- Quick statistics

### 👤 About Me
- Professional profile
- Experience history
- Achievements
- Stats and certifications

### 💼 Portfolio
- 5+ project showcase
- Expandable project cards
- Metrics dan results
- Tech stack per project
- Project summary table

### 🛠 Skills
- Programming languages with proficiency
- ML & AI technologies
- Data & databases
- Visualization & BI tools
- DevOps & infrastructure
- Specialized expertise

### 📜 Education
- Formal education details
- Professional certifications
- Continuous learning activities
- Speaking engagements

### 📞 Contact
- Direct contact information
- Social media links
- Contact form
- Response time info

## 🔧 Requirements

- Python 3.8+
- Streamlit 1.28.1+
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Matplotlib
- Seaborn

Semua dependencies sudah terdaftar di `requirements.txt`

## 💡 Tips & Tricks

### 1. Add Logo/Profile Picture
```python
st.image("path/to/your/image.jpg", width=250)
```

### 2. Tambah Social Media Badges
Streamlit mendukung HTML/Markdown, jadi bisa tambah badge:
```markdown
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5)](https://linkedin.com)
```

### 3. Optimize Performance
- Gunakan `@st.cache_data` untuk data besar
- Gunakan `@st.cache_resource` untuk model/object besar

### 4. Deploy Demo Data
Bisa tambah sample visualizations:
```python
import plotly.graph_objects as go
# Create charts untuk showcase
```

## 🐛 Troubleshooting

### App crash di local
```bash
# Clear cache
rm -rf .streamlit
# Atau di Windows: rmdir /s .streamlit
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Issues di Streamlit Cloud
- Check deployment logs
- Ensure all imports are in `requirements.txt`
- Verify `.streamlit/config.toml` syntax
- Check file paths (gunakan relative paths)

## 📈 Best Practices

1. **Keep it Updated** - Update projects dan skills secara berkala
2. **Add Links** - Link ke GitHub repos dan live demos
3. **Metrics Matter** - Tampilkan KPI dan hasil nyata
4. **Professional Photos** - Gunakan foto berkualitas tinggi
5. **Mobile Responsive** - Test di mobile devices
6. **Fast Loading** - Optimize images dan data
7. **SEO Friendly** - Update page title dan meta tags

## 🎓 Advance Features yang Bisa Ditambah

1. **GitHub Integration** - Auto-pull latest repos
2. **Blog Section** - Embedded Medium articles
3. **Interactive Demos** - Live model predictions
4. **Analytics** - Track visitor stats
5. **Dynamic Content** - Load dari database
6. **Authentication** - Gated content
7. **API Integration** - Pull real-time data

## 📱 Responsive Design

Portfolio ini sudah responsif untuk:
- ✅ Desktop (1920px+)
- ✅ Tablet (768px - 1024px)
- ✅ Mobile (320px - 768px)

## 🔐 Security Notes

- Jangan commit sensitive data (API keys, passwords)
- Gunakan environment variables untuk secrets
- Hide email addresses jika diperlukan
- Consider rate limiting untuk contact form

## 📞 Support & Questions

Jika ada pertanyaan atau issue:
1. Check Streamlit documentation: https://docs.streamlit.io/
2. Review Streamlit Community: https://discuss.streamlit.io/
3. Check source code comments di `portofloi.py`

## 📄 License

Free to use and modify for personal portfolio purposes.

## 🚀 Live Demo

Setelah deploy, share link Anda:
```
https://yourname-myportofolio.streamlit.app
```

---

**Built with ❤️ using Streamlit**

Happy deploying! 🎉
