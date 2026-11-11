"""
Re-applies the Sun Li-jen hook to Road to 56's Nationalist China tree.
Run this again whenever R56 updates china_nationalist.txt.

Usage (from the submod folder):
    python tools/patch_r56_tree.py "C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/820260968/common/national_focus/china_nationalist.txt"

It writes common/national_focus/china_nationalist.txt into this submod with two edits:
  1. pastes the focuses from tools/SLJ_focuses.txt into the end of the focus_tree
  2. makes KMT_gut_the_deep_state_new, KMT_china_at_the_mercy_of_the_cc_clique, and KMT_expand_dais_apparatus mutually exclusive with the Sun branch
"""
import os
import re
import sys

ROOT = "SLJ_the_officers_memorandum"
HOOK_FOCUSES = ["KMT_gut_the_deep_state_new", "KMT_china_at_the_mercy_of_the_cc_clique", "KMT_expand_dais_apparatus"]


def main(src):
    raw = open(src, "rb").read()
    bom = raw.startswith(b"\xef\xbb\xbf")
    text = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in text else "\n"

    if ROOT in text:
        sys.exit("Already patched - point this at R56's original file.")

    # 1. paste the Sun focuses before the focus_tree's final closing brace
    here_tools = os.path.dirname(os.path.abspath(__file__))
    block = open(os.path.join(here_tools, "SLJ_focuses.txt"), encoding="utf-8").read()
    block = block.replace("\r\n", "\n").replace("\n", nl)
    end = text.rstrip().rfind("}")
    if end == -1:
        sys.exit("Couldn't find the end of the focus_tree.")
    text = text[:end] + nl + "\t### ---- Sun Li-jen Path (R56_sun_lijen submod) ----" + nl + "\t" + block + nl + text[end:]

    # 2. mutual exclusions on Chiang's fascist-turn focus, CC Clique, Dai Expansion

    for focus in HOOK_FOCUSES:
        m = re.search(r"(?m)^([ \t]*)id[ \t]*=[ \t]*" + focus + r"\b", text)
        if not m:
            sys.exit("Couldn't find " + focus + " - R56 may have renamed it.")
        indent = m.group(1)
        line = nl + indent + "mutually_exclusive = { focus = " + ROOT + " }"
        text = text[:m.end()] + line + text[m.end():]

    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(here, "common", "national_focus", "china_nationalist.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "wb") as f:
        f.write((b"\xef\xbb\xbf" if bom else b"") + text.encode("utf-8"))
    print("Wrote", out)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
