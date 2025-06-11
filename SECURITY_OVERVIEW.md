# Secure File Upload/Download Portal with AES Encryption

## Objective:
Build a secure web portal to handle file uploads and downloads, ensuring confidentiality of files through AES encryption.

## Tech Stack:
- Backend: Python Flask
- Encryption: AES-256 CBC Mode (PyCryptodome)
- Deployment: Render.com Cloud Platform
- Source Control: Git & GitHub

## Security Features Implemented:

- 🔒 **AES-256 Encryption:** 
  - 32-byte key.
  - CBC Mode with random IV for each encryption.
  - Padding handled with PKCS#7.

- 🔒 Key Management (Current Demo Implementation):
  - AES-256 key is hardcoded as MyUltraSecretAES256KeyForTesting directly in code for demo purposes.
  - In real-world production deployments, this key should be securely stored as an environment variable or secrets manager (ex: AWS Secrets Manager, Azure Key Vault, etc.)
  - No key rotation or management implemented in demo version.

- 🔒 **File Handling:**
  - Files encrypted before saving to server disk.
  - Files decrypted only on-demand at download time.
  - Uploaded files isolated into `uploads/` folder.

- 🔒 **Deployment Security:**
  - HTTPS endpoint on Render.
  - Flask `debug=False` in production.
  - No hardcoded credentials.

## Limitations:
- No user authentication layer (can be future enhancement).
- No size limitation for uploads.
- Files remain accessible to anyone knowing the URL (without authentication).

## Future Improvements:
- Add user authentication (Flask-Login / OAuth).
- Database integration for user-specific file storage.
- File expiration and auto-deletion.
- Upload size limits and file type validation.
- Audit logs and monitoring.

---

## Demo Link:
[Live Portal](https://solid-space-fishstick-x5wgj56w99g6c64j5-5000.app.github.dev/)

## Repository:
[GitHub Repo Link](https://github.com/sachinsree47/FUTURE_CS_03)

