# ClickableURLsRevived

Sublime Text 4 plugin that underlines URLs and opens the one under your cursor.

## Install (manual)
- **Source**: Preferences → Browse Packages… → create `ClickableURLsRevived` and copy files.
- **Package**: place `ClickableURLsRevived.sublime-package` in `Installed Packages/` and restart.

## Usage
- URLs are underlined automatically.
- Open URL under cursor: Ctrl+Alt+Enter (Linux/Windows) or ⌘⌥Enter (macOS).

## Ensure underlines are visible
If your color scheme doesn’t underline `markup.underline.link`, copy
`ClickableURLsRevived-color-scheme-example.sublime-color-scheme` into your
`Packages/User/` folder and select it (or merge the rule into your scheme).

## Releases via GitHub Actions
When you push a git tag like `v1.0.0`, the provided workflow will build
`ClickableURLsRevived.sublime-package` and attach it to the GitHub Release.
