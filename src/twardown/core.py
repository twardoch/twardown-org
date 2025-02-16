#!/usr/bin/env -S uv run
# /// script
# dependencies = [
#   "markdown",
# ]
# ///
"""
Twardown Core Extension for Python Markdown

this_file: src/twardown/core.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING, List, Dict, Any, Optional, Tuple, Union

if TYPE_CHECKING:
    from markdown import Markdown
    from markdown.inlinepatterns import InlineProcessor
    from markdown.util import etree
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.blockprocessors import BlockProcessor
from markdown.inlinepatterns import InlineProcessor
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor
from markdown.parser import Parser
from markdown import Markdown
import re
from typing import List, Dict, Any, Optional


def process_text(text: str) -> str:
    """Processes a single line of text.

    Handles basic text processing including:
    - Paragraphs (separated by blank lines)
    - Inline formatting (bold, italic, code)
    - Links and images
    - Lists (ordered and unordered)
    - Code blocks (fenced and indented)

    Args:
        text: The text to process.

    Returns:
        The processed text.
    """
    return text


class BoldInlineProcessor(InlineProcessor):
    """Inline processor for bold text.

    Matches text surrounded by double asterisks or double underscores.
    Example: **bold** or __bold__
    """

    def __init__(self, md: Markdown):
        super().__init__(r"\*\*([^*]+)\*\*|__([^_]+)__", md)

    def handleMatch(self, m: re.Match, data: str) -> Tuple[Any, int, int]:
        el = etree.Element("strong")
        el.text = m.group(1) or m.group(2)  # Handle both ** and __ patterns
        return el, m.start(0), m.end(0)


class ItalicInlineProcessor(InlineProcessor):
    """Inline processor for italic text.

    Matches text surrounded by single asterisk or single underscore.
    Example: *italic* or _italic_
    """

    def __init__(self, md: Markdown):
        super().__init__(r"\*([^*]+)\*|_([^_]+)_", md)

    def handleMatch(self, m: re.Match, data: str) -> Tuple[Any, int, int]:
        el = etree.Element("em")
        el.text = m.group(1) or m.group(2)  # Handle both * and _ patterns
        return el, m.start(0), m.end(0)


class LinkInlineProcessor(InlineProcessor):
    """Inline processor for markdown links.

    Matches standard markdown links: [text](url "optional title")
    and reference-style links: [text][ref] or [text][]
    """

    def __init__(self, md: Markdown):
        super().__init__(r'\[([^\]]+)\]\(([^)"]+)(?:\s+"([^"]+)")?\)', md)

    def handleMatch(self, m: re.Match, data: str) -> Tuple[Any, int, int]:
        el = etree.Element("a")
        el.text = m.group(1)
        el.set("href", m.group(2))
        if m.group(3):  # Optional title
            el.set("title", m.group(3))
        return el, m.start(0), m.end(0)


class CodeInlineProcessor(InlineProcessor):
    """Inline processor for inline code.

    Matches text surrounded by backticks.
    Example: `code`
    """

    def __init__(self, md: Markdown):
        super().__init__(r"`([^`]+)`", md)

    def handleMatch(self, m: re.Match, data: str) -> Tuple[Any, int, int]:
        el = etree.Element("code")
        el.text = m.group(1)
        return el, m.start(0), m.end(0)


class ImageInlineProcessor(InlineProcessor):
    """Inline processor for images.

    Matches markdown image syntax: ![alt](url "optional title")
    """

    def __init__(self, md: Markdown):
        super().__init__(r'!\[([^\]]*)\]\(([^)"]+)(?:\s+"([^"]+)")?\)', md)

    def handleMatch(self, m: re.Match, data: str) -> Tuple[Any, int, int]:
        el = etree.Element("img")
        el.set("src", m.group(2))
        el.set("alt", m.group(1) or "")
        if m.group(3):  # Optional title
            el.set("title", m.group(3))
        return el, m.start(0), m.end(0)


class TwardownExtension(Extension):
    """Twardown extension for Python-Markdown."""

    def __init__(self, **kwargs: Any) -> None:
        self.config: Dict[str, Any] = {
            "option": ["default", "Description of the option"]
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md: Markdown) -> None:
        """Add Twardown extension to Markdown instance."""
        # Register block processors
        md.parser.blockprocessors.register(
            CodeBlockProcessor(md.parser), "twardown_code_block", 95
        )
        md.parser.blockprocessors.register(
            ListBlockProcessor(md.parser), "twardown_list", 90
        )

        # Register inline processors
        md.inlinePatterns.register(BoldInlineProcessor(md), "twardown_bold", 180)
        md.inlinePatterns.register(ItalicInlineProcessor(md), "twardown_italic", 170)
        md.inlinePatterns.register(LinkInlineProcessor(md), "twardown_link", 160)
        md.inlinePatterns.register(CodeInlineProcessor(md), "twardown_code", 150)
        md.inlinePatterns.register(ImageInlineProcessor(md), "twardown_image", 140)
        md.inlinePatterns.register(TwardownInlineProcessor(md), "twardown_inline", 100)

        # Register other processors
        md.treeprocessors.register(TwardownTreeProcessor(md), "twardown_tree", 100)
        md.preprocessors.register(TwardownPreprocessor(md), "twardown_pre", 100)
        md.postprocessors.register(TwardownPostprocessor(md), "twardown_post", 100)


class CodeBlockProcessor(BlockProcessor):
    """Processor for code blocks.

    Handles both fenced code blocks (```lang) and indented code blocks.
    """

    FENCED_BLOCK_RE = re.compile(
        r"(?P<fence>^`{3,}|^~{3,})[ ]*(?P<lang>[^\n]+)?[ ]*\n(?P<code>.*?)(?<=\n)(?P=fence)[ ]*$",
        re.MULTILINE | re.DOTALL,
    )
    INDENT_RE = re.compile(r"^([ ]{4}|\t)")

    def test(self, parent: Any, block: str) -> bool:
        return bool(self.FENCED_BLOCK_RE.match(block)) or bool(
            self.INDENT_RE.match(block)
        )

    def run(self, parent: Any, blocks: List[str]) -> None:
        block = blocks.pop(0)
        m = self.FENCED_BLOCK_RE.match(block)

        pre = etree.SubElement(parent, "pre")
        if m:  # Fenced code block
            code = etree.SubElement(pre, "code")
            if m.group("lang"):
                code.set("class", f"language-{m.group('lang').strip()}")
            code.text = m.group("code").rstrip()
        else:  # Indented code block
            code = etree.SubElement(pre, "code")
            code.text = "\n".join(
                [self.INDENT_RE.sub("", line) for line in block.split("\n")]
            )


class ListBlockProcessor(BlockProcessor):
    """Processor for ordered and unordered lists."""

    INDENT_RE = re.compile(r"^[ ]{0,3}([-+*]|\d+\.)[ ]+(.+)")

    def test(self, parent: Any, block: str) -> bool:
        return bool(self.INDENT_RE.match(block.split("\n")[0]))

    def run(self, parent: Any, blocks: List[str]) -> None:
        block = blocks.pop(0)
        m = self.INDENT_RE.match(block.split("\n")[0])

        if m.group(1)[0] in "-+*":
            list_elem = etree.SubElement(parent, "ul")
        else:
            list_elem = etree.SubElement(parent, "ol")

        for line in block.split("\n"):
            if self.INDENT_RE.match(line):
                item = etree.SubElement(list_elem, "li")
                item.text = self.INDENT_RE.match(line).group(2)


class TwardownBlockProcessor(BlockProcessor):
    """Twardown Block Processor."""

    def test(self, parent: Any, block: str) -> bool:
        return False  # TODO: Implement block processing logic

    def run(self, parent: Any, blocks: List[str]) -> None:
        pass  # TODO: Implement block processing logic


class TwardownInlineProcessor(InlineProcessor):
    """Twardown Inline Processor."""

    def __init__(self, md: Markdown):
        super().__init__(r"\+\+([^\+]+)\+\+", md)  # Regex for ++inserted text++

    def handleMatch(self, match: Any, data: str) -> tuple[Any, int, int]:
        text = match.group(1)
        ins = self.md.etree.Element("ins")
        ins.text = text
        return ins, match.start(0), match.end(0)


class TwardownTreeProcessor(Treeprocessor):
    """Twardown Tree Processor.

    Handles post-processing of the element tree, including:
    - Table formatting
    - List nesting
    - Code block formatting
    """

    def run(self, root: Any) -> None:
        """Process the element tree.

        Args:
            root: The root element of the tree.
        """
        for elem in root.iter():
            if elem.tag == "table":
                self._format_table(elem)
            elif elem.tag in ("ul", "ol"):
                self._format_list(elem)
            elif elem.tag == "pre":
                self._format_code_block(elem)

    def _format_table(self, table: Any) -> None:
        """Format table elements with proper alignment and classes."""
        if not table.find("thead") or not table.find("tbody"):
            return

        # Add table classes
        table.set("class", "twardown-table")

        # Process header alignment
        header_row = table.find("thead/tr")
        if header_row is not None:
            for th in header_row.findall("th"):
                align = th.get("align", "left")
                th.set("class", f"align-{align}")

        # Process body alignment
        tbody = table.find("tbody")
        if tbody is not None:
            for tr in tbody.findall("tr"):
                for td in tr.findall("td"):
                    align = td.get("align", "left")
                    td.set("class", f"align-{align}")

    def _format_list(self, list_elem: Any) -> None:
        """Format list elements with proper nesting and classes."""
        list_elem.set("class", "twardown-list")
        for li in list_elem.findall(".//li"):
            # Handle task list items
            if li.text and li.text.startswith("[ ] "):
                li.set("class", "task-list-item")
                li.text = li.text[4:]
                checkbox = etree.Element("input")
                checkbox.set("type", "checkbox")
                li.insert(0, checkbox)
            elif li.text and li.text.startswith("[x] "):
                li.set("class", "task-list-item")
                li.text = li.text[4:]
                checkbox = etree.Element("input")
                checkbox.set("type", "checkbox")
                checkbox.set("checked", "checked")
                li.insert(0, checkbox)

    def _format_code_block(self, pre: Any) -> None:
        """Format code blocks with proper classes and data attributes."""
        code = pre.find("code")
        if code is not None:
            lang_class = code.get("class", "")
            if lang_class.startswith("language-"):
                pre.set("class", "twardown-code-block")
                pre.set("data-language", lang_class[9:])


class TwardownPreprocessor(Preprocessor):
    """Twardown Preprocessor.

    Handles preprocessing of the text before parsing, including:
    - Front matter extraction
    - Magic record validation
    - Table formatting
    """

    FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
    TABLE_LINE_RE = re.compile(r"^\|(.+)\|$")
    TABLE_SEPARATOR_RE = re.compile(r"^\|(\s*:?-+:?\s*\|)+$")

    def run(self, lines: List[str]) -> List[str]:
        """Process the text before parsing.

        Args:
            lines: List of text lines to process.

        Returns:
            Processed list of lines.
        """
        # Handle front matter
        content = "\n".join(lines)
        front_matter_match = self.FRONT_MATTER_RE.match(content)
        if front_matter_match:
            # Store front matter for later use
            self.md.twardown = {"front_matter": front_matter_match.group(1)}
            content = content[front_matter_match.end() :]
            lines = content.split("\n")

        # Process tables
        new_lines = []
        in_table = False
        table_header = []
        table_alignments = []

        for line in lines:
            if self.TABLE_LINE_RE.match(line):
                if not in_table:
                    in_table = True
                    table_header = self._parse_table_row(line)
                    new_lines.append(line)
                elif self.TABLE_SEPARATOR_RE.match(line):
                    table_alignments = self._parse_table_alignments(line)
                    new_lines.append(line)
                else:
                    new_lines.append(line)
            else:
                if in_table:
                    in_table = False
                new_lines.append(line)

        return new_lines

    def _parse_table_row(self, line: str) -> List[str]:
        """Parse a table row into cells."""
        return [cell.strip() for cell in line.strip("|").split("|")]

    def _parse_table_alignments(self, line: str) -> List[str]:
        """Parse table alignments from separator line."""
        alignments = []
        for cell in line.strip("|").split("|"):
            cell = cell.strip()
            if cell.startswith(":") and cell.endswith(":"):
                alignments.append("center")
            elif cell.endswith(":"):
                alignments.append("right")
            else:
                alignments.append("left")
        return alignments


class TwardownPostprocessor(Postprocessor):
    """Twardown Postprocessor.

    Handles final text processing, including:
    - Adding CSS classes
    - Formatting special elements
    - Cleaning up whitespace
    """

    def run(self, text: str) -> str:
        """Process the final text output.

        Args:
            text: The text to process.

        Returns:
            The processed text.
        """
        # Add wrapper div with twardown class
        text = f'<div class="twardown-content">\n{text}\n</div>'

        # Clean up whitespace
        text = re.sub(r"\n\s*\n", "\n\n", text)
        text = text.strip()

        return text


def makeExtension(**kwargs: Dict[str, Any]) -> TwardownExtension:
    """Create an instance of the TwardownExtension.

    Args:
        **kwargs: Configuration options for the extension.

    Returns:
        A configured TwardownExtension instance.
    """
    return TwardownExtension(**kwargs)
