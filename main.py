
import sys
from pathlib import Path
from modules.file_reader import read_python_file
from modules.reviewer import review_code

def main():

    if len(sys.argv) < 2:
        print("please enter the file name properly")
        print("Usage python main.py <your-filename>")
        return ()
    file_to_review = sys.argv[1]

    print(f"processing the file {file_to_review}")
    code_content = read_python_file(file_to_review)

    if code_content is not None:


        review = review_code(code_content)
        
        if review is not None:
            print("--- 🚀 CODE REVIEW START 🚀 ---")
            print(review)
            print("--- 🚀 CODE REVIEW End 🚀 ---")

            with open("result_review.txt", 'w', encoding='utf-8')as file:
                file.write(review)

        else:
            print("Failed to get Gemini_API review ")


    else:
        print(f"failed to read file{file_to_review}")


if __name__ == "__main__":
    main()


        

        