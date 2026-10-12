import sys
import ollama

def summarize_file(file_path):
    try:
        # 1. Read the text file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        print(f"\n--- Processing '{file_path}' using Local LLM ---\n")

        # 2. Call the local Ollama API
        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a concise technical assistant. Summarize the provided text into 3 clear bullet points.",
                },
                {
                    "role": "user",
                    "content": content,
                },
            ],
        )

        # 3. Print the local model's output
        print("Summary:")
        print(response["message"]["content"])

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <path_to_txt_file>")
    else:
        summarize_file(sys.argv[1])