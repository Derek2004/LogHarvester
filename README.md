# 🪵 LogHarvester

**LogHarvester** is a lightweight Python-based log analysis tool I have designed to parse Linux-style SSH authentication logs (`auth.log`) and identify failed login attempts.

---

## 🚀 Features

- Parses `auth.log` files for failed SSH logins
- Extracts IP addresses and usernames
- Highlights suspicious activity using colored terminal output
- Easy to extend with IP reputation lookups or alerting

---

## 📁 Project Structure

LogHarvester/
├── inputs/ # Sample or actual log files
│ └── auth.log
├── reports/ # Output directory (future use)
├── logharvester.py # Main log parsing script
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🧰 Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

Install dependencies with:

```bash
pip install -r requirements.txt

⚙️ Usage
Run the parser from the project root:
python logharvester.py

Ensure inputs/auth.log exists and contains log entries such as:
Jul 27 12:34:56 localhost sshd[12345]: Failed password for invalid user admin from 192.168.1.100 port 2222 ssh2
Jul 27 12:35:01 localhost sshd[12345]: Failed password for root from 192.168.1.101 port 22 ssh2

💡 Future Enhancements
🔍 Add GeoIP lookup for attacker IPs

📊 Export analysis results to JSON or CSV

⚠️ Brute-force detection based on thresholds

🛡️ Integration with SIEM tools or alerting systems

👨‍💻 Author
Derek Namanda
