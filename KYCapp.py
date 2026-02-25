import streamlit as st
import os
from verifier import verify_faces

st.title("🏦 Face Recognition KYC Verification")

st.write("Upload ID photo and Selfie to verify identity")

id_image = st.file_uploader("Upload ID Card Photo", type=["jpg", "png"])
selfie_image = st.camera_input("Take a Selfie")

if id_image and selfie_image:

    os.makedirs("temp", exist_ok=True)

    id_path = os.path.join("temp", id_image.name)
    selfie_path = os.path.join("temp", selfie_image.name)

    with open(id_path, "wb") as f:
        f.write(id_image.read())

    with open(selfie_path, "wb") as f:
        f.write(selfie_image.read())

    st.image([id_path, selfie_path], caption=["ID Image", "Selfie"])

    if st.button("Verify Identity"):

        with st.spinner("Verifying..."):

            result = verify_faces(id_path, selfie_path)

        if "error" in result:
            st.error(result["error"])
        else:
            if result["verified"]:
                st.success("✅ Identity Verified")
            else:
                st.error("❌ Identity Not Matched")

            st.write("Distance:", result["distance"])
            st.write("Threshold:", result["threshold"])
