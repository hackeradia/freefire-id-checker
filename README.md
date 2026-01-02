```markdown
# Free Fire ID Checker

Simple Free Fire player ID checker that queries multiple public APIs to retrieve player information.

Features
- Real-time multiple API checking
- Colorful Kali Linux style output
- Batch processing support
- Error handling
- Auto-parsing different API formats

Installation (Kali Linux)
```bash
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/<your-username>/freefire-id-checker.git
cd freefire-id-checker
pip3 install -r requirements.txt
chmod +x ff_checker.py
```

Usage
```bash
# Single ID check
python3 ff_checker.py 12345678

# Batch check (IDs.txt)
echo "12345678" > IDs.txt
echo "87654321" >> IDs.txt
python3 ff_checker.py -b IDs.txt

# Make executable
chmod +x ff_checker.py
./ff_checker.py 12345678
```

Notes
- Ensure the APIs used are accessible; some public endpoints may rate-limit or be offline.
- Use responsibly and follow API terms of service.
```
