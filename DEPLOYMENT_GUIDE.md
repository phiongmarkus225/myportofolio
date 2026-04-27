# Streamlit Deployment Guide
# Panduan untuk deploy di Streamlit Cloud

## 📋 Pre-Deployment Checklist

- [ ] Update semua informasi pribadi di portofloi.py
- [ ] Replace placeholder links (LinkedIn, GitHub, Twitter)
- [ ] Ganti email address dengan email yang benar
- [ ] Update project descriptions dengan project Anda
- [ ] Test locally: `streamlit run portofloi.py`
- [ ] Push ke GitHub
- [ ] Deploy ke Streamlit Cloud

## 🔐 Secrets Management (Optional)

Jika menggunakan API keys atau sensitive data:

1. Upload ke Streamlit Cloud via Dashboard:
   - Settings → Secrets → Edit secrets
   - Format TOML:
   ```toml
   [database]
   host = "localhost"
   port = 5432
   
   [api]
   key = "your_api_key"
   ```

2. Access di code:
   ```python
   import streamlit as st
   db_host = st.secrets["database"]["host"]
   ```

## 🚀 Deployment Steps

### Step 1: Repository Setup
```bash
git init
git add .
git commit -m "Initial portfolio commit"
git branch -M main
git remote add origin https://github.com/yourname/myportofolio.git
git push -u origin main
```

### Step 2: Connect to Streamlit Cloud
1. Visit https://share.streamlit.io/
2. Login with GitHub account
3. Click "New app"
4. Select repository and branch

### Step 3: Configuration (Optional)
In Streamlit Cloud dashboard:
- Set title and description
- Enable/disable sharing
- Configure advanced settings

### Step 4: Share
Your app will be live at:
```
https://yourname-myportofolio.streamlit.app
```

## 🔄 Continuous Updates

### Update Existing Portfolio
```bash
# Make changes locally
git add .
git commit -m "Update: Added new project"
git push
# Changes auto-deploy in 1-2 minutes
```

### Rollback Changes
```bash
git revert HEAD
git push
```

## ⚠️ Common Issues & Solutions

### Issue: "ModuleNotFoundError"
**Solution:** Add missing package to requirements.txt
```bash
pip freeze > requirements.txt
git add requirements.txt
git push
```

### Issue: App crashes after deploy
**Solution:** 
- Check deployment logs in dashboard
- Verify all file paths are relative
- Ensure config.toml syntax is correct

### Issue: Slow loading
**Solution:**
- Optimize images (use smaller files)
- Cache data with @st.cache_data
- Remove unnecessary dependencies

## 💻 Local Development Best Practices

### Use virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Install dev dependencies
```bash
pip install -r requirements.txt
pip install black flake8  # Code quality tools
```

### Run with auto-reload
```bash
streamlit run portofloi.py --logger.level=debug
```

## 🌟 Optimization Tips

1. **Image Optimization**
   - Use JPG for photos (smaller than PNG)
   - Resize to max 1920px width
   - Compress with tinypng.com

2. **Code Optimization**
   ```python
   @st.cache_data
   def load_expensive_data():
       # This runs once, not on every rerun
       return data
   ```

3. **Streamlit Tips**
   - Use st.columns() for layout
   - Use st.expander() for hiding content
   - Use st.metric() for KPIs
   - Use st.dataframe() for tables

## 📊 Monitor Your App

1. **View Analytics**
   - Dashboard → View analytics
   - See traffic, usage stats, errors

2. **Setup Alerts**
   - Enable notifications for errors
   - Monitor via Streamlit Community

3. **Performance**
   - Check app load time
   - Monitor memory usage
   - Track concurrent users

## 🎯 Marketing Your Portfolio

After deployment:

1. **Share Links**
   - LinkedIn (add to profile)
   - GitHub (add to README)
   - Resume/CV

2. **Write about it**
   - Blog post on Medium
   - Tweet the link
   - Share on portfolio sites

3. **Update Regularly**
   - Add new projects quarterly
   - Update skills and certifications
   - Keep social links current

## 📞 Support Resources

- **Streamlit Docs:** https://docs.streamlit.io/
- **Community Forum:** https://discuss.streamlit.io/
- **GitHub Issues:** https://github.com/streamlit/streamlit/issues
- **Streamlit Blog:** https://blog.streamlit.io/

## ✅ Final Checklist

Before going public:
- [ ] All typos fixed
- [ ] All links working
- [ ] Images loading properly
- [ ] Mobile view tested
- [ ] Contact form working (if applicable)
- [ ] Fast load time
- [ ] SEO friendly (meta tags)
- [ ] Professional appearance
- [ ] No sensitive data exposed
- [ ] Share links working

---

Happy deploying! Your professional portfolio is ready to impress! 🚀
