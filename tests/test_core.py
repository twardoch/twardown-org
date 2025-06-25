"""Tests for the twardown core module.

this_file: tests/test_core.py
"""


from markdown import Markdown
from twardown.core import (BoldInlineProcessor, CodeBlockProcessor,
                           CodeInlineProcessor, ImageInlineProcessor,
                           ItalicInlineProcessor, LinkInlineProcessor,
                           ListBlockProcessor, TwardownExtension)


def test_process_text_basic():
    """Test basic text processing."""
    assert process_text("Hello, world!") == "Hello, world!"


# Add more tests here as you implement more features.  For example:

# def test_process_text_bold():
#     assert process_text("This is *bold* text.") == "This is <strong>bold</strong> text."


def test_inserted_text():
    markdown_text = "This is ++inserted text++."
    expected_html = "<p>This is <ins>inserted text</ins>.</p>"
    html = markdown.markdown(markdown_text, extensions=[TwardownExtension()])
    assert html == expected_html


def test_bold_processor() -> None:
    """Test the bold inline processor."""
    md = Markdown()
    processor = BoldInlineProcessor(md)

    # Test with double asterisks
    text = "This is **bold** text"
    html = md.convert(text)
    assert "<strong>bold</strong>" in html

    # Test with double underscores
    text = "This is __bold__ text"
    html = md.convert(text)
    assert "<strong>bold</strong>" in html


def test_italic_processor() -> None:
    """Test the italic inline processor."""
    md = Markdown()
    processor = ItalicInlineProcessor(md)

    # Test with single asterisk
    text = "This is *italic* text"
    html = md.convert(text)
    assert "<em>italic</em>" in html

    # Test with single underscore
    text = "This is _italic_ text"
    html = md.convert(text)
    assert "<em>italic</em>" in html


def test_link_processor() -> None:
    """Test the link inline processor."""
    md = Markdown()
    processor = LinkInlineProcessor(md)

    # Test basic link
    text = "This is a [link](https://example.com)"
    html = md.convert(text)
    assert '<a href="https://example.com">link</a>' in html

    # Test link with title
    text = 'This is a [link](https://example.com "Example")'
    html = md.convert(text)
    assert '<a href="https://example.com" title="Example">link</a>' in html


def test_code_processor() -> None:
    """Test the code inline processor."""
    md = Markdown()
    processor = CodeInlineProcessor(md)

    text = "This is `inline code`"
    html = md.convert(text)
    assert "<code>inline code</code>" in html


def test_image_processor() -> None:
    """Test the image inline processor."""
    md = Markdown()
    processor = ImageInlineProcessor(md)

    # Test basic image
    text = "![Alt text](image.jpg)"
    html = md.convert(text)
    assert '<img src="image.jpg" alt="Alt text"' in html

    # Test image with title
    text = '![Alt text](image.jpg "Image title")'
    html = md.convert(text)
    assert '<img src="image.jpg" alt="Alt text" title="Image title"' in html


def test_code_block_processor() -> None:
    """Test the code block processor."""
    md = Markdown()
    processor = CodeBlockProcessor(md.parser)

    # Test fenced code block
    text = "```python\ndef test():\n    pass\n```"
    html = md.convert(text)
    assert (
        '<pre><code class="language-python">def test():\n    pass</code></pre>' in html
    )

    # Test indented code block
    text = "    def test():\n        pass"
    html = md.convert(text)
    assert "<pre><code>def test():\n    pass</code></pre>" in html


def test_list_processor() -> None:
    """Test the list block processor."""
    md = Markdown()
    processor = ListBlockProcessor(md.parser)

    # Test unordered list
    text = "- Item 1\n- Item 2\n- Item 3"
    html = md.convert(text)
    assert "<ul>" in html
    assert "<li>Item 1</li>" in html

    # Test ordered list
    text = "1. Item 1\n2. Item 2\n3. Item 3"
    html = md.convert(text)
    assert "<ol>" in html
    assert "<li>Item 1</li>" in html

    # Test task list
    text = "- [ ] Task 1\n- [x] Task 2"
    html = md.convert(text)
    assert '<input type="checkbox"' in html
    assert '<input type="checkbox" checked="checked"' in html


def test_extension_registration() -> None:
    """Test that the extension registers all processors."""
    md = Markdown(extensions=[TwardownExtension()])

    # Test that all processors are registered
    assert "twardown_bold" in md.inlinePatterns
    assert "twardown_italic" in md.inlinePatterns
    assert "twardown_link" in md.inlinePatterns
    assert "twardown_code" in md.inlinePatterns
    assert "twardown_image" in md.inlinePatterns
    assert "twardown_code_block" in md.parser.blockprocessors
    assert "twardown_list" in md.parser.blockprocessors
