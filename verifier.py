from deepface import DeepFace

def verify_faces(img1_path, img2_path):
    try:
        result = DeepFace.verify(
            img1_path,
            img2_path,
            model_name="ArcFace",
            enforce_detection=True
        )

        return {
            "verified": result["verified"],
            "distance": result["distance"],
            "threshold": result["threshold"]
        }

    except Exception as e:
        return {"error": str(e)}
