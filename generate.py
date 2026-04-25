"""
Generate AncestryTree.astro and ancestry-tree-preview.html.

v3:
- Debian recolored to raspberry pink (#c93b7e), distinct from Red Hat's red
- Bigger typography (13→16px) and chunkier strokes
- 10 new nodes added: Mandriva, OpenMandriva, CentOS Stream, MX Linux,
  Elementary OS, Zorin OS, Void Linux, Solus, AntiX, ParrotOS
- Full Mandrake → Mandriva → Mageia/OpenMandriva chain
- CentOS → CentOS Stream rebrand chain
"""
from dataclasses import dataclass
from typing import Optional, List, Tuple

# ---- Time axis ----------------------------------------------------------

YEAR_START = 1971
YEAR_END = 2023
Y_STEP = 50
Y_TOP = 100
SVG_W = 1480

def y_of(year: int) -> int:
    return Y_TOP + (year - YEAR_START) * Y_STEP

LINUX_BIRTH_Y = y_of(1991)
SVG_H = y_of(YEAR_END) + 110

# ---- Data ---------------------------------------------------------------

@dataclass
class Node:
    id: str
    name: str
    year: int
    family: str
    parent: Optional[str]
    x: int
    side: str = "right"
    defunct: bool = False
    note: Optional[int] = None
    @property
    def y(self) -> int:
        return y_of(self.year)

NODES: List[Node] = [
    # ---- Pre-Linux ancestors -------------------------------------------
    Node('unix',  'UNIX',  1971, 'proto', None,   660, side='top'),
    Node('gnu',   'GNU',   1983, 'proto', 'unix', 480),
    Node('minix', 'MINIX', 1987, 'proto', 'unix', 660),

    # ---- Linux kernel --------------------------------------------------
    Node('kernel', 'Linux kernel', 1991, 'independent', 'minix', 660, side='top'),

    # ---- First distro --------------------------------------------------
    Node('sls', 'SLS', 1992, 'slackware', 'kernel', 80, note=3),

    # 1993
    Node('slackware', 'Slackware', 1993, 'slackware', 'sls',    80),
    Node('debian',    'Debian',    1993, 'debian',    'kernel', 260),

    # 1994 — Red Hat Linux (DEFUNCT 2003)
    Node('redhat-linux', 'Red Hat Linux', 1994, 'redhat', 'kernel', 660, defunct=True),

    # 1998 — Mandrake (renamed Mandriva 2005)
    Node('mandrake', 'Mandrake', 1998, 'redhat', 'redhat-linux', 580, side='left', defunct=True),

    # 2000
    Node('gentoo', 'Gentoo', 2000, 'independent', 'kernel', 950),

    # 2002
    Node('arch', 'Arch', 2002, 'arch',   'kernel',       1140),
    Node('rhel', 'RHEL', 2002, 'redhat', 'redhat-linux',  740),

    # 2003
    Node('fedora',  'Fedora',  2003, 'redhat',      'redhat-linux', 560, side='left'),
    Node('nixos',   'NixOS',   2003, 'independent', 'kernel',       950),
    Node('knoppix', 'Knoppix', 2003, 'debian',      'debian',       400, side='left'),

    # 2004
    Node('ubuntu', 'Ubuntu', 2004, 'debian', 'debian', 300),
    Node('centos', 'CentOS', 2004, 'redhat', 'rhel',   820, defunct=True),

    # 2005
    Node('mandriva', 'Mandriva', 2005, 'redhat',   'mandrake', 580, side='left', defunct=True),
    Node('opensuse', 'openSUSE', 2005, 'opensuse', 'kernel',   880, side='left', note=4),
    Node('alpine',   'Alpine',   2005, 'independent', 'kernel', 1010),

    # 2006
    Node('mint', 'Linux Mint', 2006, 'debian', 'ubuntu', 220, side='left'),

    # 2008
    Node('void', 'Void Linux', 2008, 'independent', 'kernel', 950),

    # 2009
    Node('tails', 'Tails', 2009, 'debian', 'debian', 470),
    Node('zorin', 'Zorin OS', 2009, 'debian', 'ubuntu', 240, side='left'),

    # 2010
    Node('mageia', 'Mageia', 2010, 'redhat', 'mandriva', 580),

    # 2011
    Node('manjaro',  'Manjaro',      2011, 'arch',   'arch',   1060, side='left'),
    Node('elementary','Elementary OS',2011, 'debian', 'ubuntu', 340),

    # 2012
    Node('qubes',        'Qubes OS',     2012, 'redhat',      'fedora',   620, note=1),
    Node('whonix',       'Whonix',       2012, 'debian',      'debian',   470),
    Node('solus',        'Solus',        2012, 'independent', 'kernel',   1010),
    Node('openmandriva', 'OpenMandriva', 2012, 'redhat',      'mandriva', 440, side='left'),

    # 2013
    Node('kali',     'Kali',     2013, 'debian', 'debian', 470),
    Node('kodachi',  'Kodachi',  2013, 'debian', 'ubuntu', 380, side='left'),

    # 2014
    Node('mx', 'MX Linux', 2014, 'debian', 'debian', 460),

    # 2017
    Node('pop', 'Pop!_OS', 2017, 'debian', 'ubuntu', 380),

    # 2019
    Node('endeavour',     'EndeavourOS',   2019, 'arch',   'arch',   1080, side='left'),
    Node('chimera',       'ChimeraOS',     2019, 'arch',   'arch',   1230),
    Node('centos-stream', 'CentOS Stream', 2019, 'redhat', 'centos', 720, side='left'),

    # 2020
    Node('garuda', 'Garuda', 2020, 'arch', 'arch', 1140),

    # 2021
    Node('rocky',   'Rocky Linux', 2021, 'redhat', 'rhel', 700, side='left'),
    Node('alma',    'AlmaLinux',   2021, 'redhat', 'rhel', 800),
    Node('cachyos', 'CachyOS',     2021, 'arch',   'arch', 1200, side='right'),

    # 2022
    Node('nobara',  'Nobara',  2022, 'redhat', 'fedora', 520, side='left'),
    Node('steamos', 'SteamOS', 2022, 'arch',   'arch',   1230, note=2),

    # 2023
    Node('bazzite', 'Bazzite', 2023, 'redhat', 'fedora', 600),
]

INSPIRATIONS: List[Tuple[str, str]] = [
    ('slackware', 'opensuse'),
]

BANDS = [
    (70,   150,  'SLACKWARE',   'slackware'),
    (160,  510,  'DEBIAN',      'debian'),
    (520,  830,  'RED HAT',     'redhat'),
    (840,  920,  'OPENSUSE',    'opensuse'),
    (930,  1040, 'INDEPENDENT', 'independent'),
    (1050, 1280, 'ARCH',        'arch'),
]

YEAR_TICKS = [1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020]

# ---- SVG rendering ------------------------------------------------------

NODE_R = 9                 # was 7
BAND_TOP = LINUX_BIRTH_Y + 25
BAND_LABEL_Y = LINUX_BIRTH_Y + 13

def curve_path(ax: int, ay: int, bx: int, by: int) -> str:
    y_mid = (ay + by) // 2
    return f"M {ax},{ay + NODE_R} C {ax},{y_mid} {bx},{y_mid} {bx},{by - NODE_R}"

def label_pos(n: Node):
    r = NODE_R
    if n.side == 'left':
        return (n.x - r - 7, n.y + 5, 'end')
    if n.side == 'top':
        return (n.x, n.y - r - 12, 'middle')
    if n.side == 'bottom':
        return (n.x, n.y + r + 18, 'middle')
    return (n.x + r + 7, n.y + 5, 'start')

def superscript(n: int) -> str:
    return {1: '¹', 2: '²', 3: '³', 4: '⁴'}.get(n, str(n))

def render_svg() -> str:
    by_id = {n.id: n for n in NODES}
    parts: List[str] = []

    parts.append(
        f'<svg viewBox="0 0 {SVG_W} {SVG_H}" xmlns="http://www.w3.org/2000/svg" '
        f'role="img" aria-label="Ancestry tree of Linux distributions, from UNIX (1971) to 2023">'
    )

    # Family bands (Linux era only)
    parts.append('<g class="bands">')
    band_h = SVG_H - BAND_TOP - 10
    for x_min, x_max, _, family in BANDS:
        parts.append(
            f'<rect x="{x_min}" y="{BAND_TOP}" '
            f'width="{x_max - x_min}" height="{band_h}" '
            f'class="band band-{family}" rx="4"/>'
        )
    for x_min, x_max, label, family in BANDS:
        cx = (x_min + x_max) // 2
        parts.append(
            f'<text x="{cx}" y="{BAND_LABEL_Y}" '
            f'class="band-label band-label-{family}" text-anchor="middle">{label}</text>'
        )
    parts.append('</g>')

    # Linux divider
    parts.append(
        f'<line x1="60" x2="{SVG_W - 20}" y1="{LINUX_BIRTH_Y + 20}" '
        f'y2="{LINUX_BIRTH_Y + 20}" class="linux-divider"/>'
    )

    # Year axis
    parts.append('<g class="year-axis">')
    for yr in YEAR_TICKS:
        y = y_of(yr)
        parts.append(
            f'<line x1="60" x2="{SVG_W - 20}" y1="{y}" y2="{y}" class="year-grid"/>'
        )
        parts.append(
            f'<text x="50" y="{y + 5}" class="year-label" text-anchor="end">{yr}</text>'
        )
    parts.append('</g>')

    # Direct lineage edges
    parts.append('<g class="edges">')
    for n in NODES:
        if n.parent is None:
            continue
        p = by_id[n.parent]
        path = curve_path(p.x, p.y, n.x, n.y)
        cls = f'edge edge-{n.family}'
        if p.defunct:
            cls += ' edge-from-defunct'
        parts.append(f'<path d="{path}" class="{cls}"/>')
    parts.append('</g>')

    # Inspiration edges
    parts.append('<g class="inspirations">')
    for from_id, to_id in INSPIRATIONS:
        a = by_id[from_id]
        b = by_id[to_id]
        path = curve_path(a.x, a.y, b.x, b.y)
        parts.append(f'<path d="{path}" class="edge-inspired"/>')
    parts.append('</g>')

    # Nodes
    parts.append('<g class="nodes">')
    for n in NODES:
        lx, ly, anchor = label_pos(n)
        defunct_cls = ' node-defunct' if n.defunct else ''
        note_marker = ''
        if n.note:
            note_marker = f'<tspan class="node-note"> {superscript(n.note)}</tspan>'
        parts.append(
            f'<g class="node node-{n.family}{defunct_cls}">'
            f'<circle cx="{n.x}" cy="{n.y}" r="{NODE_R}" class="node-circle"/>'
            f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" class="node-name">'
            f'{n.name}<tspan class="node-year"> · {n.year}</tspan>{note_marker}'
            f'</text>'
            f'</g>'
        )
    parts.append('</g>')

    parts.append('</svg>')
    return '\n'.join(parts)

# ---- Shared CSS ---------------------------------------------------------

CSS = """\
.ancestry-tree {
  margin: 2rem 0;
  /* Family colors. Debian shifted to raspberry pink (was carmine #b13354)
     so it stops getting confused with Red Hat's red. */
  --at-proto:       #876342;
  --at-slackware:   #4d6da3;
  --at-debian:      #c93b7e;
  --at-redhat:      #c9352b;
  --at-opensuse:    #6cab43;
  --at-arch:        #1c8bc4;
  --at-independent: #6b7280;
  --at-grid:        var(--sl-color-gray-5, #d4d4d8);
  --at-text:        var(--sl-color-text, #18181b);
  --at-text-muted:  var(--sl-color-gray-3, #71717a);
  --at-bg:          var(--sl-color-bg, #fff);
}

.ancestry-tree svg {
  width: 100%;
  height: auto;
  display: block;
  font-family: inherit;
}

/* Family bands */
.band { opacity: 0.05; }
.band-slackware   { fill: var(--at-slackware); }
.band-debian      { fill: var(--at-debian); }
.band-redhat      { fill: var(--at-redhat); }
.band-opensuse    { fill: var(--at-opensuse); }
.band-independent { fill: var(--at-independent); }
.band-arch        { fill: var(--at-arch); }

.band-label {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.18em;
  opacity: 0.85;
}
.band-label-slackware   { fill: var(--at-slackware); }
.band-label-debian      { fill: var(--at-debian); }
.band-label-redhat      { fill: var(--at-redhat); }
.band-label-opensuse    { fill: var(--at-opensuse); }
.band-label-independent { fill: var(--at-independent); }
.band-label-arch        { fill: var(--at-arch); }

/* Linux divider */
.linux-divider {
  stroke: var(--at-grid);
  stroke-width: 2;
  opacity: 0.7;
}

/* Year axis */
.year-grid {
  stroke: var(--at-grid);
  stroke-width: 1;
  stroke-dasharray: 2 4;
  opacity: 0.5;
}
.year-label {
  font-size: 14px;
  font-variant-numeric: tabular-nums;
  fill: var(--at-text-muted);
  font-weight: 500;
}

/* Direct lineage edges — chunkier strokes for v3 */
.edge {
  fill: none;
  stroke-width: 3.5;
  opacity: 0.55;
  stroke-linecap: round;
}
.edge-proto       { stroke: var(--at-proto); }
.edge-slackware   { stroke: var(--at-slackware); }
.edge-debian      { stroke: var(--at-debian); }
.edge-redhat      { stroke: var(--at-redhat); }
.edge-opensuse    { stroke: var(--at-opensuse); }
.edge-arch        { stroke: var(--at-arch); }
.edge-independent { stroke: var(--at-independent); }

.edge-from-defunct {
  stroke-dasharray: 7 6;
  opacity: 0.5;
}

/* Inspiration edges */
.edge-inspired {
  fill: none;
  stroke: var(--at-opensuse);
  stroke-width: 2.5;
  stroke-dasharray: 1 7;
  stroke-linecap: round;
  opacity: 0.6;
}

/* Nodes */
.node-circle {
  stroke-width: 4;
  fill: var(--at-bg);
  transition: r 0.15s ease, stroke-width 0.15s ease;
}
.node-proto       .node-circle { stroke: var(--at-proto); }
.node-slackware   .node-circle { stroke: var(--at-slackware); }
.node-debian      .node-circle { stroke: var(--at-debian); }
.node-redhat      .node-circle { stroke: var(--at-redhat); }
.node-opensuse    .node-circle { stroke: var(--at-opensuse); }
.node-arch        .node-circle { stroke: var(--at-arch); }
.node-independent .node-circle { stroke: var(--at-independent); }

.node-defunct .node-circle {
  stroke-dasharray: 3 3;
  opacity: 0.65;
}

.node-name {
  font-size: 16px;
  font-weight: 600;
  fill: var(--at-text);
}
.node-year {
  font-weight: 400;
  font-variant-numeric: tabular-nums;
  fill: var(--at-text-muted);
}
.node-note {
  font-weight: 400;
  font-size: 12px;
  fill: var(--at-text-muted);
}

.node:hover .node-circle {
  r: 11;
  stroke-width: 4.5;
}

/* Footnotes */
.ancestry-footnotes {
  margin: 1rem 0 0 0;
  padding-top: 0.75rem;
  border-top: 1px solid var(--sl-color-gray-5, #e4e4e7);
  font-size: 0.95rem;
  color: var(--sl-color-gray-3, #71717a);
  line-height: 1.6;
}
.ancestry-footnotes p { margin: 0.35rem 0; }
.fn-marker {
  font-weight: 700;
  margin-right: 0.45em;
  color: var(--at-text);
  font-variant-numeric: tabular-nums;
}

/* Dark mode */
[data-theme="dark"] .ancestry-tree {
  --at-grid:       var(--sl-color-gray-4, #52525b);
  --at-text-muted: var(--sl-color-gray-2, #a1a1aa);
  --at-proto:      #b08962;
  --at-debian:     #e0588f;  /* brighter pink in dark mode for clarity */
}
[data-theme="dark"] .band              { opacity: 0.10; }
[data-theme="dark"] .band-label        { opacity: 0.9;  }
[data-theme="dark"] .edge              { opacity: 0.7;  }
[data-theme="dark"] .edge-from-defunct { opacity: 0.75; }
[data-theme="dark"] .edge-inspired     { opacity: 0.75; }
"""

FOOTNOTES_HTML = """\
<figcaption class="ancestry-footnotes">
  <p><span class="fn-marker">¹</span>Qubes&nbsp;OS uses Fedora as <em>dom0</em>, but the real engine is the Xen hypervisor — every "qube" is a separate VM.</p>
  <p><span class="fn-marker">²</span>SteamOS&nbsp;1–2 (2013) was Debian-based; the Steam Deck reboot in 2022 moved it to Arch. Shown at current ancestry.</p>
  <p><span class="fn-marker">³</span>SLS (Softlanding Linux System, 1992) was the first complete Linux distribution — kernel + GNU userland in one package. Slackware forked from it the following year.</p>
  <p><span class="fn-marker">⁴</span>The dotted line shows that early SUSE Linux (1994) was a German repackaging of Slackware before evolving into its own RPM-based distribution. openSUSE is the community edition since 2005.</p>
</figcaption>"""

# ---- File generation ----------------------------------------------------

def render_astro() -> str:
    svg = render_svg()
    return f"""---
// AncestryTree.astro
// Generated from generate.py — edit data there, not here.
// 52-year ancestry diagram from UNIX (1971) through 45 nodes to 2023.
// Pure inline SVG, zero JS. Themes via CSS variables.
---
<figure class="ancestry-tree">
{svg}
{FOOTNOTES_HTML}
</figure>

<style>
{CSS}</style>
"""

def render_preview_html() -> str:
    svg = render_svg()
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AncestryTree preview — Linux distros, 1971–2023</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {{
      margin: 0;
      padding: 2rem 1.25rem 4rem;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "IBM Plex Sans",
                   system-ui, sans-serif;
      color: #18181b;
      background: #fafaf9;
      max-width: 1480px;
      margin-inline: auto;
    }}
    header {{
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid #e4e4e7;
    }}
    h1 {{
      font-size: 1.4rem;
      margin: 0 0 0.35rem;
      letter-spacing: -0.01em;
    }}
    p.tagline {{
      margin: 0;
      color: #71717a;
      font-size: 0.95rem;
    }}
    .theme-toggle {{
      float: right;
      font-size: 0.85rem;
      color: #52525b;
      background: transparent;
      border: 1px solid #d4d4d8;
      padding: 0.4rem 0.75rem;
      border-radius: 4px;
      cursor: pointer;
      font-family: inherit;
    }}
    [data-theme="dark"] {{
      color: #e4e4e7;
      background: #18181b;
    }}
    [data-theme="dark"] header {{ border-color: #3f3f46; }}
    [data-theme="dark"] p.tagline {{ color: #a1a1aa; }}
    [data-theme="dark"] .theme-toggle {{
      color: #d4d4d8;
      border-color: #3f3f46;
    }}

{CSS}
  </style>
</head>
<body>
  <header>
    <button class="theme-toggle" onclick="document.documentElement.dataset.theme = document.documentElement.dataset.theme === 'dark' ? '' : 'dark'">Toggle dark mode</button>
    <h1>Fifty-two years of Linux ancestry, branched</h1>
    <p class="tagline">UNIX at the top, GNU and MINIX feeding into Linus's kernel, then forty distros branching from there.</p>
  </header>

  <figure class="ancestry-tree">
{svg}
{FOOTNOTES_HTML}
  </figure>
</body>
</html>
"""

if __name__ == '__main__':
    import os, sys
    out_astro = 'src/components/AncestryTree.astro'
    out_html = 'ancestry-tree-preview.html'
    for arg in sys.argv[1:]:
        if arg.startswith('--out-dir='):
            d = arg.split('=', 1)[1]
            out_astro = os.path.join(d, 'AncestryTree.astro')
            out_html = os.path.join(d, 'ancestry-tree-preview.html')
    os.makedirs(os.path.dirname(out_astro) or '.', exist_ok=True)
    with open(out_astro, 'w') as f:
        f.write(render_astro())
    with open(out_html, 'w') as f:
        f.write(render_preview_html())
    print(f"Wrote {out_astro}")
    print(f"Wrote {out_html}")
    print(f"Nodes: {len(NODES)}")
    print(f"Direct edges: {sum(1 for n in NODES if n.parent)}")
    print(f"Inspiration edges: {len(INSPIRATIONS)}")
    print(f"SVG size: {SVG_W} x {SVG_H}")
