import base64
import os
import sys

try:
    def get_b64(path):
        with open(path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

    bg = get_b64(r"C:\Users\user\.gemini\antigravity\brain\42c0e064-cbdc-42e4-b21d-d8b9f72ff1ad\bg_dungeon_1775112995494.png")
    slime = get_b64(r"C:\Users\user\.gemini\antigravity\brain\42c0e064-cbdc-42e4-b21d-d8b9f72ff1ad\char_slime_1775113011408.png")
    miner = get_b64(r"C:\Users\user\.gemini\antigravity\brain\42c0e064-cbdc-42e4-b21d-d8b9f72ff1ad\char_miner_1775113027165.png")
    gold = get_b64(r"C:\Users\user\.gemini\antigravity\brain\42c0e064-cbdc-42e4-b21d-d8b9f72ff1ad\ore_gold_1775113045160.png")
    crystal = get_b64(r"C:\Users\user\.gemini\antigravity\brain\42c0e064-cbdc-42e4-b21d-d8b9f72ff1ad\ore_crystal_1775113060589.png")
    emerald = get_b64(r"C:\Users\user\.gemini\antigravity\brain\42c0e064-cbdc-42e4-b21d-d8b9f72ff1ad\ore_emerald_1775114804164.png")

    with open(r"C:\Users\user\.gemini\antigravity\scratch\mining-game\template.html", "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace("%%BG_DUNGEON%%", bg)
    html = html.replace("%%CHAR_SLIME%%", slime)
    html = html.replace("%%CHAR_MINER%%", miner)
    html = html.replace("%%ORE_GOLD%%", gold)
    html = html.replace("%%ORE_CRYSTAL%%", crystal)
    html = html.replace("%%ORE_EMERALD%%", emerald)

    target_dir = r"C:\Users\user\.gemini\antigravity\scratch\mining-game"
    os.makedirs(target_dir, exist_ok=True)

    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    print("SUCCESS: Python script generated index.html")
except Exception as e:
    import traceback
    traceback.print_exc()
    sys.exit(1)
