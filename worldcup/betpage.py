"""Private, client-side-encrypted bet-analysis page.

The tracked-bet analysis is rendered to an HTML fragment, then encrypted with
AES-256-GCM under a key derived from a passphrase (PBKDF2-HMAC-SHA256). Only
the ciphertext, salt and IV ship in the deployed file — the page is unreadable
without the passphrase, which is entered in the browser and never leaves it.
This gives genuine privacy even though GitHub Pages itself is public.

    BET_PAGE_PASSPHRASE='your secret' python -m worldcup.betpage --sims 50000
"""

from __future__ import annotations

import argparse
import base64
import os
from datetime import datetime, timezone
from html import escape
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

from .bets import compute

SITE_DIR = Path(__file__).parent / "outputs" / "site"
PAGE_NAME = "picks.html"
PBKDF2_ITERS = 200_000


def _ev_badge(ev: float) -> str:
    if ev >= 0.05:
        return f'<span class="ev good">+{ev*100:.0f}% EV</span>'
    if ev <= -0.05:
        return f'<span class="ev bad">{ev*100:.0f}% EV</span>'
    return f'<span class="ev flat">~fair ({ev*100:+.0f}%)</span>'


def render_fragment(data: dict) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    p = [f'<p class="meta">Updated {ts} UTC · {data["played"]}/72 group games in · '
         f'{data["n_sims"]:,} simulations</p>']

    for b in data["bets"]:
        odds = f"1 in {1/b['prob']:,.0f}" if b["prob"] > 0 else "—"
        p.append('<div class="card">')
        p.append(f'<div class="cardhead"><h3>{escape(b["name"])}</h3>{_ev_badge(b["ev"])}</div>')
        p.append(f'<p class="stake">£{b["stake"]:.0f} → £{b["returns"]:,.2f} '
                 f'<span class="mult">({b["dec"]:.0f}×)</span></p>')
        p.append('<div class="nums">'
                 f'<div><span>Model</span><b>{100*b["prob"]:.2f}%</b><i>{odds}</i></div>'
                 f'<div><span>Bookie implied</span><b>{100*b["implied"]:.2f}%</b></div>'
                 f'<div><span>Expected return</span><b>£{b["exp_return"]:,.2f}</b>'
                 f'<i>on £{b["stake"]:.0f}</i></div></div>')
        p.append('<table class="legs"><tbody>')
        for lg in b["legs"]:
            cls = "weak" if lg["weakest"] else ""
            tag = ' <span class="wk">weakest link</span>' if lg["weakest"] else ""
            st = f' {lg["status"]}' if lg["status"] else ""
            p.append(f'<tr class="{cls}"><td>{escape(lg["team"])}{st}</td>'
                     f'<td>reach {escape(lg["stage"])}</td>'
                     f'<td class="pct">{100*lg["prob"]:.0f}%{tag}</td></tr>')
        p.append('</tbody></table></div>')

    crit = [c for c in data["criticality"] if c["max_swing"] >= 0.002]
    if crit:
        p.append('<h2>Games that move a bet</h2>')
        p.append('<p class="meta">Ranked by how much the result swings a bet '
                 '(all teams are already through the group, so these mostly affect '
                 'the knockout draw).</p>')
        for c in crit[:8]:
            dot = "🔴" if c["max_swing"] >= 0.02 else ("🟠" if c["max_swing"] >= 0.005 else "⚪")
            who = " & ".join(escape(t) for t in c["involved"])
            p.append('<div class="game">')
            p.append(f'<div class="gh">{dot} <b>{escape(c["date"])}</b> · '
                     f'{escape(c["home"])} v {escape(c["away"])} '
                     f'<span class="odds">{100*c["p_home"]:.0f}/{100*c["p_draw"]:.0f}/'
                     f'{100*c["p_away"]:.0f}</span> — {who}</div>')
            for r in c["rows"]:
                if abs(r["swing"]) < 0.002:
                    continue
                team = escape(c["involved"][0])
                p.append(f'<div class="swing"><code>{escape(r["bet"])}</code> '
                         f'{100*r["base"]:.2f}% → '
                         f'<b>{100*r["if_win"]:.2f}%</b> if {team} win, '
                         f'{100*r["if_not"]:.2f}% if not '
                         f'<span class="d">({r["swing"]*100:+.2f} pts)</span></div>')
            p.append('</div>')
    return "".join(p)


def encrypt_page(fragment_html: str, passphrase: str) -> str:
    salt = os.urandom(16)
    iv = os.urandom(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt,
                     iterations=PBKDF2_ITERS)
    key = kdf.derive(passphrase.encode("utf-8"))
    ct = AESGCM(key).encrypt(iv, fragment_html.encode("utf-8"), None)
    b64 = lambda x: base64.b64encode(x).decode("ascii")
    return PAGE_TEMPLATE.replace("__SALT__", b64(salt)) \
                        .replace("__IV__", b64(iv)) \
                        .replace("__CT__", b64(ct)) \
                        .replace("__ITERS__", str(PBKDF2_ITERS))


def build(passphrase: str, n_sims: int = 50_000, seed: int = 19) -> Path:
    data = compute(n_sims, seed)
    html = encrypt_page(render_fragment(data), passphrase)
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    out = SITE_DIR / PAGE_NAME
    out.write_text(html)
    return out


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Private · Bet Tracker</title>
<style>
  :root{--bg:#0e1320;--card:#161e31;--text:#e8ecf5;--muted:#93a0b8;--accent:#4cc38a;
    --accent2:#f5c542;--line:#26314f;--bad:#ff6b6b;}
  *{box-sizing:border-box;}
  body{margin:0;background:var(--bg);color:var(--text);
    font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
  main{max-width:780px;margin:0 auto;padding:1.2rem;}
  h1{font-size:1.4rem;text-align:center;margin:.6rem 0 .2rem;}
  h2{margin-top:2rem;font-size:1.15rem;color:var(--accent2);border-bottom:2px solid var(--line);padding-bottom:.3rem;}
  h3{margin:0;font-size:1.1rem;color:var(--accent);}
  .lock{max-width:420px;margin:5rem auto;background:var(--card);padding:1.6rem;border-radius:14px;text-align:center;}
  .lock input{width:100%;padding:.7rem;margin:.8rem 0;border-radius:8px;border:1px solid var(--line);
    background:#0e1320;color:var(--text);font-size:1rem;}
  .lock button{width:100%;padding:.7rem;border:0;border-radius:8px;background:var(--accent);
    color:#06281a;font-weight:700;font-size:1rem;cursor:pointer;}
  .lock label{display:flex;gap:.5rem;align-items:center;justify-content:center;color:var(--muted);font-size:.85rem;margin-top:.6rem;}
  .err{color:var(--bad);min-height:1.2em;font-size:.9rem;margin-top:.6rem;}
  .meta{color:var(--muted);font-size:.85rem;}
  .card{background:var(--card);border-radius:12px;padding:1rem 1.1rem;margin:1rem 0;border:1px solid var(--line);}
  .cardhead{display:flex;justify-content:space-between;align-items:center;gap:.5rem;}
  .ev{font-size:.8rem;font-weight:700;padding:.2rem .5rem;border-radius:999px;white-space:nowrap;}
  .ev.good{background:rgba(76,195,138,.18);color:var(--accent);}
  .ev.bad{background:rgba(255,107,107,.18);color:var(--bad);}
  .ev.flat{background:rgba(147,160,184,.18);color:var(--muted);}
  .stake{margin:.3rem 0 .6rem;color:var(--text);} .mult{color:var(--muted);}
  .nums{display:flex;flex-wrap:wrap;gap:1rem;margin:.5rem 0 .8rem;}
  .nums div{display:flex;flex-direction:column;} .nums span{color:var(--muted);font-size:.72rem;text-transform:uppercase;letter-spacing:.04em;}
  .nums b{font-size:1.2rem;} .nums i{color:var(--muted);font-style:normal;font-size:.78rem;}
  table.legs{width:100%;border-collapse:collapse;font-size:.9rem;}
  table.legs td{padding:.32rem .2rem;border-top:1px solid var(--line);}
  table.legs td.pct{text-align:right;color:var(--muted);}
  tr.weak td{color:var(--accent2);} .wk{font-size:.7rem;background:rgba(245,197,66,.18);padding:.1rem .35rem;border-radius:5px;}
  .game{background:var(--card);border-radius:10px;padding:.6rem .8rem;margin:.6rem 0;border:1px solid var(--line);}
  .gh{font-size:.92rem;} .odds{color:var(--muted);font-size:.8rem;}
  .swing{font-size:.85rem;color:var(--muted);margin-top:.25rem;padding-left:.3rem;}
  .swing code{background:#0e1320;padding:.05rem .3rem;border-radius:4px;color:var(--accent);}
  .swing b{color:var(--text);} .swing .d{color:var(--muted);}
  footer{margin:2.5rem 0 1rem;text-align:center;color:var(--muted);font-size:.75rem;}
</style></head>
<body>
<div id="gate" class="lock">
  <h1>🔒 Private Bet Tracker</h1>
  <p class="meta">Enter the passphrase to decrypt.</p>
  <input id="pw" type="password" placeholder="Passphrase" autocomplete="current-password"
    onkeydown="if(event.key==='Enter')unlock()">
  <button onclick="unlock()">Unlock</button>
  <label><input id="remember" type="checkbox"> Remember on this device</label>
  <div id="err" class="err"></div>
</div>
<main id="content" style="display:none"></main>
<footer id="foot" style="display:none">Decrypted locally in your browser · ML model probabilities, not promises.</footer>
<script>
const SALT="__SALT__", IV="__IV__", CT="__CT__", ITERS=__ITERS__;
const b64=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
async function decrypt(pass){
  const enc=new TextEncoder();
  const km=await crypto.subtle.importKey("raw",enc.encode(pass),"PBKDF2",false,["deriveKey"]);
  const key=await crypto.subtle.deriveKey(
    {name:"PBKDF2",salt:b64(SALT),iterations:ITERS,hash:"SHA-256"},
    km,{name:"AES-GCM",length:256},false,["decrypt"]);
  const pt=await crypto.subtle.decrypt({name:"AES-GCM",iv:b64(IV)},key,b64(CT));
  return new TextDecoder().decode(pt);
}
async function reveal(pass){
  const html=await decrypt(pass);
  document.getElementById("content").innerHTML=html;
  document.getElementById("gate").style.display="none";
  document.getElementById("content").style.display="block";
  document.getElementById("foot").style.display="block";
}
async function unlock(){
  const pass=document.getElementById("pw").value;
  const err=document.getElementById("err"); err.textContent="";
  try{
    await reveal(pass);
    if(document.getElementById("remember").checked) localStorage.setItem("bp_pw",pass);
  }catch(e){ err.textContent="Wrong passphrase."; }
}
(async()=>{ const s=localStorage.getItem("bp_pw");
  if(s){ try{ await reveal(s); }catch(e){ localStorage.removeItem("bp_pw"); } } })();
</script>
</body></html>
"""


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(prog="worldcup.betpage")
    ap.add_argument("--sims", type=int, default=50_000)
    ap.add_argument("--seed", type=int, default=19)
    args = ap.parse_args(argv)
    pw = os.environ.get("BET_PAGE_PASSPHRASE")
    if not pw:
        raise SystemExit("Set BET_PAGE_PASSPHRASE in the environment.")
    out = build(pw, args.sims, args.seed)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
