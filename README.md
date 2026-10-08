# ClickableURLsRevived

Sublime Text 4+ plugin that underlines URLs that are present in a text file and allow you to open the one under your cursor
in your system's default web browser.

Developed and maintained by **CybTekSol [ https://github.com/CybTekSol ]**.

**DISCLAIMER:**  
This plugin is provided free of charge, **AS-IS**, no warranties or guarantees (expressed or implied)... use is at your own risk and is licensed as stated in the LICENSE file located in this repository.

## Install (manual)
- **Source**: Preferences → Browse Packages… → create `ClickableURLsRevived` and copy files.
- **Package**: place `ClickableURLsRevived.sublime-package` in `Installed Packages/` and restart.

## Usage
- URLs are underlined automatically.
- Open URL under cursor: Ctrl+Alt+Enter (Linux/Windows) or ⌘⌥Enter (macOS) or a Mouse Right-Click action.

## Ensure underlines are visible
If your color scheme doesn’t underline `markup.underline.link`, copy
`ClickableURLsRevived-color-scheme-example.sublime-color-scheme` into your
`Packages/User/` folder and select it (or merge the rule into your scheme).

## Releases via GitHub Actions
When you push a git tag like `v1.1.0`, the provided workflow will build
`ClickableURLsRevived.sublime-package` and attach it to the GitHub Release.
