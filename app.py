from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import uuid
import time
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# Configuration
WEBHOOK_URL = "https://discord.com/api/webhooks/1404537582804668619/6jZeEj09uX7KapHannWnvWHh5a3pSQYoBuV38rzbf_rhdndJoNreeyfFfded8irbccYB"
KEYS_FILE = "keys.json"
USAGE_FILE = "key_usage.json"

# Ensure data files exist
def init_data_files():
    if not os.path.exists(KEYS_FILE):
        with open(KEYS_FILE, 'w') as f:
            json.dump({}, f)
    
    if not os.path.exists(USAGE_FILE):
        with open(USAGE_FILE, 'w') as f:
            json.dump({}, f)

def load_keys():
    try:
        with open(KEYS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_keys(keys):
    with open(KEYS_FILE, 'w') as f:
        json.dump(keys, f, indent=2)

def load_usage():
    try:
        with open(USAGE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_usage(usage):
    with open(USAGE_FILE, 'w') as f:
        json.dump(usage, f, indent=2)

def generate_key(user_id, duration_days=30, channel_id=None):
    """Generate a new activation key"""
    keys = load_keys()
    usage = load_usage()
    
    key = str(uuid.uuid4())
    activation_time = int(time.time())
    expiration_time = activation_time + (duration_days * 24 * 60 * 60)
    
    keys[key] = {
        "user_id": user_id,
        "channel_id": channel_id,
        "activation_time": activation_time,
        "expiration_time": expiration_time,
        "is_active": True,
        "machine_id": None,
        "activated_by": None,
        "created_by": user_id,
        "duration_days": duration_days
    }
    
    usage[key] = {
        "created": activation_time,
        "activated": None,
        "last_used": None,
        "usage_count": 0
    }
    
    save_keys(keys)
    save_usage(usage)
    
    return key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'Unknown')
        duration = int(data.get('duration', 30))
        channel_id = data.get('channel_id', None)
        
        if duration < 1 or duration > 365:
            return jsonify({"success": False, "error": "Duration must be between 1 and 365 days"})
        
        key = generate_key(user_id, duration, channel_id)
        
        return jsonify({
            "success": True,
            "key": key,
            "duration": duration,
            "expires": datetime.fromtimestamp(time.time() + (duration * 24 * 60 * 60)).strftime('%Y-%m-%d %H:%M:%S')
        })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/keys')
def view_keys():
    keys = load_keys()
    usage = load_usage()
    
    # Combine keys with usage data
    key_list = []
    for key, key_data in keys.items():
        key_info = key_data.copy()
        if key in usage:
            key_info.update(usage[key])
        key_list.append(key_info)
    
    # Sort by creation time (newest first)
    key_list.sort(key=lambda x: x.get('activation_time', 0), reverse=True)
    
    return render_template('keys.html', keys=key_list)

@app.route('/api/keys')
def api_keys():
    keys = load_keys()
    usage = load_usage()
    
    key_list = []
    for key, key_data in keys.items():
        key_info = key_data.copy()
        if key in usage:
            key_info.update(usage[key])
        key_list.append(key_info)
    
    return jsonify(key_list)

@app.route('/revoke/<key>')
def revoke_key(key):
    keys = load_keys()
    
    if key in keys:
        keys[key]["is_active"] = False
        save_keys(keys)
        return jsonify({"success": True, "message": "Key revoked successfully"})
    
    return jsonify({"success": False, "error": "Key not found"})

@app.route('/stats')
def stats():
    keys = load_keys()
    usage = load_usage()
    
    total_keys = len(keys)
    active_keys = sum(1 for k in keys.values() if k["is_active"])
    revoked_keys = total_keys - active_keys
    total_usage = sum(k.get("usage_count", 0) for k in usage.values())
    
    # Count by duration
    daily_keys = sum(1 for k in keys.values() if k.get("duration_days") == 1)
    weekly_keys = sum(1 for k in keys.values() if k.get("duration_days") == 7)
    monthly_keys = sum(1 for k in keys.values() if k.get("duration_days") == 30)
    lifetime_keys = sum(1 for k in keys.values() if k.get("duration_days") >= 365)
    
    return render_template('stats.html', 
                         total_keys=total_keys,
                         active_keys=active_keys,
                         revoked_keys=revoked_keys,
                         total_usage=total_usage,
                         daily_keys=daily_keys,
                         weekly_keys=weekly_keys,
                         monthly_keys=monthly_keys,
                         lifetime_keys=lifetime_keys)

if __name__ == '__main__':
    init_data_files()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
