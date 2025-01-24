import os
from datetime import datetime


def sanitize_filename(title):
    """Convert title to valid directory name"""
    return "".join(c if c.isalnum() or c in ['-', '_'] else '-'
                   for c in title.lower()).strip('-')


def format_bibtex_authors(authors):
    """Format authors for bibtex citation"""
    return " and ".join(authors)


def create_citation_key(first_author, year):
    """Create citation key like 'sun2024'"""
    return f"{first_author.split()[-1].lower()}{year}"


def create_publication():
    # Get publication details
    title = input("Paper title: ")
    authors = input("Other authors (comma-separated, press enter if none): ")
    date = input("Publication date (YYYY-MM-DD): ")
    doi = input("DOI: ")
    journal = input("Journal name: ")
    abstract = input("Abstract: ")
    arxiv = input("arXiv link (press enter if none): ")
    pdf_link = input("PDF link (press enter if none): ")

    # Process date
    year = date.split('-')[0]

    # Create author list
    author_list = ["Hanlin Sun"]
    if authors:
        author_list.extend([a.strip() for a in authors.split(",")])
    authors_yaml = "\n- ".join(author_list)

    # Create citation
    citation_key = create_citation_key("Hanlin Sun", year)
    bibtex_authors = format_bibtex_authors(author_list)

    # Read template
    with open("content/publication/_template.md", "r") as f:
        template = f.read()

    # Replace placeholders
    content = template.replace("PAPER_TITLE", title)
    content = content.replace("OTHER_AUTHORS", authors_yaml)
    content = content.replace("YYYY-MM-DD", date)
    content = content.replace("DOI_HERE", doi)
    content = content.replace("JOURNAL_NAME", journal)
    content = content.replace("ABSTRACT_HERE", abstract)
    content = content.replace("ARXIV_LINK", arxiv if arxiv else "")
    content = content.replace("PDF_LINK", pdf_link if pdf_link else "")
    content = content.replace("DOI_LINK", f"https://doi.org/{doi}")
    content = content.replace("CITATION_KEY", citation_key)
    content = content.replace("AUTHORS_BIB", bibtex_authors)
    content = content.replace("YEAR", year)

    # Create directory and file
    dir_name = sanitize_filename(title)
    dir_path = f"content/publication/{dir_name}"

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(f"{dir_path}/index.md", "w") as f:
        f.write(content)

    print(f"\nPublication created at {dir_path}/index.md")
    print("\nDon't forget to:")
    print("1. Verify the citation format")
    print("2. Add any additional links (code, slides, etc.)")
    print("3. Add featured image if needed")


if __name__ == "__main__":
    create_publication()
