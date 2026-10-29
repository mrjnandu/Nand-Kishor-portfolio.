"""
build.py : data.py + template se public/index.html banata hai.
  python build.py            -> sirf build
  python build.py --serve    -> build + local server (http://localhost:8000)
"""
import json, shutil, sys
from pathlib import Path
from data import PROFILE

ROOT = Path(__file__).parent
PUBLIC = ROOT / "public"


def build():
    template = (ROOT / "templates" / "index.template.html").read_text(encoding="utf-8")
    html = template.replace("__DATA__", json.dumps(PROFILE, ensure_ascii=False))
    PUBLIC.mkdir(exist_ok=True)
    (PUBLIC / "index.html").write_text(html, encoding="utf-8")
    shutil.copytree(ROOT / "assets", PUBLIC / "assets", dirs_exist_ok=True)
    print("Done! public/index.html ban gayi.")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        import functools, http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(PUBLIC))
        print("Open karo: http://localhost:8000  (band karne ke liye Ctrl+C)")
        http.server.ThreadingHTTPServer(("", 8000), handler).serve_forever()
