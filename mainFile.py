import argparse
import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_text = md_file.read()
        html_content = markdown.markdown(markdown_text)

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Markdown to HTML')
    parser.add_argument('inputfile', type=str, help='Path to input Markdown file')
    parser.add_argument('outputfile', type=str, help='Path to output HTML file')
    args = parser.parse_args()

    input_file = args.inputfile
    output_file = args.outputfile

    if not input_file.endswith('.md'):
        print("Error: Input file must be a Markdown (.md) file")
        exit()

    if not output_file.endswith('.html'):
        print("Error: Output file must be an HTML (.html) file")
        exit()

    convert_markdown_to_html(input_file, output_file)
