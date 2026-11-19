"""data.json + template.html -> 참돔_선상낚시_백과.html"""
import json, pathlib
here = pathlib.Path(__file__).parent
data = [d for d in json.loads((here / "data.json").read_text(encoding="utf-8")) if d]
tpl = (here / "template.html").read_text(encoding="utf-8")
blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
(here / "참돔_선상낚시_백과.html").write_text(tpl.replace("__DATA__", blob), encoding="utf-8")
print("sections:", len(data))
