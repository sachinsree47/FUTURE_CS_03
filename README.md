## FUTURE_CS_03

Task 3 of Future Intern in the track of Cyber Security

**Analyst:** Sachin Madhumitha Sree D  
**Tools Used:** Python Flask, PyCryptodome, GitHub, Render

---

### Task Summary

Built a secure file upload/download web portal using Flask with AES-256 encryption. Files uploaded are encrypted before storage and decrypted on-demand when downloaded. The application was deployed on Render.

---

### Deliverables

- app.py – Flask backend  
- crypto_utils.py – AES encryption logic  
- index.html – Portal UI template  
- requirements.txt – Python dependencies  
- SECURITY_OVERVIEW.md – Implementation & key management notes 
- AES_Report.pdf - Full report 
- Working_screenshots.pdf – Portal demo with UI  
- README.md – This file

---

### How to Run

```bash
# Clone the repository
git clone https://github.com/sachinsree47/FUTURE_CS_03.git
cd FUTURE_CS_03

# Install dependencies
pip install -r requirements.txt

# Set the AES key (32 bytes for AES-256)
export AES_SECRET_KEY='MyUltraSecretAES256KeyForTesting'

# Run the app
python app.py
