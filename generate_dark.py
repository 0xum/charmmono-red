"""Apply red accents to the unmodified Charmmono Dark 0.3.1 source."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
theme = json.loads((ROOT / "upstream/charmmono-dark-0.3.1.json").read_text())
theme["name"] = "Charmmono Red Dark"

# Target UI roles explicitly: the same source colors also occur in diagnostics
# and terminal ANSI colors, where their original meaning must be preserved.
theme["colors"].update({
    "focusBorder": "#e05a64ff",
    "textLink.foreground": "#f2a09aff",
    "textLink.activeForeground": "#ffb4abff",
    "button.background": "#f28b82ff",
    "button.hoverBackground": "#f2a09aff",
    "inputOption.activeBorder": "#e05a64ff",
    "badge.foreground": "#ffd4d1ff",
    "badge.background": "#8f2834ff",
    "progressBar.background": "#e05a64ff",
    "activityBarBadge.background": "#f28b82ff",
    "activityBar.activeBorder": "#f28b82ff",
    "list.inactiveFocusBackground": "#6b202999",
    "list.focusBackground": "#6b2029ff",
    "tab.activeBorderTop": "#f28b82ff",
    "editorLink.activeForeground": "#f28b82ff",
    "editorCursor.foreground": "#ffd4d1ff",
    "sash.hoverBorder": "#f28b82ff",
    "peekView.border": "#f28b82ff",
    "editor.linkedEditingBackground": "#8f283499",
    "editor.inactiveSelectionBackground": "#a63c484d",
    "editor.selectionBackground": "#a63c4880",
    "panelTitle.activeBorder": "#f28b82ff",
    "terminal.tab.activeBorder": "#f28b82ff",
    "terminalCursor.foreground": "#ffb4abff",
    "editorBracketHighlight.foreground3": "#f28b82ff",
    "editorBracketHighlight.foreground6": "#f28b82ff",
})

# Match the syntax roles adjusted in Red Light. Keep scopes, styles, semantic
# tokens, strings, constants, Git diffs and error colors from the original.
syntax_colors = {"#bd9cfeff": "#f28b82ff", "#fd8da3ff": "#f6a0a6ff"}
for token in theme["tokenColors"]:
    settings = token.get("settings", {})
    for key in ("foreground", "background"):
        if settings.get(key) in syntax_colors:
            settings[key] = syntax_colors[settings[key]]

destination = ROOT / "themes/charmmono-red-dark-color-theme.json"
destination.write_text(json.dumps(theme, indent=2, ensure_ascii=False) + "\n")
print(destination)
