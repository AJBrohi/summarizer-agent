import sys
import time
import ollama

def summarize_file(file_path):
    try:
        # 1. Read the text file content
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        print(f"\n--- Processing '{file_path}' using Local LLM ---\n")

        # Start the timer
        start_time = time.time()

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

        # End the timer
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Extract performance metrics returned by Ollama
        eval_count = response.get("eval_count", 0)  # Number of tokens generated
        eval_duration = response.get("eval_duration", 0) / 1e9  # Convert nanoseconds to seconds

        # 3. Print the local model's output
        print("Summary:")
        print(response["message"]["content"])

        print("\n--- Performance Metrics ---")
        print(f"Total time taken: {elapsed_time:.2f} seconds")
        if eval_duration > 0 and eval_count > 0:
            tokens_per_sec = eval_count / eval_duration
            print(f"Speed: {tokens_per_sec:.2f} tokens/second")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <path_to_txt_file>")
    else:
        summarize_file(sys.argv[1])