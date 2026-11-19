"""4컷 속 작은 참돔: 비늘 해칭 없이 윤곽선만 (작게 줄이면 뭉개지므로)"""
import re, pathlib
here = pathlib.Path(__file__).parent
src = (here / "seabream.py").read_text(encoding="utf-8")
ns = {"__file__": str(here / "seabream.py")}
exec(src.split("def drop")[0], ns)
fish, A = ns["fish"], ns["A"]
def small(cx, cy, s, left):
    keep = [p for p in re.findall(r'<path[^>]*/>', fish(cx, cy, s, left))
            if float(re.search(r'stroke-width="([\d.]+)"', p).group(1)) >= 0.9]
    return "".join(p.replace(A, 'class="d f"') for p in keep)
t = (here / "template.html").read_text(encoding="utf-8")
head, fin = t.split('id="finale"', 1)
fin = re.sub(r'<path class="d f"[^>]*/>', "", fin)  # 이전 실행에서 넣은 작은 물고기 제거(재실행 안전)
def strip(fin, x0, x1, y0, y1):
    n = 0
    for p in re.findall(r'\s*<path class="d"[^>]*/>', fin):
        nums = list(map(float, re.findall(r'(-?\d+\.\d)', re.search(r' d="([^"]*)"', p).group(1))))
        if nums and all(x0 <= x <= x1 for x in nums[0::2]) and all(y0 <= y <= y1 for y in nums[1::2]):
            fin = fin.replace(p, "", 1); n += 1
    return fin, n
fin, n3 = strip(fin, 50, 160, 290, 345)
fin, n4 = strip(fin, 340, 400, 295, 345)
anchor = '<path class="d" stroke-width="1" d="M214 220'
fin = fin.replace(anchor, small(116, 314, .5, True) + small(370, 318, .38, True) + "\n    " + anchor, 1)
t = head + 'id="finale"' + fin
t = t.replace("#finale svg path{stroke-width:1.9px}", "#finale svg path:not(.f){stroke-width:1.9px}")
(here / "template.html").write_text(t, encoding="utf-8")
print("removed", n3, n4)
