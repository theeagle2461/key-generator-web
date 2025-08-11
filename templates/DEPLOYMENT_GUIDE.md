# 🚀 Deployment Guide - Key Generator Web App

This guide will help you deploy your key generator web application to free hosting services so it runs 24/7 even when your PC is off.

## 🌐 Free Hosting Options

### Option 1: Render (Recommended - Easiest)
**Free Tier:** 750 hours/month (enough for 24/7)
**URL:** https://render.com

#### Steps:
1. **Sign up** for a free Render account
2. **Connect your GitHub** repository
3. **Create a new Web Service**
4. **Configure:**
   - **Build Command:** `pip install -r requirements_web.txt`
   - **Start Command:** `python app.py`
   - **Environment Variables:** None needed for basic setup

### Option 2: Railway
**Free Tier:** $5 credit monthly (usually enough for small apps)
**URL:** https://railway.app

#### Steps:
1. **Sign up** for Railway
2. **Connect GitHub** repository
3. **Deploy** automatically
4. **Set environment variables** if needed

### Option 3: Heroku (Limited Free Tier)
**Free Tier:** Discontinued, but still works with credit card
**URL:** https://heroku.com

### Option 4: PythonAnywhere
**Free Tier:** Limited but reliable
**URL:** https://www.pythonanywhere.com

## 📁 Project Structure
```
your-project/
├── app.py                 # Main Flask application
├── requirements_web.txt   # Python dependencies
├── templates/            # HTML templates
│   ├── index.html       # Main page
│   ├── keys.html        # Keys view page
│   └── stats.html       # Statistics page
├── keys.json            # Generated keys storage
├── key_usage.json       # Usage tracking
└── DEPLOYMENT_GUIDE.md  # This file
```

## 🚀 Quick Deploy to Render

### Step 1: Prepare Your Code
1. **Create a GitHub repository** and push your code
2. **Ensure all files are committed** including templates folder

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up
2. Click **"New +"** → **"Web Service"**
3. **Connect your GitHub** repository
4. **Configure the service:**
   - **Name:** `key-generator` (or any name you want)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements_web.txt`
   - **Start Command:** `python app.py`
   - **Plan:** `Free`

### Step 3: Deploy
1. Click **"Create Web Service"**
2. Wait for build to complete (usually 2-5 minutes)
3. Your app will be available at: `https://your-app-name.onrender.com`

## 🔧 Local Testing

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements_web.txt

# Run the app
python app.py

# Open browser to http://localhost:5000
```

## 📱 Features

### ✅ What You Get:
- **Beautiful Web Interface** - Generate keys from any device
- **Key Management** - View, search, and revoke keys
- **Statistics Dashboard** - Visual charts and metrics
- **24/7 Availability** - Runs even when your PC is off
- **Mobile Responsive** - Works on phones and tablets
- **Real-time Updates** - Auto-refreshing data

### 🔑 Key Types Supported:
- **Daily Keys** (1 day)
- **Weekly Keys** (7 days)
- **Monthly Keys** (30 days)
- **Lifetime Keys** (365+ days)

## 🛠️ Customization

### Change Webhook URL:
Edit `app.py` line 18:
```python
WEBHOOK_URL = "YOUR_NEW_WEBHOOK_URL_HERE"
```

### Add Authentication:
You can add basic authentication by modifying the Flask routes.

### Custom Styling:
Edit the CSS in the HTML template files to match your brand.

## 🔒 Security Notes

- **Keys are stored locally** on the hosting service
- **No user authentication** by default (add if needed)
- **Webhook logging** for monitoring usage
- **Rate limiting** can be added for production use

## 📊 Monitoring

### View Logs:
- **Render:** Dashboard → Your Service → Logs
- **Railway:** Deployments → View Logs
- **Heroku:** Dashboard → Your App → More → View Logs

### Check Status:
- **Render:** Dashboard shows uptime and status
- **Railway:** Real-time deployment status
- **Heroku:** App status in dashboard

## 🚨 Troubleshooting

### Common Issues:

1. **Build Fails:**
   - Check `requirements_web.txt` exists
   - Ensure all dependencies are listed

2. **App Won't Start:**
   - Check logs for error messages
   - Verify `app.py` has no syntax errors

3. **Templates Not Found:**
   - Ensure `templates/` folder is in root directory
   - Check file permissions

4. **Port Issues:**
   - The app automatically uses `PORT` environment variable
   - Most hosting services set this automatically

### Getting Help:
- Check the hosting service's documentation
- Look at build logs for specific error messages
- Ensure all files are committed to GitHub

## 🎯 Next Steps

After deployment:

1. **Test the web interface** - Generate some test keys
2. **Share the URL** with your team/users
3. **Monitor usage** through the statistics page
4. **Set up webhook notifications** for key activations
5. **Customize the interface** to match your needs

## 💡 Pro Tips

- **Auto-deploy:** Enable automatic deployments on GitHub push
- **Environment Variables:** Use them for sensitive configuration
- **Custom Domain:** Most services support custom domains
- **Backup:** Regularly backup your `keys.json` file
- **Monitoring:** Set up alerts for downtime

---

**🎉 Congratulations!** Your key generator is now running 24/7 in the cloud!

**Need help?** Check the hosting service's documentation or look at the build logs for specific errors.
