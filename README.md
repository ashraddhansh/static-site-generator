# Static Site Generator

A Python-based static site generator built as part of the Boot.dev course. This project converts Markdown files into fully functional HTML websites with a customizable template system.

## Overview

This static site generator takes Markdown content files and converts them into HTML pages using a template. It recursively processes all Markdown files in your content directory, applies consistent styling through a shared template, and manages static assets like CSS and images.

## Features

- **Markdown to HTML Conversion**: Converts Markdown files to HTML with full support for block and inline formatting
- **Template System**: Uses a single HTML template to generate consistent page layouts across your site
- **Recursive Processing**: Automatically processes all Markdown files in nested directories
- **Static Asset Management**: Copies CSS, images, and other static files to the output directory

## Project Structure

```
.
├── build.sh              # Build script to generate the site
├── main.sh               # Main shell script entry point
├── test.sh               # Test runner script
├── template.html         # HTML template used for all pages
├── content/              # Markdown source files
│   ├── index.md
│   ├── blog/
│   │   ├── glorfindel/
│   │   ├── majesty/
│   │   └── tom/
│   └── contact/
├── docs/                 # Generated HTML output
├── static/               # Static assets (CSS, images)
│   ├── index.css
│   └── images/
└── src/                  # Python source code
    ├── main.py           # Main entry point
    ├── generate_page.py  # Page generation logic
    ├── block_markdown.py # Block-level Markdown parsing
    ├── inline_markdown.py# Inline Markdown parsing
    ├── htmlnode.py       # HTML node representation
    ├── textnode.py       # Text node representation
    ├── parentnode.py     # Parent node representation
    └── test_*.py         # Test files
```

## Getting Started

### Prerequisites

- Python 3.14+ (I used virtual environment)

### Building the Site

Run the build script:

```bash
./build.sh
```

This will:
1. Copy all static files (CSS, images) to the `docs/` directory
2. Process all Markdown files in the `content/` directory
3. Generate corresponding HTML files in the `docs/` directory

### Customizing the Build

You can specify a custom base path when running the generator:

```bash
python3 src/main.py "/"
```

This is useful when deploying to a subdirectory.

## How It Works

### 1. Content Creation

Create Markdown files in the `content/` directory. Each file must start with an H1 header (`# Title`):

```markdown
# My Page Title

This is the page content...
```

### 2. Template System

The `template.html` file defines the page layout. It uses placeholders that the generator replaces:

- `{{ Title }}` - Replaced with the H1 header from the Markdown
- `{{ Content }}` - Replaced with the converted HTML content
- `{{ basepath }}` - Replaced with the configured base path for links and assets

### 3. Generation Process

The generator:
1. Reads your Markdown files
2. Parses them into a block and inline structure
3. Converts them to HTML
4. Injects the content into the template
5. Writes the final HTML to the `docs/` directory

### 4. Asset Management

Static files in the `static/` directory are automatically copied to `docs/`, maintaining the same directory structure.

## Directory Mapping

Content directories are mapped to output directories:

```
content/blog/glorfindel/index.md  ->  docs/blog/glorfindel/index.html
content/contact/index.md          -> docs/contact/index.html
```

## Testing

Run the test suite:

```bash
./test.sh
```

This validates:
- Markdown parsing (block and inline)
- HTML node conversion
- Page generation logic

## Implementation Details

- **Block Markdown Parser** (`block_markdown.py`): Handles Markdown block elements (paragraphs, headings, lists, code blocks, etc.)
- **Inline Markdown Parser** (`inline_markdown.py`): Handles inline formatting (bold, italic, links, code, etc.)
- **HTML Nodes** (`htmlnode.py`, `parentnode.py`): Represent HTML elements and render them to HTML strings
- **Text Nodes** (`textnode.py`): Represent styled text fragments
