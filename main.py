import ollama

# Example usage
image_path = 'image 0.png' # Replace with your image path

# Use Ollama to clean and structure the OCR output
response = ollama.chat(
    model="llama3.2-vision",
    messages=[{
      "role": "user",
      "content": "The image is a book cover. Output should be in this format - <Name of the Book>: <Name of the Author>. Do not output anything else",
      "images": [image_path]
    }],
)

# Extract cleaned text
cleaned_text = response['message']['content'].strip()
print(cleaned_text)
