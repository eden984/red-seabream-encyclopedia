"""섬세한 참돔 펜화 생성기 + 그림 교체 (담화린 2차 지적: 참돔이 붕어 같음)"""
import json, pathlib, re
here = pathlib.Path(__file__).parent
A = 'class="d" fill="none" stroke="#111" stroke-linecap="round" stroke-linejoin="round"'

def fish(cx, cy, s, left=False, w=1.0):
    """참돔 한 마리를 절대좌표 path 문자열들로 반환. 원본은 오른쪽을 보고, 길이 약 106."""
    fx = -1 if left else 1
    P = lambda x, y: f"{cx + fx * x * s:.1f} {cy + y * s:.1f}"
    out = []
    def path(d, sw):
        out.append(f'<path {A} stroke-width="{sw * w:.2f}" d="{d}"/>')
    # 몸통: 이마가 가파르게 솟고 등이 높은 참돔 체형
    path(f"M{P(48,2)} C{P(45,-9)} {P(32,-22)} {P(10,-24)} C{P(-10,-25)} {P(-27,-17)} {P(-34,-8)} L{P(-40,-4)}", 1.9)
    path(f"M{P(48,2)} C{P(44,10)} {P(32,16)} {P(14,17)} C{P(-6,18)} {P(-24,12)} {P(-34,5)} L{P(-40,2)}", 1.9)
    # 깊게 갈라진 꼬리
    path(f"M{P(-40,-4)} L{P(-58,-19)} Q{P(-54,-12)} {P(-49,-1)} Q{P(-54,9)} {P(-58,15)} L{P(-40,2)}", 1.7)
    path(f"M{P(-43,-5)} L{P(-52,-12)} M{P(-43,1)} L{P(-52,8)}", .7)
    # 가시 있는 등지느러미: 가시 + 막
    tips = []
    for i, x in enumerate(range(20, -27, -5)):
        yb = -24 + 0.011 * x * x if x < 0 else -24 + 0.004 * x * x
        h = 10 - i * 0.55
        path(f"M{P(x, yb)} L{P(x - 2, yb - h)}", .9)
        tips.append((x - 2, yb - h))
    path("M" + " L".join(P(x, y) for x, y in tips), .7)
    # 눈, 아가미, 입
    ex, ey, r = 36, -7, 3.4
    k = .55 * r
    path(f"M{P(ex+r,ey)} C{P(ex+r,ey+k)} {P(ex+k,ey+r)} {P(ex,ey+r)} C{P(ex-k,ey+r)} {P(ex-r,ey+k)} {P(ex-r,ey)} C{P(ex-r,ey-k)} {P(ex-k,ey-r)} {P(ex,ey-r)} C{P(ex+k,ey-r)} {P(ex+r,ey-k)} {P(ex+r,ey)}", 1.2)
    path(f"M{P(ex+.6,ey-1)} L{P(ex-.6,ey+1)}", 1.6)
    path(f"M{P(25,-17)} Q{P(18,-2)} {P(25,13)}", 1.1)
    path(f"M{P(30,-12)} Q{P(26,-2)} {P(30,8)}", .7)
    path(f"M{P(48,2)} L{P(42,3)}", 1)
    # 가슴·배·뒷지느러미
    path(f"M{P(21,1)} Q{P(9,4)} {P(3,12)} Q{P(13,8)} {P(21,4)}", .9)
    path(f"M{P(17,15)} L{P(11,23)} L{P(9,16)}", .9)
    path(f"M{P(-12,15)} L{P(-25,21)} L{P(-29,10)}", .9)
    # 옆줄 + 비늘 해칭
    path(f"M{P(25,-17)} Q{P(0,-21)} {P(-37,-4)}", .6)
    rows = [(-14, 14, -20), (-7, 18, -28), (0, 18, -30), (7, 14, -26), (12, 8, -18)]
    for y, x0, x1 in rows:
        for x in range(x0, x1, -6):
            path(f"M{P(x, y)} Q{P(x-3, y-3)} {P(x-6, y)}", .55)
    return "".join(out)

def drop(svg, starts):
    for st in starts:
        svg, n = re.subn(r'<path[^>]*d="' + re.escape(st) + r'[^"]*"[^>]*/>', "", svg, count=1)
        assert n == 1, st
    return svg

d = json.loads((here / "data.json").read_text(encoding="utf-8"))
# fig.1: 기존 물고기(13~18번 path) 제거, 바닥 근처에 오른쪽을 보는 참돔
s0 = drop(d[0]["svg"], ["M190 205 Q215", "M190 205 L176", "M205 191 Q215", "M234 199 a1.5", "M228 194 Q231", "M205 200 l1 1"])
d[0]["svg"] = s0.replace("</svg>", fish(206, 205, .78) + "</svg>")
# fig.5: 기존 물고기 제거, 왼쪽을 보는 참돔(입이 줄 끝에)
s4 = drop(d[4]["svg"], ["M310 200 Q330", "M355 195 L372", "M322 193 Q330", "M325 205 Q335"])
angler = (f'<path {A} stroke-width="1.3" d="M168 110 L182 110 L181 129 L169 129 Z M171 110 L175 118 L179 110 M169 120 L181 120"/>'
          f'<path {A} stroke-width="1.3" d="M196 104 a4 4 0 1 0 .1 0 M196 108 L192 114"/>'
          f'<path {A} stroke-width="1.2" d="M203 99 a2.5 2.5 0 1 0 .1 0 M197 110 a2.5 2.5 0 1 0 .1 0"/>')
d[4]["svg"] = s4.replace("</svg>", fish(358, 202, .6, left=True) + angler + "</svg>")
(here / "data.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

# 표지 + 4컷(template.html)
t = (here / "template.html").read_text(encoding="utf-8")
hero_old = re.search(r'\s*<path class="d" stroke-width="1.8" d="M330 196 Q352[^>]*/>\s*<path class="d" stroke-width="1.4" d="M330 196 L314[^>]*/>', t)
if hero_old:
    hero_fish = fish(346, 196, .55).replace(A, 'class="d"')
    t = t.replace(hero_old.group(0), "\n    " + hero_fish)
p3 = re.search(r'\s*<path class="d" stroke-width="1.8" d="M90 314 q16[^>]*/>\s*<path class="d" stroke-width="1" d="M100 311 a2[^>]*/>', t)
if p3:
    t = t.replace(p3.group(0), "\n    " + fish(116, 314, .5, left=True).replace(A, 'class="d"'))
p4 = re.search(r'\s*<path class="d" stroke-width="1.8" d="M332 318 q14[^>]*/>\s*<path class="d" stroke-width="1" d="M372 318 a2[^>]*/>', t)
if p4:
    t = t.replace(p4.group(0), "\n    " + fish(370, 318, .38, left=True).replace(A, 'class="d"'))
(here / "template.html").write_text(t, encoding="utf-8")
print("hero", bool(hero_old), "p3", bool(p3), "p4", bool(p4))
