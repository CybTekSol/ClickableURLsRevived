import re, webbrowser, sublime, sublime_plugin
URL_REGEX = re.compile(r"""(?xi)\b((?:https?|ftp)://[^\s<>'"()]+|www\.[^\s<>'"()]+)""")
class ClickableUrlsHighlighter(sublime_plugin.ViewEventListener):
    URL_KEY = "clickable_urls_regions"
    @classmethod
    def is_applicable(cls, settings): return not settings.get("is_widget", False)
    def __init__(self, view):
        super().__init__(view)
        s = sublime.load_settings("ClickableURLsRevived.sublime-settings")
        self.max_regions = s.get("max_url_highlights", 1000)
        self.scope = s.get("highlight_scope", "markup.underline.link")
    def on_modified_async(self): self._rescan()
    def on_activated_async(self): self._rescan()
    def on_load_async(self): self._rescan()
    def _rescan(self):
        if self.view.size() > 2_000_000: self.view.erase_regions(self.URL_KEY); return
        text = self.view.substr(sublime.Region(0, self.view.size())); regs=[]
        for m in URL_REGEX.finditer(text):
            if len(regs)>=self.max_regions: break
            regs.append(sublime.Region(m.start(1), m.end(1)))
        self.view.add_regions(self.URL_KEY, regs, self.scope,
            flags=(sublime.DRAW_NO_OUTLINE|sublime.DRAW_EMPTY|sublime.DRAW_NO_FILL|sublime.DRAW_SOLID_UNDERLINE))
class OpenUrlUnderCursorCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for sel in self.view.sel():
            r = sel if not sel.empty() else self._url_region(sel.begin())
            if r and not r.empty():
                u = self.view.substr(r); 
                if u.startswith("www."): u = "http://" + u
                webbrowser.open_new_tab(u)
    def _url_region(self, pt):
        line = self.view.line(pt); text = self.view.substr(line); off = line.begin()
        for m in URL_REGEX.finditer(text):
            a,b = off+m.start(1), off+m.end(1)
            if a <= pt <= b: return sublime.Region(a,b)
        return sublime.Region(pt,pt)
