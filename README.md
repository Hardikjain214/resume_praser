# resume_praser
AI Resume Parser is a web application that automatically extracts key information from resumes and displays it in a structured format. The application uses Natural Language Processing (NLP) techniques to identify candidate details such as name, email, phone number, skills, education, and experience from uploaded PDF or DOCX resumes.
AI Resume Parser

An intelligent resume parsing application that extracts important candidate information from resumes and converts unstructured resume data into structured JSON format.

Features
Upload resumes in PDF or DOCX format
Extract candidate details automatically
Name
Email Address
Phone Number
Skills
Education
Experience
Clean and user-friendly interface
JSON output display
Fast and accurate parsing
Responsive design
Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python, Flask
NLP: spaCy / NLTK
File Processing: PyPDF2, pdfplumber, python-docx
How It Works
Upload a resume.
The system processes the document.
NLP models extract relevant information.
Parsed data is displayed in a structured JSON format.
Sample Output
{
  "Name": "John Doe",
  "Email": "john.doe@gmail.com",
  "Phone": "+91 9876543210",
  "Skills": [
    "Python",
    "JavaScript",
    "SQL",
    "Git"
  ]
}
Future Improvements
Experience extraction
Education timeline extraction
Resume ranking system
ATS score calculation
Multiple resume comparison
AI-powered candidate matching
Author

Hardik Jain
