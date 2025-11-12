# file_crypto.py
import streamlit as st

def encrypt(text, key):
    """Encrypt text using a simple Caesar cipher."""
    encrypted = ""
    for char in text:
        encrypted += chr((ord(char) + key) % 256)  # wrap within byte range
    return encrypted

def decrypt(text, key):
    """Decrypt text using the same Caesar cipher."""
    decrypted = ""
    for char in text:
        decrypted += chr((ord(char) - key) % 256)
    return decrypted

def run():
    st.title("🔐 File Encryption & Decryption Tool")

    mode = st.radio("Select mode:", ["Encrypt", "Decrypt"])
    key = st.number_input("Enter key (number)", min_value=1, step=1)

    uploaded_file = st.file_uploader("Upload a file", type=None)

    if uploaded_file is not None:
        file_content = uploaded_file.read().decode("latin-1")  # Keep encoding compatible

        if mode == "Encrypt":
            if st.button("Encrypt File"):
                encrypted_text = encrypt(file_content, key)
                st.success("✅ File encrypted successfully!")
                st.download_button(
                    label="⬇ Download Encrypted File",
                    data=encrypted_text.encode("latin-1"),
                    file_name=uploaded_file.name + ".enc",
                    mime="text/plain"
                )

        elif mode == "Decrypt":
            if st.button("Decrypt File"):
                decrypted_text = decrypt(file_content, key)
                st.success("✅ File decrypted successfully!")
                st.download_button(
                    label="⬇ Download Decrypted File",
                    data=decrypted_text.encode("latin-1"),
                    file_name=uploaded_file.name.replace(".enc", "") + "_decrypted.txt",
                    mime="text/plain"
                )
