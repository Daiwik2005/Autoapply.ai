from resume_parser.extract_text import resume

print("Welcome to autoapply.ai!")

r=input("Enter your Resume file path:")
resume(r)
keyword=input("enter any  one special keyword to search(like cyber or iot (use ',' for separation )): ")
print("Searching for jobs based on the resume and keywords...")
print("Done!")
