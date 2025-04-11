# Passport OCR Pipeline with FastAPI, S3, and Aurora

## 📸 Project Overview
This project is a complete OCR pipeline built in Python using FastAPI. It allows users to upload a passport image, extract key information (e.g., name and passport number) using Tesseract OCR, upload the image to AWS S3, and store the extracted data in an Aurora MySQL database.

The project is Dockerized and deployed on an AWS EC2 instance, making it cloud-ready and easily accessible via a public Swagger UI.

---

## 🔧 Technologies Used

- **Python 3.9**
- **FastAPI**
- **Tesseract OCR (`pytesseract`)**
- **Boto3** (for AWS S3 interaction)
- **PyMySQL** (for Aurora MySQL)
- **Docker**
- **AWS EC2 + S3 + RDS (Aurora MySQL)**

---

## ⚙️ How It Works
1. A user uploads a passport image via the `/extract-passport/` FastAPI endpoint.
2. The image is saved temporarily to `/tmp/`.
3. `pytesseract` extracts the text content.
4. Parsed data (like Name and Passport Number) is structured.
5. The image is uploaded to an S3 bucket.
6. Extracted data is inserted into a table in Aurora MySQL.

---

## 🏗️ Project Structure

```bash
passport-extractor/
├── app/
│   ├── main.py           # FastAPI entrypoint
│   ├── ocr_utils.py      # OCR logic using Tesseract
│   └── aws_utils.py      # S3 and Aurora integration
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🚀 Run Locally (via Docker)

1. Clone this repository:
```bash
git clone https://github.com/your-username/passport-extractor.git
cd passport-extractor
```

2. Build the Docker image:
```bash
docker build -t passport-api .
```

3. Run the container:
```bash
docker run -p 8000:8080 \
  -e AWS_ACCESS_KEY_ID=your-access-key \
  -e AWS_SECRET_ACCESS_KEY=your-secret-key \
  passport-api
```

4. Access the API at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌍 Deploy to AWS EC2

1. Launch an Amazon EC2 instance (Amazon Linux or Ubuntu)
2. Install Docker and upload the project via `scp`
3. Build and run the Docker container (same steps as above)
4. Ensure port `8000` or `8001` is open in the Security Group

---

## 📦 Sample Output
```json
{
  "data": {
    "Name": "JOHN DOE",
    "Passport_Number": "AB1234567"
  }
}
```

---

## 🔐 Notes
- Make sure to **never commit real AWS credentials**.
- Use `.env` files or secret managers for production.
- This repo uses mock keys and assumes a secure development setup.

---

## 📬 Author
**Minjin Mishka**  
Computer Science @ Constructor University  
Passionate about AI, automation, and cloud deployment.

> "Automating real-world workflows through intelligent systems."

---

## 🪪 License
This project is for educational and personal portfolio use. Please contact the author for reuse or collaboration.

