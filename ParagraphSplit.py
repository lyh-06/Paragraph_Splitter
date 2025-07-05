import pandas as pd
import re

# Paste text into the paragraph variable
# You may have to manually add a double newline or \n\n to separate paragraphs
paragraph = """paragraph 1.\n\nparagraph2."""

def split_paragraph(paragraph):
    paragraph_num = 1

    # Split paragraphs using double newline
    paragraph_list = paragraph.split("\n\n")
    abbreviations = ['Mr.', 'Mrs.', 'Dr.', 'Ms.', 'Prof.', 'Rev.', 'St.', 'e.g.', 'i.e.', 'etc.', 'vs.']

    cleaned = []

    for paragraph in paragraph_list:
        if paragraph.strip():
            temp_paragraph = paragraph
            for abbr in abbreviations:
                temp_paragraph = temp_paragraph.replace(abbr, abbr.replace('.', 'PERIOD_MARKER'))
            temp_paragraph = re.sub(r'(\d+)\.(\d+)', r'\1DECIMAL_MARKER\2', temp_paragraph)

            sentences = temp_paragraph.split('.')

            processed_sentences = []
            for s in sentences:
                if s.strip():
                    s = s.replace('PERIOD_MARKER', '.')
                    s = s.replace('DECIMAL_MARKER', '.')
                    s = s.strip()
                    if(s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
                        s = s[1:-1]
                    if("\n" in s):
                        s = s.replace("\n", " ")
                    s = s + "."
                    processed_sentences.append(s)
            for sentence in processed_sentences:
                cleaned.append({'Paragraph Number': paragraph_num, 'Excerpt': sentence.strip()})
            paragraph_num += 1
    df = pd.DataFrame(cleaned)
    return df

cleaned_df = split_paragraph(paragraph)
print(cleaned_df)
# Save to Excel file, change the name as needed
cleaned_df.to_excel('article_name.xlsx', index=False)
# The code above splits the given paragraph into sentences and saves them into a excel file.
