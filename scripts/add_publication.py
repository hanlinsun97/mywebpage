import tempfile
import os
from datetime import datetime


def sanitize_filename(title):
    """Convert title to a valid directory name"""
    return "".join(c if c.isalnum() or c in ['-', '_'] else '-'
                   for c in title.lower()).strip('-')


def format_bibtex_authors(authors):
    """Format authors for BibTeX citation"""
    return " and ".join(authors)


def format_plain_authors(authors):
    """Format authors for display, with 'Hanlin Sun' in bold"""
    formatted_authors = []
    for author in authors:
        if author.strip().lower() == "hanlin sun":
            formatted_authors.append("**Hanlin Sun**")
        else:
            formatted_authors.append(author.strip())
    return ", ".join(formatted_authors)


def create_citation_key(first_author, year, title):
    """Create citation key like 'sun2024higher'"""
    last_name = first_author.split()[-1].lower()
    title_words = title.lower().split()
    first_word = next((word for word in title_words
                      if word.lower() not in ['a', 'an', 'the']),
                      title_words[0])
    return f"{last_name}{year}{first_word}"


def create_publication():
    # Get publication details
    import os


def create_publication():
    # Other input prompts...

    # Create a temporary file for the abstract
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_file:
        print(
            f"Please enter your abstract in the following file: {temp_file.name}")
        print("Press Enter when you are done editing the abstract.")
        temp_file.close()  # Close the file so it can be opened in an editor

        # Open the temporary file in the default text editor
        # Use 'xdg-open' for Linux or 'start' for Windows
        os.system(f'open "{temp_file.name}"')

        input("Press Enter after you have finished editing the abstract...")

        # Read the abstract from the temporary file
        with open(temp_file.name, 'r', encoding='utf-8') as f:
            abstract = f.read().strip()

    # Delete the temporary file
    os.remove(temp_file.name)

    # Continue with the rest of the publication creation...
    title = input("Paper title: ").strip()
    authors = input("Full author list (comma-separated in order): ").strip()
    date = input("Publication date (YYYY-MM-DD): ").strip() + "T00:00:00Z"
    doi = input("DOI: ").strip()
    journal_name = input("Journal name (full name): ").strip()
    journal_short = input("Journal name (abbreviated): ").strip()
    abstract = input("Abstract: ").strip()
    arxiv = input("arXiv link (press enter if none): ").strip()
    pdf_link = input("PDF link (press enter if none): ").strip()

    # Process date and year
    year = date.split('-')[0]

    # Process authors
    author_list = [a.strip() for a in authors.split(",") if a.strip()]
    if not author_list:
        print("Author list cannot be empty.")
        return
    authors_yaml = "\n  - ".join(author_list)

    # Format authors for display
    other_authors = format_plain_authors(author_list)

    # Create citation
    first_author = author_list[0]
    citation_key = create_citation_key(first_author, year, title)
    bibtex_authors = format_bibtex_authors(author_list)

    # Read template
    template_path = "content/publication/.template.md"
    if not os.path.exists(template_path):
        print(f"Template file not found at {template_path}")
        return

    with open(template_path, "r", encoding='utf-8') as f:
        template = f.read()

    # Replace placeholders in Markdown
    content_md = template.replace("PAPER_TITLE", title)
    content_md = content_md.replace("OTHER_AUTHORS", authors_yaml)
    content_md = content_md.replace("YYYY-MM-DD", date)
    content_md = content_md.replace("DOI_HERE", doi)
    content_md = content_md.replace("JOURNAL_NAME", journal_name)
    content_md = content_md.replace("JOURNAL_SHORT", journal_short)
    content_md = content_md.replace("ABSTRACT_HERE", abstract)
    content_md = content_md.replace("ARXIV_LINK", arxiv if arxiv else "")
    content_md = content_md.replace("PDF_LINK", pdf_link if pdf_link else "")
    content_md = content_md.replace("CITATION_KEY", citation_key)
    content_md = content_md.replace("AUTHORS_BIB", bibtex_authors)

    # Create directory and file
    dir_name = sanitize_filename(title)
    dir_path = f"content/publication/{dir_name}"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = f"{dir_path}/index.md"
    with open(file_path, "w", encoding='utf-8') as f:
        f.write(content_md)

    print(f"\nPublication created at {file_path}")
    print(f"Citation key generated: {citation_key}")
    print("\nDon't forget to:")
    print("1. Verify the citation format")
    print("2. Add any additional links (code, slides, etc.)")
    print("3. Add featured image if needed")


if __name__ == "__main__":
    create_publication()
