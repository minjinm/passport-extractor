from fastapi import FastAPI, UploadFile, File
from app.ocr_utils import extract_passport_data
from app.aws_utils import upload_to_s3, insert_to_aurora
import traceback

# ✅ Define the FastAPI app BEFORE using it
app = FastAPI()

@app.post("/extract-passport/")
async def extract_passport(file: UploadFile = File(...)):
    try:
        image_path = f"/tmp/{file.filename}"
        with open(image_path, "wb") as f:
            f.write(await file.read())

        print(f"📸 Saved image to {image_path}")

        data, raw_text = extract_passport_data(image_path)
        print("🧠 Extracted data:", data)

        s3_url = upload_to_s3(image_path, "myfirstbucket00282905", file.filename)
        print("✅ Uploaded to S3:", s3_url)

        insert_to_aurora(data, {
            "host": "database-2-instance-1.cl46c0agmnre.eu-central-1.rds.amazonaws.com",
            "user": "admin",
            "password": "Nn99211737",
            "database": "passport_data"
        })
        print("🗃️ Inserted into Aurora")


        return {
            "data": data,
            "s3_url": s3_url
        }

    except Exception as e:
        print("🔥 ERROR:", str(e))
        traceback.print_exc()
        return {"error": "Internal Server Error"}
